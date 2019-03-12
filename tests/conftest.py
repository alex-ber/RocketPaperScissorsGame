import pytest

iswebfound = False
try:
    from web import application
    iswebfound = True
except ImportError:
    pass

# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )
#
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")
#
# # content of test_sample.py
# def test_answer(cmdopt):
#     if cmdopt == "type1":
#         print("first")
#     elif cmdopt == "type2":
#         print("second")
#     assert 0  # to see what was printed


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def skip_tests(**kwargs):
    items = kwargs.get('items', None)
    if items is None:
        TypeError("items can't be None")

    reason=kwargs.get('reason', None)
    if reason is None:
        TypeError("reason can't be None")

    keyword = kwargs.get('keyword', None)
    if keyword is None:
        TypeError("keyword can't be None")

    skip = pytest.mark.skip(reason=reason)
    for item in items:
        if keyword in item.keywords:
            item.add_marker(skip)




def pytest_collection_modifyitems(config, items):
    if not config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        skip_tests(config=config, items=items, keyword="slow", reason="need --runslow option to run")

    if not iswebfound:
        # --runslow given in cli: do not skip slow tests
        skip_tests(config=config, items=items, keyword="ws", reason="need --runws option to run")


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


