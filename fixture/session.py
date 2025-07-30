from selenium.webdriver.common.by import By


class Session:

    def __init__(self, app):
        self.app = app
    def open_login_page(self):
        wd = self.app.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

    def type(self,locator_type, locator_name, text ):
        wd = self.app.wd
        wd.find_element(locator_type, locator_name).click()
        wd.find_element(locator_type, locator_name).clear()
        wd.find_element(locator_type, locator_name).send_keys(text)

    def type_user_name(self, user):
        locators = self.app.locators
        self.type(By.ID, locators.USER_NAME, user.username)


    def type_password(self, user):
        locators = self.app.locators
        self.type(By.NAME, locators.PASSWORD,user.password)


    def submit_login(self):
        wd = self.app.wd
        locators = self.app.locators
        wd.find_element(By.ID, locators.SUBMIT_LOGIN).click()

    def check_sent_sms_title(self):
        wd = self.app.wd
        locators = self.app.locators
        return wd.find_element(By.XPATH, locators.SMS_SENT)

    def loginAs(self, user):
        self.open_login_page()
        self.type_user_name(user)
        self.type_password(user)
        self.submit_login()


    def reset_password(self):
        wd = self.app.wd
        locators = self.app.locators
        self.open_login_page()
        wd.find_element(By.XPATH, locators.RESET_PASSWORD).click() #это кнопка восстановить доступ
        wd.find_element(By.XPATH, locators.RESET_PASSWORD_INFO_WINDOW) #это модальное информ окно о средствах смены пароля

    def switch_to_ibank_page(self):
        wd = self.app.wd
        self.open_login_page()
        locators = self.app.locators
        window_before = wd.window_handles[0]
        wd.find_element(By.LINK_TEXT, locators.INTERNET_BANK).click()
        window_after = wd.window_handles[1]
        wd.switch_to.window(window_after)
