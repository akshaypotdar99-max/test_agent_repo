from selenium.webdriver.common.by import By
from BaseSeleniumFramework.Helpers.DriverHelper import BasePage


class ResetPasswordPage(BasePage):
    username = (By.NAME,"username")
    reset_button = (By.CSS_SELECTOR,".orangehrm-forgot-password-button--reset")
    cancel_button = (By.CSS_SELECTOR, ".orangehrm-forgot-password-button--cancel")
    success_password_reset_lnk_dialog_title = (By.CSS_SELECTOR,".orangehrm-forgot-password-title")