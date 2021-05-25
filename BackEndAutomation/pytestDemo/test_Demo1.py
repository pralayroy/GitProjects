# Any pytest file should start with test_ or end with _test
# pytest method should start with test
# Any code should wrapped inside method
# Every method in pytest treated as a test case
import pytest


def test_firstProgram(setup):
    print("Hello pytest")


@pytest.mark.smoke
def test_GreetCreditCard():
    print("Good Morning")


# Parameterization test with multiple data set
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

