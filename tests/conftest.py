import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

# # content of test_sample.py
# def test_answer(cmdopt):
#     if cmdopt == "type1":
#         print("first")
#     elif cmdopt == "type2":
#         print("second")
#     assert 0  # to see what was printed



def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


# # content of test_module.py
# import pytest
#
#
# def test_func_fast():
#     pass
#
#
# @pytest.mark.slow
# def test_func_slow():
#     pass


