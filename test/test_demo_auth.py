# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.user import User
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.desrtoy)
    return fixture

#@pytest.mark.parametrize()
def test_first_demo_auth(app):
    app.login(User("demo", "demo"))


def test_incorrect_demo_auth(app):
    app.login(User("1234", "1234"))
