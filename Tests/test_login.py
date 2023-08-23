import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from time import sleep


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()

    def test_close_form_with_close_button(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_log_in()

        login_page.wait_for_modal_to_appear()
        self.assertTrue(login_page.modal_is_displayed())

        login_page.click_close_button()

        login_page.wait_for_modal_to_disappear()
        self.assertFalse(login_page.modal_is_displayed())

    def test_close_form_with_X_button(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_log_in()

        login_page.wait_for_modal_to_appear()
        self.assertTrue(login_page.modal_is_displayed())

        login_page.click_x_icon()

        login_page.wait_for_modal_to_disappear()
        self.assertFalse(login_page.modal_is_displayed())

    def test_successfully_log_in(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_log_in()
        sleep(1)

        username_text = "uzytkowniktestowy123321"
        login_page.find_username(username_text, login_page.input_username)
        sleep(1)

        password_text = "testowy123321"
        login_page.find_password(password_text, login_page.input_password)
        sleep(1)

        login_page.find_login()
        wait_username = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        self.assertEqual("Welcome " + username_text, wait_username.text)

    def test_invalid_username(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_log_in()
        sleep(1)

        username_text = "uzytkowniktestowy123"
        login_page.find_username(username_text, login_page.input_username)
        sleep(1)

        password_text = "testowy123"
        login_page.find_password(password_text, login_page.input_password)
        sleep(1)

        login_page.find_login()
        sleep(3)
        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "User does not exist.")
        alert.accept()

    def test_invalid_password(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_log_in()
        sleep(1)

        username_text = "uzytkowniktestowy123321"
        login_page.find_username(username_text, login_page.input_username)
        sleep(1)

        password_text = "testowy123"
        login_page.find_password(password_text, login_page.input_password)
        sleep(1)

        login_page.find_login()
        sleep(3)
        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "Wrong password.")
        alert.accept()

if __name__ == "__main__":
    unittest.main(verbosity=2)
