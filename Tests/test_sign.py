import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from Pages.home_page import HomePage
from Pages.sign_page import SignPage
from time import sleep
from datetime import datetime


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()

    def test_close_form_with_close_button(self):
        sign_page = SignPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_sign_up()

        sign_page.wait_for_modal_to_appear()
        self.assertTrue(sign_page.modal_is_displayed())

        sign_page.click_close_button()

        sign_page.wait_for_modal_to_disappear()
        self.assertFalse(sign_page.modal_is_displayed())

    def test_close_form_with_X_button(self):
        sign_page = SignPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_sign_up()

        sign_page.wait_for_modal_to_appear()
        self.assertTrue(sign_page.modal_is_displayed())

        sign_page.click_x_icon()

        sign_page.wait_for_modal_to_disappear()
        self.assertFalse(sign_page.modal_is_displayed())

    def test_successfully_sign_up(self):
        sign_page = SignPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_sign_up()
        sleep(1)

        username_text = "uzytkowniktestowy" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        sign_page.find_username(username_text, sign_page.input_username)
        sleep(1)

        password_text = "testowy123321"
        sign_page.find_password(password_text, sign_page.input_password)
        sleep(1)

        sign_page.find_login()
        sleep(3)
        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "Sign up successful.")
        alert.accept()

    def test_invalid_username(self):
        sign_page = SignPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_sign_up()
        sleep(1)

        username_text = ""
        sign_page.find_username(username_text, sign_page.input_username)
        sleep(1)

        password_text = "testowy123"
        sign_page.find_password(password_text, sign_page.input_password)
        sleep(1)

        sign_page.find_login()
        sleep(3)
        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()

    def test_invalid_password(self):
        sign_page = SignPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_sign_up()
        sleep(1)

        username_text = "uzytkowniktestowy123321"
        sign_page.find_username(username_text, sign_page.input_username)
        sleep(1)

        password_text = ""
        sign_page.find_password(password_text, sign_page.input_password)
        sleep(1)

        sign_page.find_login()
        sleep(3)
        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()

    def test_exist_username(self):
        sign_page = SignPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_sign_up()
        sleep(1)

        username_text = "uzytkowniktestowy123321"
        sign_page.find_username(username_text, sign_page.input_username)
        sleep(1)

        password_text = "testowy123"
        sign_page.find_password(password_text, sign_page.input_password)
        sleep(1)

        sign_page.find_login()
        sleep(3)
        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "This user already exist.")
        alert.accept()


if __name__ == "__main__":
    unittest.main(verbosity=2)
