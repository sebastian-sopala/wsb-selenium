from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class HomePage(BasePage):
    home_link = (By.XPATH, '//a[text()="Home "]')
    about_us_link = (By.XPATH, '//a[text()="About us"]')
    contact_link = (By.XPATH, '//a[text()="Contact"]')
    cart_link = (By.XPATH, '//a[text()="Cart"]')
    login_link = (By.ID, "login2")
    signup_link = (By.ID, "signin2")
    logout_link = (By.ID, "logout2")

    def open_contact(self):
        located_by, locator_value = self.contact_link
        self.driver.find_element(located_by, locator_value).click()

    def open_about_us(self):
        located_by, locator_value = self.about_us_link
        self.driver.find_element(located_by, locator_value).click()

    def open_cart(self):
        located_by, locator_value = self.cart_link
        self.driver.find_element(located_by, locator_value).click()

    def open_log_in(self):
        located_by, locator_value = self.login_link
        self.driver.find_element(located_by, locator_value).click()

    def open_sign_up(self):
        located_by, locator_value = self.signup_link
        self.driver.find_element(located_by, locator_value).click()

    def open_log_out(self):
        located_by, locator_value = self.logout_link
        self.driver.find_element(located_by, locator_value).click()
