from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AboutUsPage(BasePage):
    video_modal = (By.XPATH, '//div[@id="videoModal"]')
    about_us_close_btn = (By.XPATH, '//div[@id="videoModal"]//button[text()="Close"]')
    about_us_x_btn = (By.XPATH, '//div[@id="videoModal"]//div[@class="modal-header"]/button/span[text()="×"]')
    play_btn = (By.XPATH, '//button[@title="Play Video"]')
    video_player = (By.XPATH, '//*[@id="example-video"]')
    video_paused = (By.CLASS_NAME, "vjs-paused")
    video_playing = (By.CLASS_NAME, "vjs-playing")

    def click_close_button(self):
        self.click_on(*self.about_us_close_btn)

    def click_x_icon(self):
        self.click_on(*self.about_us_x_btn)

    def play_video(self):
        self.click_on(*self.play_btn)

    def pause_video(self):
        self.click_on(*self.video_player)

    def wait_for_modal_to_appear(self):
        self.wait_for_visible(*self.video_modal)

    def wait_for_modal_to_disappear(self):
        self.wait_for_not_visible(*self.video_modal)

    def modal_is_displayed(self):
        return self.driver.find_element(*self.video_modal).is_displayed()

    def wait_for_video_to_pause(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.video_paused))

    def video_is_paused(self):
        player = self.driver.find_element(*self.video_player)
        player_class = player.get_attribute("class")

        return "vjs-paused" in player_class

    def wait_for_video_to_play(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.video_playing))

    def video_is_playing(self):
        player = self.driver.find_element(*self.video_player)
        player_class = player.get_attribute("class")

        return "vjs-playing" in player_class

