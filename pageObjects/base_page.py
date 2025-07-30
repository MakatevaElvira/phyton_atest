class BasePage:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def type(self, web_element, text):
        web_element.click()
        web_element.clear()
        web_element.send_keys(text)