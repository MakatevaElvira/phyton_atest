# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from user import User


def login(wd, user):
    wd.find_element(By.ID, "username").clear()
    wd.find_element(By.ID, "username").send_keys(user.username)
    wd.find_element(By.NAME, "password").clear()
    wd.find_element(By.NAME, "password").send_keys(user.password)
    wd.find_element(By.ID, "login-button").click()


class test_first_demo_auth(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'

        options.add_argument("−−incognito")
        options.accept_insecure_certs = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("−−disable - extensions")#появляются левые вкладки
        options.add_argument("−−disable-popup-blocking")


        self.wd = webdriver.Chrome(options=options)
        self.wd.set_window_size(1980, 1080)
        self.wd.implicitly_wait(1)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_first_demo_auth(self):
        wd = self.wd
        self.open_login_page(wd)
        login(wd, User("demo", "demo"))

    def test_incorrect_demo_auth(self):
        wd = self.wd
        self.open_login_page(wd)
        login(wd, User("1234", "1234"))

    def open_login_page(self, wd):
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
