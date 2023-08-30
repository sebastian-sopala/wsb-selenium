import unittest
from time import sleep

from Pages.home_page import HomePage
from Pages.cart_page import CartPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(unittest.TestCase):

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

    def test_home_pictures(self):
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)

        home_page.open_cart()

        home_page.wait_for_cart_page_to_open()
        self.assertTrue(home_page.place_order_btn)

        cart_page.click_home_image()

        cart_page.wait_for_home_page_to_open()
        self.assertTrue(cart_page.image_carousel)

    def test_move_images(self):
        home_page = HomePage(self.driver)

        home_page.move_image_first()

        wait_next_images = (WebDriverWait(self.driver, 6).
                            until(EC.visibility_of_element_located((By.XPATH, '//img[@src="nexus1.jpg"]'))))

        if wait_next_images:
            home_page.move_image_second()

        self.assertTrue(home_page.move_image_second())

    def test_move_next_icon(self):
        home_page = HomePage(self.driver)

        home_page.move_image_first()
        home_page.find_next_icon()

        self.assertTrue(home_page.move_image_second())

    def test_move_previous_icon(self):
        home_page = HomePage(self.driver)

        home_page.move_image_first()
        home_page.find_previous_icon()

        self.assertTrue(home_page.move_image_third())

    def test_choose_categories_phones(self):
        home_page = HomePage(self.driver)

        sleep(5)
        home_page.click_categories_phones()
        sleep(5)
        items = self.driver.find_elements(By.CSS_SELECTOR, '.col-lg-9 .item')
        phone_names = ['Samsung', 'Nexus', 'Nokia', 'iPhone', 'Sony', 'HTC']
        are_all_phone_names_present = all(any(phone_name.lower() in item.text.lower() for phone_name in phone_names)
                                          for item in items)
        self.assertTrue(are_all_phone_names_present,
                        "Not all displayed items after clicking 'Phones' contain expected phone names.")

    def test_choose_categories_laptops(self):
        home_page = HomePage(self.driver)

        sleep(5)
        home_page.click_categories_laptops()
        sleep(5)
        items = self.driver.find_elements(By.CSS_SELECTOR, '.col-lg-9 .item')
        laptops_names = ['Sony', 'MacBook', 'Dell']
        are_all_laptops_names_present = all(
            any(laptop_name.lower() in item.text.lower() for laptop_name in laptops_names) for item in items)
        self.assertTrue(are_all_laptops_names_present,
                        "Not all displayed items after clicking 'Laptops' contain expected phone names.")

    def test_choose_categories_monitors(self):
        home_page = HomePage(self.driver)

        sleep(5)
        home_page.click_categories_monitors()
        sleep(5)
        items = self.driver.find_elements(By.CSS_SELECTOR, '.col-lg-9 .item')
        monitors_names = ['Apple', 'Asus']
        are_all_monitors_names_present = all(
            any(monitor_name.lower() in item.text.lower() for monitor_name in monitors_names) for item in items)
        self.assertTrue(are_all_monitors_names_present,
                        "Not all displayed items after clicking 'Monitors' contain expected phone names.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
