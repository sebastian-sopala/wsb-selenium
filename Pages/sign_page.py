from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class SignPage(BasePage):
    input_username = (By.ID, "sign-username")
    input_password = (By.ID, "sign-password")
    button_register = (By.XPATH, "//button[@onclick='register()']")
    sign_close_btn = (By.XPATH, '//div[@id="signInModal"]//button[text()="Close"]')
    sign_modal = (By.XPATH, '//*[text()="Sign up"]')
    sign_x_btn = (By.XPATH, '//div[@id="signInModal"]//div[@class="modal-header"]/button/span[text()="×"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.alert = None

    def find_username(self, username, input_username):
        located_by, located_value = input_username
        input_username = self.driver.find_element(located_by, located_value)
        input_username.send_keys(username)

    def find_password(self, password, input_password):
        located_by, located_value = input_password
        input_password = self.driver.find_element(located_by, located_value)
        input_password.send_keys(password)

    def find_login(self):
        located_by, located_value = self.button_register
        self.driver.find_element(located_by, located_value).click()

    def click_close_button(self):
        self.click_on(*self.sign_close_btn)

    def click_x_icon(self):
        self.click_on(*self.sign_x_btn)

    def wait_for_modal_to_appear(self):
        self.wait_for_visible(*self.sign_modal)

    def wait_for_modal_to_disappear(self):
        self.wait_for_not_visible(*self.sign_modal)

    def modal_is_displayed(self):
        return self.driver.find_element(*self.sign_modal).is_displayed()
