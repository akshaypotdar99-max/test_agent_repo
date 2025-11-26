import pytest
from BaseSeleniumFramework.Driver import Driver
from BaseSeleniumFramework.Utils import config
from OrangeHRMPOM.Application.Login.LoginPage import LoginPage


@pytest.fixture
def driver():
    driver = Driver().get_driver()
    login = LoginPage(driver)
    login.goto()
    login.fill_credentials(config.USERNAME, config.PASSWORD)
    login.click_login()
    yield driver
    Driver().quit_driver()