from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):

    __EMAIL_OR_ACCOUNT_NUM_FIELD = "#EmailOrAccountNumber"
    __PASSWORD_FIELD = "#Password"
    __LOGIN_ERROR_MSG = ".SignInTo .msgboxTitle" #".SignInTo>.messagebox.Failure>.msgContent>.msgboxTitle"
    __SIGN_IN_BTN = "#SignInNow"
    __REGISTER_NOW_BTN = "[data-ga-guest-label='Sign-up-now']"
    __CONTINUE_SHOPPING_BTN = ".link-btn"

    def __init__(self, page:Page):
        super().__init__(page)

    def fill_login_info(self, email_or_account_num, password) -> None:
        self.fill(self.__EMAIL_OR_ACCOUNT_NUM_FIELD, email_or_account_num)
        self.fill(self.__PASSWORD_FIELD, password)
        self.click(self.__SIGN_IN_BTN)

    def get_login_error_msg(self) -> str:
        return self.inner_text(self.__LOGIN_ERROR_MSG)

    def register_btn_click(self) -> None:
        self.click(self.__REGISTER_NOW_BTN)

    def continue_shopping_btn_click(self) -> None:
        self.click(self.__CONTINUE_SHOPPING_BTN)