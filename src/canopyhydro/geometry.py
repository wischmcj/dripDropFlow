"""Spacially centeric code"""
from __future__ import annotations

import functools
import logging
import math

import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.spatial import Delaunay, distance
from shapely.geometry import MultiLineString, MultiPoint, MultiPolygon, Polygon
from shapely.ops import polygonize, unary_union

from canopyhydro.configuration import output_dir
from canopyhydro.DataClasses import coord_list
from canopyhydro.utils import _try_import

log = logging.getLogger("model")

if has_geopandas := _try_import("geopandas"):
    from geopandas import GeoSeries


if has_matplotlib := _try_import("matplotlib"):
    import matplotlib.pyplot as plt
    from matplotlib.collections import PatchCollection
    from matplotlib.colors import to_rgba
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path

    # Plots a Polygon to pyplot `ax`
    def polygon_plot(ax, polys: list | Polygon, **kwargs):
        if isinstance(polys, Polygon):
            polys = [polys]
        if isinstance(polys, MultiPolygon):
            polys = list(polys.geoms)
        colors = kwargs.get("facecolor", ["grey"])
        if isinstance(colors, str):
            colors = list(colors)
        union_dict = {color: [] for color in colors}
        for poly, color in zip(polys, colors):
            union_dict[color].append(poly)
        for color, polys in union_dict.items():
            if polys != []:
                to_draw = unary_union(polys)
                kwargs["facecolor"] = to_rgba(color)

                path = Path.make_compound_path(
                    Path(np.asarray(to_draw.exterior.coords)[:, :2]),
                    *[
                        Path(np.asarray(ring.coords)[:, :2])
                        for ring in to_draw.interiors
                    ],
                )

                patch = PathPatch(path, **kwargs)
                collection = PatchCollection([patch], **kwargs)
                ax.add_collection(collection, autolim=True)
                ax.autoscale_view()
        return collection
else:

    def polygon_plot(ax, poly, **kwargs):
        raise ImportError("matplotlib is required to plot polygons")


### Functions relating to Alpha Shapes
def circumcenter_lapack(points: coord_list) -> np.ndarray:
    """
    Calculate the circumcenter of a set of points relative to simplex
    https://en.wikipedia.org/wiki/Polarization_identity
    """
    points = np.asarray(points)
    rows, _ = points.shape
    A = np.bmat(
        obj=[
            [2 * np.dot(points, points.T), np.ones((rows, 1))],
            [np.ones((1, rows)), np.zeros((1, 1))],
        ]
    )
    b = np.hstack((np.sum(points * points, axis=1), np.ones(1)))
    return np.array(np.linalg.solve(A, b)[:-1])


def circumcenter_lu_factor(points: coord_list) -> np.ndarray:
    """
    Calculate the circumcenter of a set of points relative to simplex
    Theoretically less efficient than LAPACK (O(n^3) + O(n^2) v. O(n^2))
    when a given set of equations (e.g. set of points, A )
    only needs to be solved for a single vector (e.g b)
    """
    points = np.asarray(points)
    rows, _ = points.shape
    A = np.bmat(
        obj=[
            [2 * np.dot(points, points.T), np.ones((rows, 1))],
            [np.ones((1, rows)), np.zeros((1, 1))],
        ]
    )
    b = np.hstack((np.sum(points * points, axis=1), np.ones(1)))
    lu, piv = lu_factor(A)
    sir_c = lu_solve((lu, piv), b)
    return sir_c


def circumradius(points: coord_list, center: np.ndarray = []) -> np.float32:
    """
    Calculte the radius of the circle in which the given polygon may be inscribed
    """
    points = np.asarray(points)
    return np.linalg.norm(points[0, :] - np.dot(center, points))


def simplices(points: coord_list) -> coord_list:
    """
    Yields simpicies and radius
    """
    coords = np.asarray(points)
    tri = Delaunay(coords)

    for simplex in tri.simplices:
        simplex_points = coords[simplex]
        try:
            center = circumcenter_lapack(simplex_points)
            yield simplex, circumradius(simplex_points, center), center
        except np.linalg.LinAlgError as err:
            log.warning(
                f"""Error calculating simplicies,
                        input invalid (potentially coincident points)
                         {err}"""
            )


