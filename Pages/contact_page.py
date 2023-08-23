from time import sleep

from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class ContactPage(BasePage):
    contact_close_btn = (By.XPATH, '//div[@id="exampleModal"]//button[text()="Close"]')
    contact_modal = (By.XPATH, '//*[text()="New message"]')
    contact_x_btn = (By.XPATH, '//div[@id="exampleModal"]//div[@class="modal-header"]/button/span[text()="×"]')
    contact_email_field = (By.XPATH, '//*[@id="recipient-email"]')
    contact_name_field = (By.XPATH, '//*[@id="recipient-name"]')
    contact_message_field = (By.XPATH, '//*[@id="message-text"]')
    contact_send_btn = (By.XPATH, '//*[text()="Send message"]')

    def click_close_button(self):
        self.click_on(*self.contact_close_btn)

    def click_x_icon(self):
        self.click_on(*self.contact_x_btn)

    def wait_for_modal_to_appear(self):
        self.wait_for_visible(*self.contact_modal)

    def wait_for_modal_to_disappear(self):
        self.wait_for_not_visible(*self.contact_modal)

    def modal_is_displayed(self):
        return self.driver.find_element(*self.contact_modal).is_displayed()

    def input_email(self, text):
        self.input_text(*self.contact_email_field, text=text)

    def input_name(self, text):
        self.input_text(*self.contact_name_field, text=text)

    def input_message(self, text):
        self.input_text(*self.contact_message_field, text=text)

    def click_send_button(self):
        self.click_on(*self.contact_send_btn)
