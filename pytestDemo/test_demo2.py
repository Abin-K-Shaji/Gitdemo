import pytest

from pytestDemo.test_demo import setup

import pytest
@pytest.mark.usefixtures("setup")
class Testeg:

    def test_demo2(self):
        print("i am abin")
    def test_demo3(self):
        print("i am abin2")
    def test_demo4(self):
        print("i am cabin3")
    def test_demo5(self):
        print("i am cabin4")