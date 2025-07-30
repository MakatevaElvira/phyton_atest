# -*- coding: utf-8 -*-
import pytest

from assertpy import assert_that
from model.user import User

@pytest.mark.parametrize("username, password", [
    ("demo", "demo"),
    ("test_user", "12345"),
    ("admin", "admin"),
])
def test_first_demo_auth(app,username, password):
    user = User(username, password)
    app.session.loginAs(user)
    assert app.session.check_sent_sms_title().is_displayed()

@pytest.mark.parametrize("username, password", [
    ("demo", "demo"),
    ("test_user", "12345"),
    ("admin", "admin"),
])
def test_correct_demo_auth(app,username, password):
    user = User(username, password)
    app.authPage.login_as(user)
    app.authPage.submit_login()
    assert  app.session.check_sent_sms_title().is_displayed(), \
    "Ожидалось, что окно подтверждения логина отобразится, а оно не отображается"

@pytest.mark.parametrize("username, password", [
    ("demo", ""),
    ("", "12345"),
    ("", ""),
])
def test_incorrect_demo_auth(app,username, password):
    user = User(username, password)
    app.authPage.login_as(user)
    assert_that(app.is_element_clickable(app.authPage.login_button)).is_false()