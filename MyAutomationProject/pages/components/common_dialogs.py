from pages.base_page import BasePage

class CommonDialogs(BasePage):

    __ACCEPT_ALL_COOKIES_BTN = "#onetrust-accept-btn-handler"
    __CLOSE_CHANGE_COUNTRY_BTN = "[data-testid='country-selector-close-button']"

    def __init__(self, page):
        super().__init__(page)

    def close_accept_cookies_and_country_dialog(self) -> None:
        self.click(self.__ACCEPT_ALL_COOKIES_BTN)
        self.click(self.__CLOSE_CHANGE_COUNTRY_BTN)