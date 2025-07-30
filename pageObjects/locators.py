


class Locators:
    def __init__(self, app):
        self.app = app

    USER_NAME = ("username")
    PASSWORD = ("password")
    SUBMIT_LOGIN = ("login-button")
    SMS_SENT = ("//div[ contains(text(),'Отправили СМС код на ваш номер телефона')]")
    RESET_PASSWORD = ("//div[@id='additional-actions']")
    RESET_PASSWORD_INFO_WINDOW= ("//div[@class='modal-dialog']")
    INTERNET_BANK = ("Об Интернет-банке")