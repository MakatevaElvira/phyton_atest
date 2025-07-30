
from selenium.webdriver.common.by import By


from utils.decorators import named
from pageObjects.base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, app):
        super().__init__(app)  # инициализируем BasePage

    @property
    @named("Поле ввода логина")
    def username_field( self):
        wd = self.app.wd
        return wd.find_element(By.NAME, "password")

    @property
    @named("Поле ввода пароля")
    def password_field(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "username")

    @property
    @named("Кнопка подтверждения логина")
    def login_button(self):
        wd = self.app.wd
        return wd.find_element(By.ID, "login-button")

    @property
    @named("Сообщение об отправке СМС")
    def sms_sent_title(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div[ contains(text(),'Отправили СМС код на ваш номер телефона')]")

    def open(self):
        wd = self.app.wd
        wd.get(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        #return self

    def submit_login(self):
        self.login_button.click()

    def login_as(self, user):
        self.open()
        self.type(self.username_field, user.username)
        self.type(self.password_field, user.password)

