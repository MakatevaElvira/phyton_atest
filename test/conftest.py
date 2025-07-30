import pytest
from fixture.application import Application

fixture = None
@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()

    def fin():
        fixture.destroy()
    request.addfinalizer(fin)

    return fixture

