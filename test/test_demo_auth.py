# -*- coding: utf-8 -*-
from model.user import User

#@pytest.mark.parametrize()
def test_first_demo_auth(app):
    app.session.login(User("demo", "demo"))


def test_incorrect_demo_auth(app):
    app.session.login(User("1234", "1234"))
