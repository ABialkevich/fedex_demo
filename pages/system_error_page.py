from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations

from pages.base_page import BasePage


class SystemErrorPage(BasePage):
    NOTIFICATION_ERROR = By.XPATH, '//*[contains(text(),"Unfortunately")]'
    TROUBLE_MSG = By.ID, 'title'

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_elements(self):
        soft_assert(self._is_elem_displayed(self.NOTIFICATION_ERROR))
        verify_expectations()

    def is_trouble_msg_displayed(self):
        return self._is_elem_displayed(self.TROUBLE_MSG)
