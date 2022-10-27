# coding=utf-8
from random import randrange

from tests.base_test import BaseTest


class TestCanvasSearch(BaseTest):

    def test_canvas_elements(self):
        self.pages.home_page.canvas_component.verify_page_elements()

    def test_search(self):
        self.pages.home_page.canvas_component.fill_tracking_number(randrange(100, 1000))
        self.pages.home_page.canvas_component.click_track_btn()
        # instead of verifying all elements we can verify only part of them using hamcrest to build smart verifications
        self.pages.system_error_page.verify_page_elements()
