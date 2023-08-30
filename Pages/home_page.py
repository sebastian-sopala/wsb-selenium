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
    first_image = (By.XPATH, '//img[@src="Samsung1.jpg"]')
    second_image = (By.XPATH,  '//img[@src="nexus1.jpg"]')
    third_image = (By.XPATH,  '//img[@src="iphone1.jpg"]')
    next_icon_right = (By.XPATH, '//a[@class="carousel-control-next"]')
    next_icon_left = (By.XPATH, '//a[@class="carousel-control-prev"]')
    categories_phones = (By.XPATH, '//a[text()="Phones"]')
    categories_laptops = (By.XPATH, '//a[text()="Laptops"]')
    categories_monitors = (By.XPATH, '//a[text()="Monitors"]')
    url_list_items = (By.XPATH, "//a[@href='https://demoblaze.com/index.html#']")

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
        return self.driver.find_element(*self.first_image).is_displayed()

    def move_image_second(self):
        return self.driver.find_element(*self.second_image).is_displayed()

    def move_image_third(self):
        return self.driver.find_element(*self.third_image).is_displayed()

    def find_next_icon(self):
        located_by, located_value = self.next_icon_right
        self.driver.find_element(located_by, located_value).click()

    def find_previous_icon(self):
        located_by, located_value = self.next_icon_left
        self.driver.find_element(located_by, located_value).click()

    def click_categories_phones(self):
        located_by, locator_value = self.categories_phones
        self.driver.find_element(located_by, locator_value).click()

    def click_categories_laptops(self):
        located_by, locator_value = self.categories_laptops
        self.driver.find_element(located_by, locator_value).click()

    def click_categories_monitors(self):
        located_by, locator_value = self.categories_monitors
        self.driver.find_element(located_by, locator_value).click()
