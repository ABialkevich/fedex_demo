from operator import is_not

from _pytest.fixtures import fixture
from hamcrest import assert_that, equal_to

from factories.user_factory import UserFactory
from helper_enums.user_enum import UserEnum
from tests.base_test import BaseTest


class TestSingUpLogInMenu(BaseTest):

    @fixture()
    def open_login_menu(self):
        self.pages.home_page.header_menu_component.click_to_login_menu()

    def test_sing_up_login_component_elements(self, open_login_menu):
        # instead of verifying all elements we can verify only part of them using hamcrest to build smart verifications
        self.pages.home_page.header_menu_component.verify_page_elements()

    def test_login_btn(self, open_login_menu):
        self.pages.home_page.header_menu_component.click_to_login_btn()
        self.pages.login_credentials_page.verify_page_elements()

    def test_login_by_unknown_user(self, open_login_menu):
        user = UserFactory.get_user(user=UserEnum.COGNITO)
        self.pages.home_page.header_menu_component.click_to_login_btn()
        self.pages.login_credentials_page.fill_username(user.username)
        self.pages.login_credentials_page.fill_password(user.password)
        self.pages.login_credentials_page.click_login_btn()

        # assert_that(self.pages.system_error_page.is_trouble_msg_displayed(), equal_to(True))

    def test_open_acc_btn(self, open_login_menu):
        self.pages.home_page.header_menu_component.click_to_open_acc_btn()
        self.pages.open_acc_page.verify_page_elements()

    def test_create_user_id_btn(self, open_login_menu):
        self.pages.home_page.header_menu_component.click_to_create_user_id_btn()
        self.pages.contact_info_page.verify_page_elements()
