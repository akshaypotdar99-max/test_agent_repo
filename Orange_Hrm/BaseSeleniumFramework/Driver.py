from selenium import webdriver

from BaseSeleniumFramework.Helpers.DriverFactory import DriverFactory
from BaseSeleniumFramework.Utils import config


class Driver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = DriverFactory.create_driver(config.BROWSER)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None