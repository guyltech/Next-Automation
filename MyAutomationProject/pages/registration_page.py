from playwright.sync_api import Page
from pages.base_page import BasePage

class RegistrationPage(BasePage):

    __TITLE_FIELD = "#Title"
    __FIRST_NAME_FIELD = "#FirstName"
    __LAST_NAME_FIELD = "#LastName"
    __EMAIL_FIELD = "#Email"
    __PASSWORD_FIELD = "#Password"
    __DOB_FIELD = "#DobDate"
    __TELEPHONE_FIELD = "#PhoneNumber"
    __HOUSE_NUM_FIELD = "#HouseNumberOrName"
    __POSTCODE_FIELD = "#Postcode"
    __SMS_CHECKBOX = "#ChkBySms"
    __REGISTER_BTN = "#SignupButton"
    __EMPTY_TITLE_ERROR_MSG = "#Title-error"
    __EMPTY_INVALID_FIRST_NAME_ERROR_MSG = "#FirstName-error"
    __INVALID_EMAIL_ERROR_MSG = "#Email-error"
    __INVALID_PASSWORD_ERROR_MSG = "#Password-error"

    def __init__(self, page:Page):
        super().__init__(page)

    def fill_registration_info(self, title, first_name, last_name, email, password, dob, telephone, house_no, postcode) -> None:
        self.select_option(self.__TITLE_FIELD, title)
        self.fill(self.__FIRST_NAME_FIELD, first_name)
        self.fill(self.__LAST_NAME_FIELD, last_name)
        self.fill(self.__EMAIL_FIELD, email)
        self.fill(self.__PASSWORD_FIELD, password)
        self.fill(self.__DOB_FIELD, dob)
        self.fill(self.__TELEPHONE_FIELD, telephone)
        self.fill(self.__HOUSE_NUM_FIELD, house_no)
        self.fill(self.__POSTCODE_FIELD, postcode)
        self.click(self.__SMS_CHECKBOX)
        self.click(self.__REGISTER_BTN)

    def get_empty_title_error_msg(self) -> str:
        return self.inner_text(self.__EMPTY_TITLE_ERROR_MSG)

    def get_empty_first_name_error_msg(self) -> str:
        return self.inner_text(self.__EMPTY_INVALID_FIRST_NAME_ERROR_MSG)

    def get_invalid_first_name_error_msg(self) -> str:
        return self.inner_text(self.__EMPTY_INVALID_FIRST_NAME_ERROR_MSG)

    def get_invalid_email_error_msg(self) -> str:
        return self.inner_text(self.__INVALID_EMAIL_ERROR_MSG)

    def get_invalid_password_error_msg(self) -> str:
        return self.inner_text(self.__INVALID_PASSWORD_ERROR_MSG)