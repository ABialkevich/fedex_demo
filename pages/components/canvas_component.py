import time

from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations

from pages.base_page import BasePage


class CanvasComponent(BasePage):
    TRACKING_NUMBER_INPUT = By.ID, 'trackingnumber'
    TRACK_BTN = By.ID, 'btnSingleTrack'
    ASSISTANT_ICON = By.XPATH, '//*[@class="va_icon"]'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_tracking_number(self, tracking_number):
        self._fill_text(self.TRACKING_NUMBER_INPUT, tracking_number)

    def click_track_btn(self):
        while self._is_elem_displayed(self.TRACK_BTN, timeout=5):
            self._click(self.TRACK_BTN)
            time.sleep(3)

    def click_assistant_icon(self):
        self._click(self.ASSISTANT_ICON)

    def verify_page_elements(self):
        soft_assert(self._is_elem_displayed(self.TRACK_BTN))
        soft_assert(self._is_elem_displayed(self.TRACKING_NUMBER_INPUT))
        verify_expectations()
