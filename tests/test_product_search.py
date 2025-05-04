import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestProductSearch(BaseTest):

    # TC01: Verify the search results are displayed based on the search query 'Jeans'
    def test_search_jeans_displays_valid_results(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.search_product("jeans","")
        assert self.search_results_page.are_search_results_valid("jeans")

    # TC02: Verify the search results are displayed based on the search query 'Women jeans' on drop down selection
    def test_search_dropdown_women_jeans_displays_valid_results(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.search_product("jeans","Women")
        assert self.search_results_page.are_search_results_valid("jeans")

    # TC03: Verify the search results are displayed based on the search query 'Mango jeans'
    def test_search_dropdown_mango_jeans_displays_valid_results(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.search_product("mango","jeans")
        assert self.search_results_page.are_search_results_valid("jeans")

    # TC04: Verify the search results are displayed based on the search query 'Coffee table'
    def test_search_dropdown_coffe_table_displays_valid_results(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.search_product("coffee", "table")
        assert self.search_results_page.are_search_results_valid("coffee table")

    # TC05: Verify the search box can be cleared to start a new search
    def test_search_clear_btn(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.search_product_clear_search_box("shirt")
        assert self.home_page.is_search_box_clear()

    # TC06: Verify error message is displayed when entering invalid search query / no results found
    def test_search_invalid_query_displays_error(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.search_product("sdgssdfdfffffffffffffffffdsdssdddddddffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","")
        assert "We found no results that closely match your search for" in self.search_results_page.get_invalid_search_error_msg()