def maximal_alpha(boundary_points: coord_list, union_poly: Polygon) -> np.float32:
    """
    Finds the minimal alpha shape for the given
    coord list that still contains the given polygon
    """
    upper = (
        10  # annectotally seems to be plenty high to ensure a discontinuous alpha shape
    )
    lower = 0
    iterations = 10
    runs = 0
    while runs <= iterations:
        alpha = (upper - lower) / 2
        hull, _ = concave_hull(boundary_points, union_poly)
        if hull.contains(Polygon):
            # The tested curvature is less than or equal to the max curvature for a continuous alpha shape
            lower = alpha
        else:
            # The tested curvature is greater than or equal to the max curvature for a continuous alpha shape
            upper = alpha
        runs += 1
    return alpha


# @profile
# might eventually be updated to deal
# with 3d a la https://github.com/bellockk/alphashape/blob/master/alphashape/optimizealpha.py
def concave_hull(boundary_points, alpha: int = 0):
    """alpha shape / concave hull
    Creates a delaunay triangulation on the set of points. Using this triangulation,
    returns a minimal concave polygon with a concavity factor alpha
    see: trunk_lean
    """

    if len(boundary_points) < 4:
        # When you have a triangle, there is no sense in computing an alpha
        # shape.
        return MultiPoint(list(boundary_points)).convex_hull, boundary_points, set()

    def add_edge(edges, edge_points, coords, i, j):
        # adds a line between points i and j
        if (i, j) in edges or (j, i) in edges:
            # already added
            return
        edges.add((i, j))
        edge_points.append(coords[[i, j]])

    def add_center(centers, center):
        centers.add((center[0], center[1], center[2]))

    coords = np.array(
        sorted(point.coords[0] for point in boundary_points if len(point.coords) > 0)
    )

    # Find minimal set of triangles with points in set

    edges = set()
    centers = set()
    edge_points = []
    # loop over triangles:
    # ia, ib, ic = indices of corner points of the triangle
    tri = simplices(coords)

    for (ia, ib, ic), _, center in tri:
        if len(coords[0]) == 2:
            # simpler logic suffices in 2d
            pa = coords[ia]
            pb = coords[ib]
            pc = coords[ic]

            # Lengths of sides of triangle
            a = math.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
            b = math.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
            c = math.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)

            # Semiperimeter of triangle
            s = (a + b + c) / 2.0

            # Area of triangle by Heron's formula
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            circum_r = a * b * c / (4.0 * area)

            # Here's the radius filter.
            # print circum_r
            if circum_r < 1.0 / alpha:
                add_edge(edges, edge_points, coords, ia, ib)
                add_edge(edges, edge_points, coords, ib, ic)
                add_edge(edges, edge_points, coords, ic, ia)
                add_center(centers, center)
        else:
            raise (Exception("3D alpha shapes not yet supported"))
    m = MultiLineString(edge_points)
    triangles = list(polygonize(m))
    return unary_union(triangles), edge_points, centers


# def draw_vectors(vectors: list[tuple[list[int]]],
#                  colors: Optional[list[str]] = ["black"],
#                  save: bool = False,
#                  show: bool = False,
#                  file_name_ext: str = "",
#                  )->tuple[int,int,int]:
#     """Gets the x, y and z coordinates from a list of vectors
#         as separate lists.

#     ### Args:
#         - `vectors (list[tuple[list[int]]])`: _description_

#     ### Returns:
#         - `_type_`: _description_
#     """
#     for x,y,z in vectors:
#         plt.plot(x, y, z, color="black")
#     if save:
#         save_dir = "/".join(
#             [str(output_dir), "draw_vectors", f"{file_name_ext.replace('.','')}"]
#         )  # .replace("/", "\\")
#         plt.savefig(save_dir, dpi=3000)
#     if show:
#         plt.show()


