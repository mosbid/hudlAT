from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """ Performs click to locator find element """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException:
            assert False, "Locator is missing"
        except:
            assert False, "Couldn't perform click"

    def send_keys(self, by_locator, text):
        """ Send keys to locator with text """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException:
            assert False, "Locator is missing"
        except:
            assert False, "Couldn't perform send_keys"

    def element_displayed(self, by_locator):
        """ Check if locator is present on page """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            assert False, "Locator is missing"

    def url_changed(self, expected_url):
        """ Check url has changed """
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        except TimeoutException:
            assert False, "Missing expected URL"