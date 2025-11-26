from selenium.webdriver.common.by import By
from BaseSeleniumFramework.Helpers.DriverHelper import BasePage
from BaseSeleniumFramework.Utils import config


class LoginPage(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.CSS_SELECTOR, ".orangehrm-login-button")
    error_msg = (By.CSS_SELECTOR, ".oxd-alert-content--error")
    forgot_password_lnk = (By.CSS_SELECTOR, ".orangehrm-login-forgot-header")

    def goto(self):
        self.open(config.BASE_URL)

    def fill_credentials(self, username, password):
        self.type(self.username, username)
        self.type(self.password, password)

    def click_login(self):
        self.click(self.login_btn)

    def get_error_message(self):
        msg = ""
        try:
            msg = self.get_text(self.error_msg)
        except Exception as e:
            pass
        return msg

    def click_forgot_password(self):
        self.click(self.forgot_password_lnk)