### Functions relating to 2D Cylinder Projections
def get_projection(vector: list, magnitude: list, radius: float()):
    """
    Takes in the vector (starting point), magnitude and radius that fully define a cylinder.
    Finds the projection of the cylinder on a plane

    Some linear algebra/diff eq could help us find this for an arbitrary plane.
    """
    noCirPoints = 360
    tCir = np.linspace(
        0, 2 * np.pi, noCirPoints
    )  # 360 evenly spaced points between 0 - 2pi (radian degrees)
    a_ortho = np.cos(tCir)  # x coordinates of the points on a circle
    b_ortho = np.sin(tCir)  # y coordinates of the points on a circle
    delt_a = magnitude[0]
    delt_b = magnitude[1]
    delt_c = magnitude[2]
    dim_a = vector[0]
    dim_b = vector[1]
    # unit vector at base of cylinder, pointing up cylinder axis
    vNorm = np.sqrt(delt_a**2 + delt_b**2 + delt_c**2)
    aV = np.hstack((delt_a, delt_b, delt_c)) / vNorm
    bV = -aV  # unit vector looking down from top circle (but not translated)
    # function to find the z component of an orthogonal vector in 3D
    # oVz = lambda v, a, b: ((-v[0] * a - v[1] * b) / v[2])

    # initializing min max arrays+
    projection = {
        "polygon": Polygon(),
        "base_vector": (0, 0, 0),
        "anti_vector": (0, 0, 0),
        "angle": 0,
        "area": 0,
    }
    c1 = Polygon()
    bBox = Polygon()
    c2 = Polygon()
    # coord_list = []
    try:
        # for each cylinder
        if not np.isnan(dim_a[0]):
            if np.logical_and(delt_a == 0, delt_b == 0):
                pX = dim_a[0] + radius * a_ortho
                pY = dim_b[0] + radius * b_ortho
                cPS = Polygon(list(zip(pX, pY)))
                ang = 0
                projection = {
                    "polygon": cPS,
                    "base_vector": aV,
                    "anti_vector": bV,
                    "angle": ang,
                    "area": cPS.area,
                }
                return projection
            else:
                # find orthogonal unit vectors @ endpoints
                # Identifies corners of projected rectangle
                # Recall that aV is a unit vector pointing 'up' the cylinder
                aVp1 = np.hstack((aV[1], -aV[0]))
                aVp2 = np.hstack((-aV[1], aV[0]))
                bVp1 = np.hstack((bV[1], -bV[0]))
                bVp2 = np.hstack((-bV[1], bV[0]))
                aVp1 = aVp1 / np.linalg.norm(aVp1)
                aVp2 = aVp2 / np.linalg.norm(aVp2)
                bVp1 = bVp1 / np.linalg.norm(bVp1)
                bVp2 = bVp2 / np.linalg.norm(bVp2)
                # from each endpoint, use radius to find points on the edge of
                # the circle representing the end of the cylinder
                # vertices of the rectangle
                x1 = dim_a[0] + radius * aVp1[0]
                y1 = dim_b[0] + radius * aVp1[1]
                x2 = dim_a[0] + radius * aVp2[0]
                y2 = dim_b[0] + radius * aVp2[1]
                x3 = dim_a[1] + radius * bVp1[0]
                y3 = dim_b[1] + radius * bVp1[1]
                x4 = dim_a[1] + radius * bVp2[0]
                y4 = dim_b[1] + radius * bVp2[1]

                if aV[2] != 0:
                    # calculate set of orthgonal vectors using lambda function
                    # That is 360 orthogonal vectors ending at eqidistant points along
                    # a circle of radius radius with the starting point of our cylinder
                    # at is center
                    ZOrtho = (-aV[0] * a_ortho - aV[1] * b_ortho) / aV[2]
                    # unit-ify the orthgonal vectors
                    uovd = np.sqrt(a_ortho**2 + b_ortho**2 + ZOrtho**2)
                    uov = (
                        np.hstack((a_ortho[:, None], b_ortho[:, None], ZOrtho[:, None]))
                        / uovd[:, None]
                    )
                    # donot re unit-fy, you only want the horizontal component, not the
                    # renormalized horizontal component
                    # using only the X and Y components, find circle coods in plane of
                    # interest
                    xaC = dim_a[0] + uov[:, 0] * radius
                    yaC = dim_b[0] + uov[:, 1] * radius
                    # zaC = dim_c[0] + uov[:, 2] * radius
                    xbC = dim_a[1] + uov[:, 0] * radius
                    ybC = dim_b[1] + uov[:, 1] * radius
                    # zbC = dim_c[1] + uov[:, 2] * radius
                    try:
                        c1c = list(
                            zip(
                                [0 if np.isnan(x) else x for x in xaC],
                                [0 if np.isnan(y) else y for y in yaC],
                            )
                        )
                        c2c = list(
                            zip(
                                [0 if np.isnan(x) else x for x in xbC],
                                [0 if np.isnan(y) else y for y in ybC],
                            )
                        )

                        # coord_list.extend(c1c)
                        # coord_list.extend(c2c)
                        c1 = Polygon(c1c)
                        c2 = Polygon(c2c)
                    except Exception as e:
                        log.error(
                            f"Error creating circular portions of the projections {e}"
                        )

                # assemble total package
                rX = np.vstack((x1, x2, x3, x4))
                rY = np.vstack((y1, y2, y3, y4))
                # test for circle parts in polygon
                try:
                    bBoxc = list(
                        zip(
                            [0 if np.isnan(x) else x for x in rX],
                            [0 if np.isnan(y) else y for y in rY],
                        )
                    )
                    # coord_list.extend(bBoxc)
                    bBox = Polygon(bBoxc)
                    partsPS = [c1, bBox, c2]
                except Exception as err:
                    log.error(
                        f"Error creating rectangular portion of the projection: {err=}: {vector=},{magnitude=}"
                    )
                try:
                    if np.max([poly_part.area for poly_part in partsPS]) > 0:
                        to_union = [poly for poly in partsPS if poly.area > 0]
                        cPS = unary_union([part for part in to_union])
                        # cPSc = Polygon(coord_list)
                except Exception as err:
                    log.error(f"Error unioning projection polygons: {err=} ")
                # get angle away from plane projected on to
                run = math.sqrt(delt_b**2 + delt_a**2)
                rise = delt_c
                if run == 0:
                    slope = 1  # straightDown e.g. is in flow
                else:
                    slope = rise / run
                ang = np.arctan(slope)
                projection = {
                    "polygon": cPS,
                    "base_vector": aV,
                    "anti_vector": bV,
                    "angle": ang,
                    "area": cPS.area,
                }
                return projection
        else:
            log.warning("dim_a[0] is null, unable to project")
        return projection
    except UnboundLocalError:
        log.error(
            f"UnboundLocalError: vector : {vector} magnitude: {magnitude} radius: {radius}"
        )


