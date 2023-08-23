import unittest
from selenium import webdriver
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

if __name__ == "__main__":
    unittest.main(verbosity=2)
