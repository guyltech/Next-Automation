import time

import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestSortingAndFiltering(BaseTest):

    # TC01: Verify correct sorting of 'Furniture' products by 'Most Popular' under the 'Beds' subcategory
    def test_sort_beds_most_popular(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.select_main_department_and_sub_category("Furniture", "Beds")
        self.sub_category_page.select_sort_option("Most Popular")
        assert self.sub_category_page.are_products_sorted_by_most_popular(), "Products are not sorted by popularity"

    # TC02: Verify correct sorting of 'Beauty' products by 'Price: Low - High' under the 'Soaps' subcategory
    def test_sort_soaps_price_ascending(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.select_main_department_and_sub_category("Beauty", "Soaps")
        self.sub_category_page.select_sort_option("Price: Low - High")
        assert self.sub_category_page.are_products_sorted_by_price_ascending(), "Products are not sorted by popularity"