import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute at the end")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Pralay", "Roy", "www.xyz.com"]


# Parameterization test with multiple data set
# Now if you want to send chorme browser with multiple other information like user name password then you need to
# wrape parameter like @pytest.fixture(params=[("chrome", "Pralay"), "Firefox", "IE"]). Like this you can send multiple
# values in single run
@pytest.fixture(params=[("chrome","Pralay"), ("Firefox", "Roy"), "IE"])
def crossBrowser(request):
    return request.param

