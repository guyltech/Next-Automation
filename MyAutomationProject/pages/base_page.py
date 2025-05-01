from typing import Union

from playwright.sync_api import Page, Locator
import time

class BasePage:
    def __init__(self, page:Page):
        self.__page = page

    def fill(self, locator: str, text: str) -> None:
        self.__page.locator(locator).highlight()
        time.sleep(1)
        self.__page.locator(locator).fill(text)

    # click() implementation that supports both str and Locator
    def click(self, locator: Union[str, Locator]) -> None:
        if isinstance(locator, str):
            my_locator = self.__page.locator(locator)  # locator is str
        else:
            my_locator = locator  # locator is already a Locator

        my_locator.highlight()
        time.sleep(1)
        my_locator.click()

    def press_enter(self) -> None:
        self.__page.keyboard.press("Enter")

    def select_option(self, locator: str, text: str) -> None:
        self.__page.locator(locator).highlight()
        time.sleep(1)
        self.__page.locator(locator).select_option(value=text)  # Or: select_option(text)

    def locator(self, locator: str) -> Locator:
        return self.__page.locator(locator)

    # inner_text() implementation that supports both str and Locator
    def inner_text(self, locator: Union[str, Locator]) -> str:
        if isinstance(locator, str): # Check if the locator is a string (CSS selector)
            my_locator = self.__page.locator(locator)
        else: # If it's already a Locator, use it as is
            my_locator = locator

        my_locator.highlight()
        return my_locator.inner_text()

    def nth(self, locator: Union[str, Locator], index: int) -> Locator:
        if isinstance(locator, str):
            my_locator = self.__page.locator(locator)
        else:
            my_locator = locator

        my_locator.nth(index).highlight()
        return my_locator.nth(index)

    def url(self) -> str:
        return self.__page.url

    def get_attribute(self, locator: str, attribute: str) -> str:
        return self.__page.locator(locator).get_attribute(attribute)

    def hover(self, locator: str) -> None:
        self.__page.locator(locator).highlight()
        time.sleep(1)
        self.__page.locator(locator).hover()

    def first(self, locator: Union[str, Locator]) -> Locator:
        if isinstance(locator, str): # Check if the locator is a string (CSS selector)
            my_locator = self.__page.locator(locator) # page.locator will get str as this is the default in Playwright
        else: # If it's already a Locator, use it as is
            my_locator = locator
        return my_locator.first