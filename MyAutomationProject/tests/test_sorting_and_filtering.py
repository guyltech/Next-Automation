import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestSortingAndFiltering(BaseTest):

    # ! Implement test_navigation_header first !
    def test_sort_beds_most_popular(self) -> None:
        pass