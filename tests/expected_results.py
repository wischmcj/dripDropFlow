from __future__ import annotations

ten_cyls_rows = [
    "Cylinder(cyl_id=0.0, x=array([0.076822, 0.076822]), y=array([-3.386935, -3.386935]), z=array([-0.595933, -0.5315  ]), radius=0.222504, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=-1.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((-0.146 -0.596, -0.146 -0.532, 0.299 -0.532, 0.299 -0.596, -0.146 ...>, 'base_vector': array([0., 1., 0.]), 'anti_vector': array([-0., -1., -0.]), 'angle': 0.0, 'area': 0.02867320046400003}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=0.0, dy=0.0, dz=0.06443300000000007, surface_area=0.09007951593260982, sa_to_vol=8.98907453673384, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=1.0, x=array([0.076822, 0.058561]), y=array([-3.386935, -3.328717]), z=array([-0.5315  , -0.085599]), radius=0.211908, length=0.450057, branch_order=0.0, branch_id=0.0, volume=0.063491, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.288 -0.524, 0.285 -0.528, 0.279 -0.532, 0.279 -0.532, 0.27 -0.5...>, 'base_vector': array([-0.04057494,  0.99076758,  0.1293572 ]), 'anti_vector': array([ 0.04057494, -0.99076758, -0.1293572 ]), 'angle': 0.1297207099046939, 'area': 0.20736615874219783}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=-0.018261, dy=0.05821799999999966, dz=0.445901, surface_area=0.5992316474954436, sa_to_vol=9.438056535500206, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=2.0, x=array([0.058561, 0.062703]), y=array([-3.328717, -3.334542]), z=array([-0.085599,  0.232646]), radius=0.197783, length=0.318325, branch_order=0.0, branch_id=0.0, volume=0.03912, parent_id=1.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.251 -0.089, 0.185 -0.09, 0.142 -0.09, 0.119 -0.09, 0.106 -0.09,...>, 'base_vector': array([ 0.01301185,  0.99974789, -0.01829889]), 'anti_vector': array([-0.01301185, -0.99974789,  0.01829889]), 'angle': -0.01829991517737181, 'area': 0.12803206766193473}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=0.004141999999999993, dy=-0.005824999999999747, dz=0.318245, surface_area=0.3955847820488214, sa_to_vol=10.112085430695844, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=3.0, x=array([0.062703, 0.06246 ]), y=array([-3.334542, -3.357087]), z=array([0.232646, 0.499611]), radius=0.198531, length=0.267916, branch_order=0.0, branch_id=0.0, volume=0.033174, parent_id=2.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.261 0.233, 0.261 0.233, 0.257 0.229, 0.245 0.226, 0.23 0.224, 0...>, 'base_vector': array([-9.07002823e-04,  9.96452711e-01, -8.41497064e-02]), 'anti_vector': array([ 9.07002823e-04, -9.96452711e-01,  8.41497064e-02]), 'angle': -0.08424933726969241, 'area': 0.11639335885381917}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=-0.00024299999999999322, dy=-0.022545000000000037, dz=0.266965, surface_area=0.33420031048164517, sa_to_vol=10.07416381749699, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=4.0, x=array([0.06246 , 0.073532]), y=array([-3.357087, -3.374155]), z=array([0.499611, 0.779853]), radius=0.188766, length=0.280979, branch_order=0.0, branch_id=0.0, volume=0.031454, parent_id=3.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.247 0.49, 0.231 0.488, 0.21 0.487, 0.19 0.486, 0.173 0.486, 0.1...>, 'base_vector': array([ 0.03940501,  0.99737522, -0.06074464]), 'anti_vector': array([-0.03940501, -0.99737522,  0.06074464]), 'angle': -0.06078206239482508, 'area': 0.11264784664532754}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=0.011071999999999999, dy=-0.017068000000000083, dz=0.280242, surface_area=0.33325563682540077, sa_to_vol=10.595016113225686, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=5.0, x=array([0.073532, 0.067962]), y=array([-3.374155, -3.393301]), z=array([0.779853, 1.05038 ]), radius=0.187445, length=0.27126, branch_order=0.0, branch_id=0.0, volume=0.029942, parent_id=4.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.261 0.783, 0.254 0.78, 0.254 0.78, 0.239 0.777, 0.221 0.775, 0....>, 'base_vector': array([-0.02053374,  0.99729465, -0.07058151]), 'anti_vector': array([ 0.02053374, -0.99729465,  0.07058151]), 'angle': -0.07064024199476766, 'area': 0.10920049253428211}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=-0.0055700000000000055, dy=-0.019146000000000107, dz=0.2705270000000001, surface_area=0.3194769179782343, sa_to_vol=10.669858993328244, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=6.0, x=array([0.067962, 0.062838]), y=array([-3.393301, -3.386649]), z=array([1.05038 , 1.311286]), radius=0.19627, length=0.261041, branch_order=0.0, branch_id=0.0, volume=0.031591, parent_id=5.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.264 1.054, 0.223 1.05, 0.223 1.05, 0.179 1.048, 0.151 1.047, 0....>, 'base_vector': array([-0.01962909,  0.99948253,  0.02548258]), 'anti_vector': array([ 0.01962909, -0.99948253, -0.02548258]), 'angle': 0.025485337950285722, 'area': 0.10543431215535382}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=-0.00512399999999999, dy=0.006652000000000324, dz=0.26090599999999986, surface_area=0.3219159648746658, sa_to_vol=10.190116326633085, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=7.0, x=array([0.062838, 0.055451]), y=array([-3.386649, -3.429066]), z=array([1.311286, 1.581252]), radius=0.182718, length=0.273378, branch_order=1.0, branch_id=0.0, volume=0.028673, parent_id=6.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.245 1.314, 0.243 1.311, 0.243 1.311, 0.239 1.308, 0.233 1.305, ...>, 'base_vector': array([-0.02702122,  0.98751991, -0.15515892]), 'anti_vector': array([ 0.02702122, -0.98751991,  0.15515892]), 'angle': -0.1557883152147459, 'area': 0.114952898083981}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=-0.007387000000000005, dy=-0.04241700000000037, dz=0.26996600000000015, surface_area=0.31385190075534425, sa_to_vol=10.94590383829192, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=8.0, x=array([0.055451, 0.073181]), y=array([-3.429066, -3.465325]), z=array([1.581252, 1.802064]), radius=0.203862, length=0.22447, branch_order=1.0, branch_id=0.0, volume=0.029308, parent_id=7.0, reverse_branch_order=32.0, segment_id=0.0, projected_data={'XZ': {'polygon': <POLYGON ((0.258 1.563, 0.256 1.56, 0.251 1.557, 0.245 1.555, 0.238 1.552, 0...>, 'base_vector': array([ 0.07898588,  0.98370163, -0.16153124]), 'anti_vector': array([-0.07898588, -0.98370163,  0.16153124]), 'angle': -0.16224207795390888, 'area': 0.11139449535023886}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=0.017729999999999996, dy=-0.03625899999999982, dz=0.220812, surface_area=0.2875242342525162, sa_to_vol=9.810435179900239, slope=0.0, is_stem=False, is_divide=False)",
    "Cylinder(cyl_id=9.0, x=array([0.073181, 0.062266]), y=array([-3.465325, -3.478196]), z=array([1.802064, 2.056271]), radius=0.196833, length=0.254767, branch_order=1.0, branch_id=0.0, volume=0.031009, parent_id=8.0, reverse_branch_order=31.0, segment_id=1.0, projected_data={'XZ': {'polygon': <POLYGON ((0.268 1.809, 0.249 1.805, 0.223 1.802, 0.223 1.802, 0.2 1.8, 0.18...>, 'base_vector': array([-0.04284314,  0.99780365, -0.05052076]), 'anti_vector': array([ 0.04284314, -0.99780365,  0.05052076]), 'angle': -0.05054227542657572, 'area': 0.10626857437616959}}, flow_id=None, flow_type=None, begins_at_drip_point=None, begins_at_divide_point=None, dx=-0.010914999999999994, dy=-0.012871000000000077, dz=0.25420700000000007, surface_area=0.315080084456099, sa_to_vol=10.160923746528395, slope=0.0, is_stem=False, is_divide=False)",
]
ten_cyls_edges = [
    (0.0, -1.0),
    (0.0, 1.0),
    (1.0, 2.0),
    (2.0, 3.0),
    (3.0, 4.0),
    (4.0, 5.0),
    (5.0, 6.0),
    (6.0, 7.0),
    (7.0, 8.0),
    (8.0, 9.0),
]


