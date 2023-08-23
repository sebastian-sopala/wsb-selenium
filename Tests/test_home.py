import unittest
from time import sleep

from Pages.home_page import HomePage
from Pages.cart_page import CartPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com")

    def tearDown(self):
        self.driver.close()

    def test_home_link(self):
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)

        # there is a bug on the site when open "https://www.demoblaze.com/cart.html" directly
        home_page.open_cart()

        home_page.wait_for_cart_page_to_open()
        self.assertTrue(home_page.place_order_btn)

        cart_page.click_home_link()

        cart_page.wait_for_home_page_to_open()
        self.assertTrue(cart_page.image_carousel)


if __name__ == "__main__":
    unittest.main(verbosity=2)
