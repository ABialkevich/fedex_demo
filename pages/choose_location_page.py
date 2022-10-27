from selenium.webdriver.common.by import By

from helper_enums.language_enum import LanguageEnum
from pages.base_page import BasePage


class ChooseLocationPage(BasePage):
    US_COUNTRY_TITLE_STR = '//*[@data-country-code="gb" and @aria-label="{language}"]'
    ACCEPT_COOKIES = By.XPATH, '//button[contains(@class,"is-save-all")]'

    def __init__(self, driver):
        super().__init__(driver)

    def select_us_language(self, language):
        self._click(self.language_btn(language))

    def language_btn(self, language):
        return By.XPATH, self.US_COUNTRY_TITLE_STR.format(language=LanguageEnum[language].value)

    def accept_cookies(self):
        count = 3
        while self._is_elem_displayed(self.ACCEPT_COOKIES, timeout=2) and count > 0:
            self._click(self.ACCEPT_COOKIES)
            count -= 1