ten_cyls_id_one = "[1.0]"
ten_cyls_bo_one = "[7.0, 8.0, 9.0]"
ten_cyls_bo_and_rad = "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]"

ten_cyls_is_stem = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
)

##ez_projection
ez_projection_xy_angle = 0.785398  # 45 degrees


# HappyPath
hp_edges = [
    (0.0, -1.0),
    (0.0, 1.0),
    (1.0, 2.0),
    (2.0, 3.0),
    (3.0, 4.0),
    (4.0, 5.0),
    (5.0, 6.0),
    (6.0, 7.0),
    (7.0, 8.0),
    (8.0, 9.0),
    (9.0, 10.0),
    (10.0, 11.0),
    (11.0, 12.0),
    (12.0, 13.0),
    (13.0, 14.0),
    (14.0, 15.0),
    (15.0, 16.0),
    (16.0, 17.0),
    (17.0, 18.0),
    (18.0, 19.0),
    (19.0, 20.0),
    (20.0, 21.0),
    (21.0, 22.0),
    (22.0, 23.0),
    (23.0, 24.0),
    (24.0, 25.0),
    (25.0, 26.0),
    (26.0, 27.0),
    (27.0, 28.0),
    (28.0, 29.0),
    (29.0, 30.0),
    (30.0, 31.0),
    (31.0, 32.0),
    (32.0, 33.0),
    (33.0, 34.0),
    (34.0, 35.0),
    (35.0, 36.0),
    (36.0, 37.0),
    (37.0, 38.0),
    (38.0, 39.0),
    (39.0, 40.0),
    (40.0, 41.0),
    (41.0, 42.0),
    (42.0, 43.0),
    (43.0, 44.0),
    (44.0, 45.0),
    (45.0, 46.0),
    (46.0, 47.0),
    (47.0, 48.0),
    (48.0, 49.0),
    (49.0, 50.0),
    (50.0, 51.0),
    (51.0, 52.0),
    (52.0, 53.0),
    (53.0, 54.0),
    (54.0, 55.0),
    (55.0, 56.0),
    (56.0, 57.0),
    (57.0, 58.0),
    (58.0, 59.0),
    (59.0, 60.0),
    (60.0, 61.0),
    (61.0, 62.0),
    (62.0, 63.0),
    (63.0, 64.0),
    (64.0, 65.0),
    (65.0, 66.0),
    (66.0, 67.0),
    (67.0, 68.0),
    (68.0, 69.0),
    (69.0, 70.0),
    (70.0, 71.0),
    (71.0, 72.0),
    (72.0, 73.0),
    (73.0, 74.0),
    (74.0, 75.0),
    (75.0, 76.0),
    (76.0, 77.0),
    (77.0, 78.0),
    (78.0, 79.0),
    (79.0, 80.0),
    (80.0, 81.0),
    (81.0, 82.0),
    (82.0, 83.0),
    (83.0, 84.0),
    (84.0, 85.0),
    (85.0, 86.0),
    (86.0, 87.0),
    (87.0, 88.0),
    (88.0, 89.0),
    (89.0, 90.0),
    (90.0, 91.0),
    (91.0, 92.0),
    (92.0, 93.0),
    (93.0, 94.0),
    (94.0, 95.0),
    (95.0, 96.0),
    (96.0, 97.0),
    (97.0, 98.0),
    (98.0, 99.0),
    (99.0, 100.0),
    (100.0, 101.0),
    (101.0, 102.0),
    (102.0, 103.0),
    (102.0, 148.0),
    (103.0, 104.0),
    (104.0, 105.0),
    (104.0, 138.0),
    (105.0, 106.0),
    (138.0, 139.0),
    (139.0, 140.0),
    (140.0, 141.0),
    (141.0, 142.0),
    (142.0, 143.0),
    (143.0, 144.0),
    (144.0, 145.0),
    (145.0, 146.0),
    (146.0, 147.0),
    (148.0, 149.0),
    (149.0, 150.0),
]

