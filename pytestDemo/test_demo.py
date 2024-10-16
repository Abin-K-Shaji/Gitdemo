import pytest

import pytest
def test_data():
    print("hello")

@pytest.mark.smoke
def test_Createdata():
    a=10
    b=30
    print(a+b)
@pytest.fixture()
def setup():
    print("hii")

def test_fixture():
    print("demo")