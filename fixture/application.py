import pytest
from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from fixture.session import Session
from fixture.ibank import Ibank


class Application:

    def is_valid(self):
         try:
             self.wd.current_url
             return True
         except:
             return False
    def __init__(self):
        self.wd = WebDriver()
        self.session = Session(self)
        self.ibank = Ibank(self)

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


