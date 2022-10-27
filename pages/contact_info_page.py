from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations

from pages.base_page import BasePage


class ContactInfoPage(BasePage):
    UID = By.ID, 'uid'
    PASSWORD = By.ID, 'password'

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_elements(self):
        soft_assert(self._is_elem_displayed(self.UID))
        soft_assert(self._is_elem_displayed(self.PASSWORD))
        verify_expectations()
