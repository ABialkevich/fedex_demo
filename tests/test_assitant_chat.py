# coding=utf-8

from tests.base_test import BaseTest


class TestSingUpLogInMenu(BaseTest):

    def test_sing_up_sign_in_menu_is_opened(self):
        self.pages.home_page.canvas_component.click_assistant_icon()
        # instead of verifying all elements we can verify only part of them using hamcrest to build smart verifications
        self.pages.assistant_page.verify_page_elements()
