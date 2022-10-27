import pytest

from models.pages_model import PagesModel
from pages.assistant_page import AssistantPage
from pages.choose_location_page import ChooseLocationPage
from pages.contact_info_page import ContactInfoPage
from pages.home_page import HomePage
from pages.login_credential_page import LoginCredentialPage
from pages.open_acc_page import OpenAccountPage
from pages.system_error_page import SystemErrorPage


class BaseTest:

    @pytest.fixture(autouse=True)
    def init(self, create_driver):
        self.driver, self.config = create_driver
        self.pages = self.__init_pages()
        self.pages.choose_location_page.select_us_language(language=self.config.language)
        self.pages.choose_location_page.accept_cookies()
        yield self.driver

    def __init_pages(self):
        pages = PagesModel()
        pages.home_page = HomePage(self.driver)
        pages.choose_location_page = ChooseLocationPage(self.driver)
        pages.login_credentials_page = LoginCredentialPage(self.driver)
        pages.open_acc_page = OpenAccountPage(self.driver)
        pages.contact_info_page = ContactInfoPage(self.driver)
        pages.system_error_page = SystemErrorPage(self.driver)
        pages.assistant_page = AssistantPage(self.driver)
        return pages
