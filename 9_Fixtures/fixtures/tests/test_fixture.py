import pytest


class TestExample2:

    @pytest.fixture()
    def fixture1(self):
        print("I am the setup 1")
        yield
        print("I am the teardown 1")

    @pytest.fixture()
    def fixture2(self):
        print("I am the setup 2")
        yield
        print("I am the teardown 2")

    def test_method1(self, fixture1):
        print("I am the test method 1")
        assert 1 + 1 == 2

    def test_method2(self, fixture1):
        print("I am the test method 2")
        assert 1 + 1 == 2

    def test_method3(self, fixture2):
        print("I am the test method 3")
        assert 1 + 1 == 2

    def test_method4(self):
        print("I am the test method 4")
        assert 1 + 1 == 2
