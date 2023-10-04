import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="Run slow tests",
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-slow"):
        skipper = pytest.mark.skip(reason="run all tests except slow tests")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skipper)

    elif config.getoption("--run-slow"):
        skipper = pytest.mark.skip(reason="Only run slow tests")
        for item in items:
            if "slow" not in item.keywords:
                item.add_marker(skipper)
