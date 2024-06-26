import pytest

from fixture.application import Application
from model.user import User

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.desrtoy)
    return fixture
def test_first_demo_auth(app):
        app.login(User("demo", "demo"))