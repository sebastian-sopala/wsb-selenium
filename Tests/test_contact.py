import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from Pages.home_page import HomePage
from Pages.contact_page import ContactPage


class Contact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()

    def test_close_form_with_close_button(self):
        contact_page = ContactPage(self.driver)
<<<<<<< HEAD
        home_page = HomePage(self.driver).about_us_link
        sleep(1)  # TODO remove this
        contact_page.assert_modal_is_displayed()
=======
        home_page = HomePage(self.driver)

        home_page.open_contact()

        contact_page.wait_for_modal_to_appear()
        self.assertTrue(contact_page.modal_is_displayed())
>>>>>>> 241fab37f2c77d5df57f673da85ff1ea7682fe33

        contact_page.click_close_button()

        contact_page.wait_for_modal_to_disappear()
        self.assertFalse(contact_page.modal_is_displayed())

    def test_close_form_with_X_button(self):
        contact_page = ContactPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_contact()

        contact_page.wait_for_modal_to_appear()
        self.assertTrue(contact_page.modal_is_displayed())

        contact_page.click_x_icon()

        contact_page.wait_for_modal_to_disappear()
        self.assertFalse(contact_page.modal_is_displayed())

    def test_successfully_send_message(self):
        contact_page = ContactPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_contact()

        text_email = "test@wsb.pl"
        contact_page.input_email(text_email)

        text_name = "Bob"
        contact_page.input_name(text_name)

        text_message = "Uncle Bob testing the form !!!"
        contact_page.input_message(text_message)

        contact_page.click_send_button()

        alert = Alert(self.driver)

        self.assertTrue(alert)
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()


if __name__ == "__main__":
    unittest.main(verbosity=2)
