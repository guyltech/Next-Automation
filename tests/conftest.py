import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.search_results_page import SearchResultsPage


@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    #request.cls.page.set_viewport_size({"width": 1500, "height": 720})
    request.cls.page.goto("https://www.next.co.uk/")
    request.cls.home_page = HomePage(request.cls.page)
    request.cls.login_page = LoginPage(request.cls.page)
    request.cls.registration_page = RegistrationPage(request.cls.page)
    request.cls.search_results_page = SearchResultsPage(request.cls.page)
    yield
    request.cls.page.close()
    browser.close()

# Opens and closes browser when calling a test
# Runs once per test method automatically
@pytest.fixture(scope="function") #autouse=True
def setup_page_function(request, page: Page):
    page.goto("https://www.next.co.uk/")
    request.cls.home_page = HomePage(page)
    request.cls.login_page = LoginPage(page)
    request.cls.registration_page = RegistrationPage(page)
    request.cls.search_results_page = SearchResultsPage(page)