def get_projected_overlap(shading_poly_list: list[list[Polygon]], labels: list) -> dict:
    """Takes in a list of lists of polygons, w/
     each list representing a diff percentile
     grouping of polygons (e.g. grp1:(0%-25%), grp2:(25%, 50%)...)

    Consider the case in which our percentiles are defined by height,
    with the first grouping being cylinders in the xth %ile y height, thus being under than cylinders in all of the other groupings
    In this case, this function calculates the area of shade cast by each
    grouping on the below sections. As such, in each loop 'shading_poly_list'
    is partitioned into 2 categories: The sections of canopy on which shade is
    being cast and the sections of canopy that are casting that shade.
    After each loop, a new section of canopy is moved from the 'shading' group
    to the 'shaded' group and a new calculation of shaded area is made. The result
    is a cumulative sum of shaded area at various heights in the canopy.

    Note:
        shapely's intersection function could be used, and
        would be slightly more accurate. However, it is also
        rather slow for the intersection of this many shapes

    Returns:
         list[dict]: Each dicitonary corresponding to a percentile,
         with metrics describing the overlap between the polygons in that percentile
    
    Example:
         Result = {
             "sum_area": sum of areas of the polygons in the percentile,
             "effective_area": the area of the union of the polygons in the percentile,
             "internal_overlap": sum_area - effective_area,
             "overlap_with_previous": the area of the overlap between the polygons in the percentile,
                     with the polygons in the previous percentile,
        }
    """
    if len(labels) != len(shading_poly_list):
        log.info(
            f"Not enough labels; expected {len(shading_poly_list)} got {len(labels)}"
        )
    elif len(set(labels)) != len(labels):
        log.info("Labels must be distinct")
    else:
        overlap_dict = {}
        shaded_polys = []
        for idx, shader_polys in enumerate(shading_poly_list):
            shader_union_poly = unary_union(shader_polys)
            shader_sum = np.sum([poly.area for poly in shader_polys])
            shaded_union = unary_union(shaded_polys)
            total_union = unary_union(shaded_polys)

            shader_on_shaded_w_overlap = shader_union_poly.area + shaded_union.area
            shader_on_shaded_w_o_overlap = total_union.area
            shader_on_shaded_overlap = (
                shader_on_shaded_w_overlap - shader_on_shaded_w_o_overlap
            )

            shader_internal_overlap = shader_sum - shader_union_poly.area

            overlap_dict[labels[idx]] = {
                "sum_area": shader_sum,
                "effective_area": shader_union_poly.area,
                "internal_overlap": shader_internal_overlap,
                "overlap_with_previous": shader_on_shaded_overlap,
            }
            shaded_polys.extend(shader_polys)
        return overlap_dict


