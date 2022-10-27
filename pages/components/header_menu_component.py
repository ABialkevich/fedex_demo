from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations

from pages.base_page import BasePage


class HeaderMenuComponent(BasePage):
    GLOBAL_LOGIN = By.ID, 'global-login-wrapper'
    LOGIN_BTN = By.XPATH, '//*[@title="Log In"]'
    CREATE_USER_ID_BTN = By.XPATH, '//*[@title="Create User ID"]'
    OPEN_ACC_BTN = By.XPATH, '//div[@id="global-login-wrapper"]//*[@title="Open an Account"]',
    SEARCH_ICON = By.XPATH, '//*[@class="fxg-keyboard"]'
    SEARCH_INPUT = By.ID, 'fxg-search-text'
    SEARCH_BTN = By.ID, 'fxg-search-icon'
    DROPDOWN_MENU = By.XPATH, '//*[@class="fxg-dropdown__list"]//*[@href="#"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_to_login_menu(self):
        self._click(self.GLOBAL_LOGIN)

    def click_to_login_btn(self):
        self._click(self.LOGIN_BTN)

    def click_to_create_user_id_btn(self):
        self._click(self.CREATE_USER_ID_BTN)

    def click_to_open_acc_btn(self):
        self._click(self.OPEN_ACC_BTN)

    def click_to_search_icon(self):
        self._click(self.SEARCH_ICON)

    def fill_search_input(self, track_number):
        self._fill_text(self.SEARCH_INPUT, track_number)

    def click_to_search_btn(self):
        self._click(self.SEARCH_BTN)

    def get_dropdown_menus(self):
        elements = self._find_elements(web_element=self.DROPDOWN_MENU)
        return [i.text for i in elements]

    def verify_page_elements(self):
        soft_assert(self._is_elem_displayed(self.LOGIN_BTN))
        soft_assert(self._is_elem_displayed(self.CREATE_USER_ID_BTN))
        soft_assert(self._is_elem_displayed(self.OPEN_ACC_BTN))
        soft_assert(self._is_elem_displayed(self.SEARCH_ICON))
        verify_expectations()