ten_cyls_rows_proj_XZ = []
ten_cyls_rows_proj_XY = []
ten_cyls_rows_proj_YZ = []

ten_cyls_flows = "[Flow(num_cylinders=10, projected_area=1.332563385222201, surface_area=3.3102009951007805, angle_sum=13.311017528987755, volume=0.327783, sa_to_vol=100.98563451833446, drip_node_id=0)]"

small_tree_dbh = 1.058276

small_tree_flows = "[Flow(num_cylinders=216, projected_area=16.517060215326925, surface_area=19.49507498855058, angle_sum=180.03288665020412, volume=3.9062959999999998, sa_to_vol=83646.4965224844, drip_node_id=0), Flow(num_cylinders=59, projected_area=0.01712513891199792, surface_area=0.0653136170203522, angle_sum=4.0063304619261375, volume=7.699999999999999e-05, sa_to_vol=52984.87647431056, drip_node_id=405.0), Flow(num_cylinders=32, projected_area=0.01033455063954463, surface_area=0.03666120817014779, angle_sum=3.2693589141152817, volume=4.8e-05, sa_to_vol=25387.06100800808, drip_node_id=222.0), Flow(num_cylinders=4, projected_area=0.001879242349756744, surface_area=0.006360028663486393, angle_sum=-1.4004883938106008, volume=7e-06, sa_to_vol=inf, drip_node_id=188.0), Flow(num_cylinders=8, projected_area=0.0024559778348642487, surface_area=0.008355741104642577, angle_sum=-2.5182426363497505, volume=9.999999999999999e-06, sa_to_vol=6887.50207002412, drip_node_id=147.0), Flow(num_cylinders=6, projected_area=0.0016837038216656593, surface_area=0.005825910788486325, angle_sum=-2.115709206226209, volume=5.999999999999999e-06, sa_to_vol=5825.910788486325, drip_node_id=163.0), Flow(num_cylinders=3, projected_area=0.0009449634116903826, surface_area=0.003272345739832201, angle_sum=0.3639153227121651, volume=4e-06, sa_to_vol=2617.2529857240233, drip_node_id=176.0), Flow(num_cylinders=5, projected_area=0.00142245008970565, surface_area=0.00503121351083425, angle_sum=-0.00046949725728318015, volume=7e-06, sa_to_vol=3582.900027621186, drip_node_id=179.0), Flow(num_cylinders=1, projected_area=0.000277103153591026, surface_area=0.0009704536786571552, angle_sum=-0.525305433679695, volume=1e-06, sa_to_vol=970.4536786571553, drip_node_id=226.0), Flow(num_cylinders=35, projected_area=0.01052004847925714, surface_area=0.0436400206306485, angle_sum=10.193206366817037, volume=5.299999999999999e-05, sa_to_vol=inf, drip_node_id=232.0), Flow(num_cylinders=3, projected_area=0.0007556341840308715, surface_area=0.0030501880153335982, angle_sum=-1.0835316994580007, volume=4e-06, sa_to_vol=2407.4260123907607, drip_node_id=274.0), Flow(num_cylinders=24, projected_area=0.00687016322759011, surface_area=0.02719439569967338, angle_sum=-0.467953573105651, volume=3.4e-05, sa_to_vol=20303.90126264672, drip_node_id=350.0), Flow(num_cylinders=5, projected_area=0.0015186890252737617, surface_area=0.005638373415030282, angle_sum=-2.4195862206414995, volume=7e-06, sa_to_vol=4248.493555173988, drip_node_id=309.0), Flow(num_cylinders=2, projected_area=0.0006559427591282863, surface_area=0.003129183362608114, angle_sum=-1.7050548651799198, volume=3e-06, sa_to_vol=2136.118070826746, drip_node_id=304.0), Flow(num_cylinders=5, projected_area=0.0012687423706050432, surface_area=0.006314459862046074, angle_sum=-4.00094773716074, volume=6.999999999999999e-06, sa_to_vol=inf, drip_node_id=321.0), Flow(num_cylinders=3, projected_area=0.0009350371357500096, surface_area=0.0036045534549860535, angle_sum=0.5863978722482486, volume=4e-06, sa_to_vol=2774.929521007695, drip_node_id=315.0), Flow(num_cylinders=3, projected_area=0.0008613860036361682, surface_area=0.0030539265105913706, angle_sum=-1.3293928778054518, volume=4e-06, sa_to_vol=2395.079553262153, drip_node_id=325.0), Flow(num_cylinders=103, projected_area=0.035842410317746466, surface_area=0.1308078996954519, angle_sum=0.9595299834971135, volume=0.000184, sa_to_vol=81927.57367017229, drip_node_id=513.0)]"
