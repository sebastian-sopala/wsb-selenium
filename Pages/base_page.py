from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is a parent class to all pages"""
"""it contains generic methods and utilities"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on(self, *selector):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector)).click()

    def wait_for_visible(self, *selector):
        sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))

    def wait_for_not_visible(self, *selector):
        sleep(1)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(selector))

    def input_text(self, *selector, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector)).send_keys(text)
