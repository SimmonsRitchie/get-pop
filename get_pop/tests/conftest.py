import pytest


@pytest.fixture(scope="module")
def states():
    return ["ny", "tn", "tx", "pa"]
