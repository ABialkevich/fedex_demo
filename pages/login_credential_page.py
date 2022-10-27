from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations

from pages.base_page import BasePage


class LoginCredentialPage(BasePage):
    USERNAME = By.ID, 'userId'
    PASSWORD = By.ID, 'password'
    LOGIN_BTN = By.ID, 'login-btn'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_username(self, username):
        self._fill_text(self.USERNAME, username)

    def fill_password(self, password):
        self._fill_text(self.PASSWORD, password)

    def click_login_btn(self):
        self._click(self.LOGIN_BTN)

    def verify_page_elements(self):
        soft_assert(self._is_elem_displayed(self.USERNAME))
        soft_assert(self._is_elem_displayed(self.PASSWORD))
        soft_assert(self._is_elem_displayed(self.LOGIN_BTN))
        verify_expectations()
