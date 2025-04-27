from playwright.sync_api import Page
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    __PRODUCT_TITLE = "[data-testid='product_summary_title']"
    __INVALID_SEARCH_ERROR_MSG = "[data-testid='plp-no-results-header']"

    def __init__(self, page:Page):
        super().__init__(page)

    def are_search_results_valid(self, search_text) -> bool:
        products_title_list = self.locator(self.__PRODUCT_TITLE)
        count = products_title_list.count()
        print(f"Found {count} product titles on the results page.")

        if count == 0:
            print("⚠️ No product titles found!")
            return False

        for i in range(count):
            product_title = self.inner_text(
                self.nth(self.__PRODUCT_TITLE, i))  # product_title = products_list.nth(i).inner_text()
            print(f"Product title [{i}]: {product_title}")

            search_text_lower = search_text.lower()
            product_title_lower = product_title.lower()

            if search_text_lower in product_title_lower:
                print(f"✅ '{search_text}' was found in: '{product_title}'")
                continue
            else:
                print(f"❌ '{search_text}' was NOT found in: '{product_title}'")
                print("")
                return False

        print("")
        return True

    def get_invalid_search_error_msg(self) -> str:
        return self.inner_text(self.__INVALID_SEARCH_ERROR_MSG)