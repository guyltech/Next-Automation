import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestSortingAndFiltering(BaseTest):

    # Verify correct sorting of 'Furniture' products by 'Most Popular' under the 'Beds' subcategory
    def test_sort_beds_most_popular(self) -> None:
        self.home_page.common_dialogs.close_accept_cookies_and_country_dialog()
        self.home_page.select_main_department_and_sub_category("Furniture", "Beds")
        self.sub_category_page.are_products_sorted_by_most_popular()
        #assert "men" in self.search_results_page.url()