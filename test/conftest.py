from __future__ import annotations

import os
import sys

import pytest
from _pytest.nodes import Item

cwd = os.getcwd()
sys.path.append(cwd + "/src/")

from canopyhydro.configuration import test_input_dir
from canopyhydro.Cylinder import create_cyl
from canopyhydro.Forester import Forester


def pytest_collection_modifyitems(items: list[Item]):
    for item in items:
        if "spark" in item.nodeid:
            item.add_marker(pytest.mark.spark)
        elif "_int_" in item.nodeid:
            item.add_marker(pytest.mark.integration)


# @lru_cache(maxsize=256)
@pytest.fixture
def basic_forest():
    forest = Forester(test_input_dir)
    forest.get_file_names()
    # forest.qsm_to_collection()
    return forest


@pytest.fixture
def test_cyl(request):
    """
    Tests projection of cylinders parallel with:
     the XY plane, Z axis the line x=y (45 deg)
    """
    created = create_cyl(request.param)
    return created


@pytest.fixture
def basic_collection(basic_forest, request):
    basic_forest.qsm_to_collection(file_name=request.param)
    flexible_collection = basic_forest.cylinder_collections[0]
    return flexible_collection


@pytest.fixture
def flexible_collection(basic_forest, request):
    basic_forest.qsm_to_collection(file_name=request.param)
    flexible_collection = basic_forest.cylinder_collections[0]
    flexible_collection.project_cylinders("XZ")
    flexible_collection.project_cylinders("XY")
    flexible_collection.project_cylinders("YZ")
    flexible_collection.initialize_digraph_from()
    return flexible_collection


@pytest.fixture
def ez_projection():
    forest = Forester(test_input_dir)
    forest.get_file_names()
    forest.qsm_to_collection(file_name="2_EZ_projection.csv")
    collection = forest.cylinder_collections[0]
    return collection


@pytest.fixture
def happy_path_projection():
    forest = Forester(test_input_dir)
    forest.get_file_names()
    forest.qsm_to_collection(file_name="3_HappyPathWTrunk.csv")
    collection = forest.cylinder_collections[0]
    return collection


@pytest.fixture
def small_tree():
    forest = Forester(test_input_dir)
    forest.get_file_names()
    forest.qsm_to_collection(file_name="5_SmallTree.csv")
    collection = forest.cylinder_collections[0]
    return collection


@pytest.fixture
def large_collection():
    forest = Forester(test_input_dir)
    forest.get_file_names()
    forest.qsm_to_collection(file_name="4_LargeCollection.csv")
    collection = forest.cylinder_collections[0]
    # collection.project_cylinders("XZ")
    return collection
