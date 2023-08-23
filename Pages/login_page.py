from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class LoginPage(BasePage):
    input_username = (By.ID, "loginusername")
    input_password = (By.ID, "loginpassword")
    button_login = (By.XPATH, "//button[@onclick='logIn()']")

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
        located_by, located_value = self.button_login
        self.driver.find_element(located_by, located_value).click()

    def wait_for_alert(self):
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        return self.alert.text

    def find_close(self):
        pass
