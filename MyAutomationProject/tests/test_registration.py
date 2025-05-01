import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_class")
class TestRegistration(BaseTest):

    def goto_registration_page(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.accounts_icon_click()
        self.login_page.register_btn_click()

    # TC01: Verify error message is displayed when 'Title' field is empty
    def test_register_empty_title_displays_error(self) -> None:
        self.goto_registration_page()
        self.registration_page.fill_registration_info("","Guy","Levy","guy@gmail.com","Dfghjk654!","17 04 81","0545896312","17","SW1A 1AA")
        assert self.registration_page.get_empty_title_error_msg() == "Please select your Title."

    # TC02: Verify error message is displayed when 'First Name' field is empty
    def test_register_empty_first_name_displays_error(self) -> None:
        self.registration_page.fill_registration_info("Mr","","Cohen","itay@gmail.com","Dfghjk654!","17 04 81","0545896312","17","SW1A 1AA")
        assert self.registration_page.get_empty_first_name_error_msg() == "Please enter your First Name."

    # TC03: Verify error message is displayed when 'First Name' is in invalid format
    def test_register_invalid_first_name_displays_error(self) -> None:
        self.registration_page.fill_registration_info("Mr","Guy23","Levy","itay@gmail.com","Dfghjk654!","17 04 81","0545896312","17","SW1A 1AA")
        assert self.registration_page.get_invalid_first_name_error_msg() == "Please enter a valid First Name."

    # TC04: Verify error message is displayed when 'Email' is in invalid format
    def test_register_invalid_email_displays_error(self) -> None:
        self.registration_page.fill_registration_info("Mr","Guy","Levy","guy.gmail.com","Dfghjk654!","17 04 81","0545896312","17","SW1A 1AA")
        assert self.registration_page.get_invalid_email_error_msg() == "This value should be a valid email."

    # TC05: Verify error message is displayed when 'Password' is in invalid format
    def test_register_invalid_password_displays_error(self) -> None:
        self.registration_page.fill_registration_info("Mr", "Guy", "Levy", "guy@gmail.com", "12345","17 04 81", "0545896312", "17", "SW1A 1AA")
        assert self.registration_page.get_invalid_password_error_msg() == "Please enter at least 6 characters."