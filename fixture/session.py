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