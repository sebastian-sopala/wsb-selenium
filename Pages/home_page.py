from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class HomePage(BasePage):

    home_link = (By.XPATH, '//a[text()="Home "]')
    about_us_link = (By.XPATH, '//a[text()="About us"]')
    contact_link = (By.XPATH, '//a[text()="Contact"]')
    cart_link = (By.XPATH, '//a[text()="Cart"]')
    place_order_btn = (By.XPATH, '//button[text()="Place Order"]')

    def open_contact(self):
        self.click_on(*self.contact_link)

    def open_about_us(self):
        self.click_on(*self.about_us_link)

    def open_cart(self):
        self.click_on(*self.cart_link)

    def wait_for_cart_page_to_open(self):
        self.wait_for_visible(*self.place_order_btn)



