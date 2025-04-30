import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestHeaderNavigation(BaseTest):

    # TC01: Verify clicking the 'Men' category navigates the user to the corresponding category page
    def test_click_men_department_navigates_correctly(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.select_main_department_and_sub_category("Men","")
        assert "men" in self.search_results_page.url()

    # TC02: Verify clicking the subcategory 'Jackets & Coats' under the 'Men' category navigates the user to the corresponding category page
    def test_click_subcategory_men_jackets_and_coats_navigates_correctly(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.select_main_department_and_sub_category("Men","Shoes")
        #assert "coatsandjackets" in self.search_results_page.url()

    # TC03: Verify clicking the 'Baby' category navigates the user to the corresponding category page


    # TC04: Verify clicking the subcategory 'First Size' under the 'Baby' category navigates the user to the corresponding category page


    # TC05: Verify clicking the subcategory 'GHD' under the 'Beauty' category navigates the user to the corresponding category page

