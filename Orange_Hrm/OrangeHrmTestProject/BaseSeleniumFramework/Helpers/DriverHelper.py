from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def wait_for_element_presence(self,by):
        self.wait.until(EC.presence_of_element_located(by))

    def wait_for_element_visible(self,by):
        self.wait.until(EC.visibility_of_element_located(by))

    def wait_and_click(self,by):
        self.wait.until(EC.presence_of_element_located(by))
        self.driver.find_element(*by).click()

    def wait_and_sendkeys(self,by,message):
        self.wait.until(EC.presence_of_element_located(by))
        self.driver.find_element(*by).send_keys(message)