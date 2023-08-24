from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CartPage(BasePage):

    home_link = (By.XPATH, '//a[text()="Home "]')
    home_image = (By.XPATH, '//a[text()=" PRODUCT STORE"]')
    # categories = (By.XPATH, '//*[@id="cat"]')
    image_carousel = (By.XPATH, '//*[@id="contcar"]')

    def click_home_link(self):
        self.click_on(*self.home_link)

    def click_home_image(self):
        self.click_on(*self.home_image)

    def wait_for_home_page_to_open(self):
        self.wait_for_visible(*self.image_carousel)
