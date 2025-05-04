import time
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from pages.components.common_dialogs import CommonDialogs


class HomePage(BasePage):

    __ACCOUNTS_ICON = "[data-testid='header-adaptive-my-account-icon-container-link']"
    __SEARCH_PRODUCT_FIELD = "#header-big-screen-search-box"
    __SEARCH_PRODUCT_BTN = "[data-testid='header-search-bar-button']"
    __SEARCH_BAR_SUGGESTIONS_LIST = "[data-testid='searchBar-suggestions']>li span"
    __CLEAR_SEARCH_BTN = "[data-testid='header-search-bar-clear-text-button']"
    __MEN_DEPARTMENT_LINK = "[title='MEN']"
    __BABY_DEPARTMENT_LINK = "[title='BABY']"
    __FURNITURE_DEPARTMENT_LINK = "[title='FURNITURE']"
    __BEAUTY_DEPARTMENT_LINK = "[title='BEAUTY']"
    __MEN_SUB_CATEGORY_LINKS = "[href*='gender-men']"
    __BABY_SUB_CATEGORY_LINKS = "[href*='gender-newborn']"
    __FURNITURE_SUB_CATEGORY_LINKS = "[href*='department-homeware']"
    __BEAUTY_SUB_CATEGORY_LINKS = "[href*='department-beauty']"
    __MEN_JACKETS_AND_COATS_CATEGORY_LINK = "[href='/shop/gender-men-productaffiliation-coatsandjackets-0']"

    def __init__(self, page:Page):
        super().__init__(page)
        self.common_dialogs = CommonDialogs(page)

    def accounts_icon_click(self) -> None:
        self.click(self.__ACCOUNTS_ICON)

    def search_product(self, search_text_direct, search_text_dropdown) -> None:
        self.fill(self.__SEARCH_PRODUCT_FIELD,search_text_direct)
        if search_text_dropdown: # if user selects value from the dropdown menu
            time.sleep(2)
            suggestions_list = self.locator(self.__SEARCH_BAR_SUGGESTIONS_LIST)
            count = suggestions_list.count() #print(f"Dropdown count: {count}")

            for i in range(count):
                suggestion_text = self.inner_text(self.nth(suggestions_list,i)) # suggestion_text = suggestions_list.nth(i).inner_text() #print(suggestion_text)
                if search_text_dropdown in suggestion_text:
                    self.click(self.nth(suggestions_list,i)) #suggestions_list.nth(i).click()
                    break
        else:
            self.click(self.__SEARCH_PRODUCT_BTN)

        time.sleep(5)

    def search_product_clear_search_box(self, search_text_direct) -> None:
        self.fill(self.__SEARCH_PRODUCT_FIELD,search_text_direct)
        self.click(self.__CLEAR_SEARCH_BTN)

    def is_search_box_clear(self) -> bool:
        value = self.get_attribute(self.__SEARCH_PRODUCT_FIELD,"value") # value = page.locator("input").get_attribute("value")
        return (value is None) or (value == "")

    def select_main_department_and_sub_category(self, main_department, sub_category) -> None:
        match main_department:
            case "Men":
                self.hover(self.__MEN_DEPARTMENT_LINK)
                if sub_category:
                    sub_category_list = self.locator(self.__MEN_SUB_CATEGORY_LINKS)
                    self.select_sub_category(sub_category, sub_category_list)
                else:
                    self.click(self.__MEN_DEPARTMENT_LINK)
            case "Baby":
                self.hover(self.__BABY_DEPARTMENT_LINK)
                if sub_category:
                    sub_category_list = self.locator(self.__BABY_SUB_CATEGORY_LINKS)
                    self.select_sub_category(sub_category, sub_category_list)
                else:
                    self.click(self.__BABY_DEPARTMENT_LINK)
            case "Furniture":
                self.hover(self.__FURNITURE_DEPARTMENT_LINK)
                if sub_category:
                    sub_category_list = self.locator(self.__FURNITURE_SUB_CATEGORY_LINKS)
                    self.select_sub_category(sub_category, sub_category_list)
                else:
                    self.click(self.__FURNITURE_DEPARTMENT_LINK)
            case "Beauty":
                self.hover(self.__BEAUTY_DEPARTMENT_LINK)
                if sub_category:
                    sub_category_list = self.locator(self.__BEAUTY_SUB_CATEGORY_LINKS)
                    self.select_sub_category(sub_category, sub_category_list)
                else:
                    self.click(self.__BEAUTY_DEPARTMENT_LINK)
            case _:
                raise ValueError(f"Unsupported option: {main_department}")
        time.sleep(5)

    def select_sub_category(self, sub_category: str, sub_category_list : Locator) -> None:
        time.sleep(2)
        count = sub_category_list.count()

        for i in range(count):
            sub_category_text = self.inner_text(self.nth(sub_category_list,i))  # sub_category_text = sub_category_list.nth(i).inner_text()
            if sub_category == sub_category_text:
                first_match = self.first(self.nth(sub_category_list, i))
                self.click(first_match) # sub_category_list.nth(i).first.click
                break
        time.sleep(5)