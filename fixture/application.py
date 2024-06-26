import pytest
from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class Application:

    def __init__(self):
        self.wd = WebDriver()
        options = Options()
        options.page_load_strategy = 'normal'

        #options.add_argument("−−incognito")
        #options.accept_insecure_certs = True
        #options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #options.add_argument("−−disable - extensions")#появляются левые вкладки
        #options.add_argument("−−disable-popup-blocking")


        self.wd = WebDriver(options=options)
        self.wd.set_window_size(1980, 1080)
        self.wd.implicitly_wait(1)

    def open_login_page(self):
        wd = self.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

    def login(self, user):
        wd = self.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        wd.find_element(By.ID, "username").clear()
        wd.find_element(By.ID, "username").send_keys(user.username)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(user.password)
        wd.find_element(By.ID, "login-button").click()

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

    def desrtoy(self):
        self.wd.quit()


