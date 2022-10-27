# coding=utf-8
from hamcrest import assert_that, equal_to

from tests.base_test import BaseTest


class TestHeaderDropDownMenus(BaseTest):

    def test_sing_up_sign_in_menu_is_opened(self):
        expected_menu = ['Shipping', 'Tracking', 'Support', 'Account']
        dropdown_menu_names = self.pages.home_page.header_menu_component.get_dropdown_menus()

        assert_that(expected_menu, equal_to(dropdown_menu_names))
