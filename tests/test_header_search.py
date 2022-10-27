# coding=utf-8
from random import randrange

from tests.base_test import BaseTest


class TestHeaderSearch(BaseTest):

    def test_create_user_id_btn(self):
        self.pages.home_page.header_menu_component.click_to_search_icon()
        self.pages.home_page.header_menu_component.fill_search_input(randrange(100, 1000))
        self.pages.home_page.header_menu_component.click_to_search_btn()

        # instead of verifying all elements we can verify only part of them using hamcrest to build smart verifications
        self.pages.system_error_page.verify_page_elements()