### Functions relating to 3D Cylinder Calculations
def get_rotation_matrix(b: np.array):
    if np.linalg.norm(b) == 0:
        return np.eye(3)
    # Sourced from https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula#Matrix_notation
    # b must be unit vector
    # a is the z unit vector
    a = [0, 0, 1]
    v = np.cross(b, a)
    s = np.linalg.norm(v)
    c = np.dot(b, a)
    # The skew-symmetric cross product matrix of v
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    # Rotation matrix as per Rodregues formula
    R = np.eye(3) + vx + np.dot(vx, vx) * ((1 - c) / (s**2))
    return R


@functools.lru_cache
def get_unoriented_cylinder(r, h, noCirPoints=20, nv=20):
    """
    Given the radius (r) and height (h), returns the parameterization of a cylinder
        centered on the z axis, with a base at the origin and oriented vertically
    """
    theta = np.linspace(0, 2 * np.pi, noCirPoints)
    v = np.linspace(0, h, nv)
    theta, v = np.meshgrid(theta, v)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = v
    return x, y, z


def get_cylinder_surface(radius, vector_start_end):
    """Returns points on the surface of the cylinder defined
    by the givent start and end points having the given radius

    """
    vector = vector_start_end[1] - vector_start_end[0]
    vector = np.array(vector)
    length = np.linalg.norm(vector)
    vu = vector / np.linalg.norm(vector)

    # Creates cylinder centered on the z axis with the base at the origin
    Xc, Yc, Zc = get_unoriented_cylinder(radius, length)

    # Creates matrix to rotate cylinder to the desired orientation
    R = get_rotation_matrix(vu)
    t = np.transpose(np.array([Xc, Yc, Zc]))
    x, y, z = np.transpose(t @ R, (2, 0, 1))

    # shifts now oriented cylinder to the desired position
    x = x + vector_start_end[0][0]
    y = y + vector_start_end[0][1]
    z = z + vector_start_end[0][2]
    return x, y, z, vu


