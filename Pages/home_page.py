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
    place_order_btn = (By.XPATH, '//button[text()="Place Order"]')
    first_image = (By.XPATH, '//div[@class="carousel-item"]//img[@src="Samsung1.jpg"]')
    second_image = (By.XPATH,  '//div[@class="carousel-item"]//img[@src="nexus1.jpg"]')
    third_image = (By.XPATH,  '//div[@class="carousel-item"]//img[@src="iphone1.jpg"]')

    def open_contact(self):
        self.click_on(*self.contact_link)

    def open_about_us(self):
        self.click_on(*self.about_us_link)

    def open_cart(self):
        self.click_on(*self.cart_link)

    def open_home(self):
        self.click_on(*self.home_link)

    def wait_for_cart_page_to_open(self):
        self.wait_for_visible(*self.place_order_btn)

    def open_log_in(self):
        located_by, locator_value = self.login_link
        self.driver.find_element(located_by, locator_value).click()

    def open_sign_up(self):
        located_by, locator_value = self.signup_link
        self.driver.find_element(located_by, locator_value).click()

    def open_log_out(self):
        located_by, locator_value = self.logout_link
        self.driver.find_element(located_by, locator_value).click()

    def move_image_first(self):
        self.wait_for_visible(*self.first_image)

    def move_image_second(self):
        self.wait_for_visible(*self.second_image)

    def move_image_third(self):
        self.wait_for_visible(*self.third_image)
