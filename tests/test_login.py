import time
import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_class")
class TestLogin(BaseTest):

    def goto_login_page(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.accounts_icon_click()

    # TC01: Verify error message is displayed when 'Email Address or Customer Number' field is empty
    def test_login_empty_email_or_account_num_displays_error(self) -> None:
        self.goto_login_page()
        self.login_page.fill_login_info("", "usernext1!!")

        self.login_page.continue_shopping_btn_click()
        assert self.login_page.get_login_error_msg() == "Sorry, we have been unable to sign you in."

    #TC02: Verify successful login with valid info
    def test_login_valid_info_goto_my_orders(self) -> None:
        self.goto_login_page()
        self.login_page.fill_login_info("usernext391@gmail.com", "usernext1!!")
        self.login_page.continue_shopping_btn_click()
        assert "account/MyAccount/OrderTracking" in self.login_page.url()

