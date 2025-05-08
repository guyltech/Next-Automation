from playwright.sync_api import Page
from pages.base_page import BasePage

class SubCategoryPage(BasePage):

    __SUB_CATEGORY_HEADER = "[data-testid='plp-product-title']"
    __SORT_BTN = "[data-testid='plp-desktop-sort-button']"
    __SORT_OPTIONS_LIST = "[aria-labelledby='desktop-sort-select-label'] li"
    __PRODUCT_STAR_RATING = "[data-testid='product_summary_star-rating']>span[aria-label]"

    def __init__(self, page:Page):
        super().__init__(page)

    def get_sub_category_header(self) -> str:
        return self.inner_text(self.__SUB_CATEGORY_HEADER)

    def select_sort_option(self, sort_option) -> None:
        self.click("[data-testid='plp-desktop-sort-button']")
        sort_options_list = self.locator(self.__SORT_OPTIONS_LIST)
        count = sort_options_list.count()

        for i in range(count):
            option = self.nth(sort_options_list, i)
            text = self.inner_text(option)

            if sort_option in text:
                self.click(option)
                return

        raise Exception(f"Sort option '{sort_option}' not found.")

    def are_products_sorted_by_most_popular(self) -> bool:
        products_star_rating_list = self.locator(self.__PRODUCT_STAR_RATING)
        count = products_star_rating_list.count()
        print(f"🔍 Found {count} star rating elements on the page.")

        if count == 0:
            print("⚠️ No star ratings found!")
            return False

        for i in range(count):
            star_element = self.nth(self.__PRODUCT_STAR_RATING, i)
            aria_label = self.get_attribute(star_element, "aria-label") # aria-label = products_star_rating_list.nth(i).get_attribute("aria-label")
            print(f"⭐ Product {i} has aria-label: {aria_label}")

            if aria_label not in ["4 Stars", "4.5 Stars", "5 Stars"]:
                print(f"❌ Invalid rating found: {aria_label}")
                return False

        print("✅ All products have rating 4 stars or higher.")
        return True

    def are_products_sorted_by_price_ascending(self) -> bool:
        pass

    def select_filter_option(self):
        #self.click("[data-testid='horizontal-filter-facet-New In'] [type='checkbox']")
        pass
