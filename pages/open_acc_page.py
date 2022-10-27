from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations

from pages.base_page import BasePage


class OpenAccountPage(BasePage):
    CARD = By.ID, '#card'
    INVOICE = By.ID, '#invoice'

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_elements(self):
        soft_assert(self._is_elem_displayed(self.CARD))
        soft_assert(self._is_elem_displayed(self.INVOICE))
        verify_expectations()
