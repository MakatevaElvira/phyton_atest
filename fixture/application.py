from asyncio import timeout

from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.locators import Locators
from fixture.session import Session
from fixture.ibank import Ibank
from pageObjects.authPage import AuthPage



class Application:

    def is_valid(self):
         try:
             self.wd.current_url
             return True
         except:
             return False
    def __init__(self):
        options = Options()
        options.page_load_strategy = 'normal'

        self.wd = WebDriver(options=options)
        self.session = Session(self)
        self.ibank = Ibank(self)
        self.authPage = AuthPage(self)
        self.locators = Locators(self)


        self.wd_wait = WebDriverWait
        self.wd.set_window_size(1980, 1080)
        self.wd.implicitly_wait(0.1)
        self.timeout = 0.001


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

    def is_element_clickable(self, WebElement):
        try:
            self.wd_wait(self.wd, self.timeout).until(EC.element_to_be_clickable(WebElement))
            return True
        except TimeoutException:
            return False

    def destroy(self):
        self.wd.quit()


