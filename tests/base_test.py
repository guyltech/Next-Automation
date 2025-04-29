from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.search_results_page import SearchResultsPage

class BaseTest:
    home_page : HomePage
    login_page : LoginPage
    registration_page : RegistrationPage
    search_results_page : SearchResultsPage