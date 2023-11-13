from __future__ import annotations


def hello_test():
    print("Hello")


def test_int_hello():
    """
    This test is marked implicitly as an integration test because the name contains "_init_"
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
    ret = hello_test()
    assert ret == "Hello"
