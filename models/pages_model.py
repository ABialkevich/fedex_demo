import typing

from pydantic import BaseModel

from pages.assistant_page import AssistantPage
from pages.choose_location_page import ChooseLocationPage
from pages.contact_info_page import ContactInfoPage
from pages.home_page import HomePage
from pages.login_credential_page import LoginCredentialPage
from pages.open_acc_page import OpenAccountPage
from pages.system_error_page import SystemErrorPage


class PagesModel(BaseModel):
    choose_location_page: typing.Type[ChooseLocationPage] = None
    home_page: typing.Type[HomePage] = None
    login_credentials_page: typing.Type[LoginCredentialPage] = None
    open_acc_page: typing.Type[OpenAccountPage] = None
    contact_info_page: typing.Type[ContactInfoPage] = None
    system_error_page: typing.Type[SystemErrorPage] = None
    assistant_page: typing.Type[AssistantPage] = None
