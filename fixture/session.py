from selenium.webdriver.common.by import By


class Session:

    def __init__(self, app):
        self.app = app
    def open_login_page(self):
        wd = self.app.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

    def login(self, user):
        wd = self.app.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        wd.find_element(By.ID, "username").clear()
        wd.find_element(By.ID, "username").send_keys(user.username)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(user.password)
        wd.find_element(By.ID, "login-button").click()
        wd.find_element(By.XPATH, "//div[ contains(text(),'Отправили СМС код на ваш номер телефона')]")


    def reset_password(self):
        wd = self.app.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        wd.find_element(By.XPATH, "//div[@id='additional-actions']").click() #это кнопка восстановить доступ
        wd.find_element(By.XPATH, "//div[@class='modal-dialog']")#это модальное информ окно о средствах смены пароля

    def switch_to_ibank_page(self):
        wd = self.app.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        window_before = wd.window_handles[0]
        wd.find_element(By.LINK_TEXT, "Об Интернет-банке").click()
        window_after = wd.window_handles[1]
        wd.switch_to.window(window_after)
