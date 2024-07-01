from selenium.webdriver.common.by import By

class Ibank:
    def __init__(self, app):
        self.app = app

    def open_ibank_page(self):
        wd = self.app.wd
        wd.get(
            "https://www.bspb.ru/retail/ibank")

    def select_first_region(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//option[contains(text(),'Вне региона')]/..").click()
        wd.find_element(By.XPATH, "//option[contains(text(),'Вне региона')]/../option").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if field_name is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)