import pytest


@pytest.fixture()
def setup():
    print("i am happy")
    yield
    print("i'm sorry")