## Functions relating to Drawing Cylinders
def draw_cyls(
    collection: list,
    colors: list[bool] = [True],
    save: bool = False,
    file_name_ext: str = "",
    overlay: list | None = None,
    overlay_transparency: float | None = None,
    show: bool = False,
):
    """Draws a collection of cylinders in 2 dimensions"""
    log.info("Plotting cylinder collection")

    fig, ax = plt.subplots()
    try:
        geoPolys = GeoSeries(collection)
    except Exception as e:
        log.error(f"Error creating GeoSeries, is gepandas installed? {e}")
        raise e

    colors = ["Blue" if col else "Grey" for col in colors]
    geoPolys.plot(ax=ax, color=colors)
    # polygon_plot(ax, collection, facecolor=colors)
    if overlay:
        for item in overlay:
            # The below if statements allow for the overlay to be:
            #   a single polygon or a list of polygons
            #       - in the case of watershed alpha shapes
            #   or a list of coordinate lists
            #       - in the case of drip points
            if isinstance(item, Polygon) or isinstance(item, MultiPolygon):
                polygon_plot(ax, item, facecolor=["grey"], alpha=overlay_transparency)
            if isinstance(item, list):
                if isinstance(item[0], Polygon):
                    polygon_plot(
                        ax,
                        item,
                        facecolor=["grey"] * len(item),
                        alpha=overlay_transparency,
                    )
                elif isinstance(item[0], list):
                    ax.scatter(*item, alpha=overlay_transparency, color="red")
            else:
                log.error(
                    "Overlay must be a Polygon, a list of Polygons or coordinate list"
                )
    if show:
        plt.show()
    if save:
        save_dir = "/".join(
            [str(output_dir), "draw", f"{file_name_ext.replace('.','')}"]
        )  # .replace("/", "\\")
        plt.savefig(save_dir, dpi=3000)
    return ax


def draw_cylinders_3D(
    radii: int,
    vector_start_ends: list,
    save: bool = False,
    show: bool = False,
    draw_vectors=False,
    draw_projections=False,
    file_name_ext: str = "3Ddraw",
):
    """Draws a single Cylinder in 3 dimensions"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    log.info("Plotting cylinder in 3D")
    for radius, vector_start_end in zip(radii, vector_start_ends):

        x, y, z, unit_vector = get_cylinder_surface(radius, vector_start_end)

        # setting up chart
        xlim = (np.min(x), np.max(x))
        ylim = (np.min(y), np.max(y))
        zlim = (np.min(z), np.max(z))

        ax.plot_surface(x, y, z, alpha=0.6)
        vector = vector_start_end[1] - vector_start_end[0]

        if draw_vectors:
            ax.quiver(
                vector_start_end[0][0],
                vector_start_end[0][1],
                vector_start_end[0][2],
                vector[0],
                vector[1],
                vector[2],
                color="black",
            )

        if draw_projections:
            axis_extension = 4
            xlim = (np.min(x) - axis_extension, np.max(x) + axis_extension)
            ylim = (np.min(y) - axis_extension, np.max(y) + axis_extension)
            zlim = (np.min(z) - axis_extension, np.max(z) + axis_extension)

            # In the figure created, the viewer is on the positive
            # side of the x and z axis, but the  negative side of the y axis
            # So, we need to offset the y (e.g. XZ projection) based on its 2nd coordinate
            ax.contourf(x, y, z, zdir="x", offset=xlim[0], colors="C0")
            ax.contourf(x, y, z, zdir="y", offset=ylim[1], colors="C0")
            ax.contourf(x, y, z, zdir="z", offset=zlim[0], colors="C0")

        # setting viewer perspective on chart
    ax.view_init(elev=30, azim=-45, roll=0)
    ax.set(xlim=xlim, ylim=ylim, zlim=zlim, xlabel="X", ylabel="Y", zlabel="Z")
    if show:
        plt.show()
    if save:
        save_dir = "/".join(
            [str(output_dir), "draw", f"{file_name_ext.replace('.','')}"]
        )  # .replace("/", "\\")
        plt.savefig(save_dir, dpi=3000)
    return fig


### Functions relating to Points in Space
def closest_points(point: tuple, points: np.array, num_returned: int = 3):
    """
    Finds the closest point in the list 'points' from the input 'point'
    """
    points_to_return = []
    distances = distance.cdist([point], points)
    for i in np.arange(num_returned):
        closest_index = distances.argmin()
        points_to_return.append(points[closest_index])
        distances = np.delete(distances, closest_index)

    return points_to_return[0] if num_returned == 1 else points_to_return


def furthest_point(
    point: tuple,
    points: np.array,
):
    """
    Finds the furthest point in the list 'points' from the input 'point'
    """
    distances = distance.cdist([point], points)
    furthest_index = distances.argmax()
    return points[furthest_index], distances[furthest_index]


# def drip_plot(**args):
#     plt.imshow(**args)
