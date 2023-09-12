import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from Pages.home_page import HomePage
from Pages.about_us_page import AboutUsPage


class AboutUs(unittest.TestCase):

    def setUp(self):
        opts = Options()
        opts.headless = True
        self.driver = webdriver.Firefox(options=opts)
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()

    def test_close_form_with_close_button(self):
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        about_us_page.wait_for_modal_to_appear()
        self.assertTrue(about_us_page.modal_is_displayed())

        sleep(1) # TODO refactor this

        about_us_page.click_close_button()
        about_us_page.wait_for_modal_to_disappear()
        self.assertFalse(about_us_page.modal_is_displayed())

    def test_close_form_with_X_button(self):
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        about_us_page.wait_for_modal_to_appear()
        self.assertTrue(about_us_page.modal_is_displayed())

        sleep(1)  # TODO refactor this

        about_us_page.click_x_icon()
        about_us_page.wait_for_modal_to_disappear()
        self.assertFalse(about_us_page.modal_is_displayed())

    def test_video_is_playing(self):
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        about_us_page.wait_for_modal_to_appear()
        about_us_page.play_video()
        about_us_page.wait_for_video_to_play()
        self.assertTrue(about_us_page.video_is_playing())

    def test_video_is_paused(self):
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        about_us_page.play_video()
        about_us_page.wait_for_video_to_play()
        self.assertTrue(about_us_page.video_is_playing())

        about_us_page.pause_video()
        about_us_page.wait_for_video_to_pause()
        self.assertTrue(about_us_page.video_is_paused())


if __name__ == "__main__":
    unittest.main(verbosity=2)
