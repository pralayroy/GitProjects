# Any pytest file should start with test_ or end with _test
# pytest method should start with test
# Any code should wrapped inside method
# Every method in pytest treated as a test case
# Method name should have some meaningful name
# -k stands for method names execution, -v means Verbose, -s means logs in out put
# you can run specific file using py.test <file name>
# you can mark (tag) tests using @pytest.mark.smoke and then run with -m Ex: pytest -m smoke -v -s
# You can skip the test using @pytest.mark.skip
# You can skip the failure from output by mentioning @pytest.mark.xfail
# Fixture are used as setup and tear down methods for test cases - conftest file need to create for generalization
# Mark as fixture and make it available for all test cases (fixture name into parameters of method)
# Datadriven and parameterization can be done with return statement in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end


import pytest


#@pytest.mark.skip
@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test is failed because strings do not match"


@pytest.mark.smoke
def test_SecondCreditCard():
    a = 2
    b = 5
    assert a + b == 7, "Addition matched"
