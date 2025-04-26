# Next.co.uk Automation Project

⚠️ This project is a work in progress. More tests and improvements coming soon.

This project contains end-to-end UI automation tests for [Next.co.uk](https://www.next.co.uk/), built using:

- ✅ Python
- ✅ Playwright
- ✅ Pytest
- ✅ Allure for test reporting

## Test Coverage

- Login flow  
- Add to cart  
- Checkout process  

## Setup & Run

Instructions coming soon...

## 📁 Project Structure
```
project_root/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── search_results_page.py
│   └── components/
│       ├── __init__.py
│       └── common_dialogs.py
│
├── tests/
│   ├── __init__.py
│   ├── base_test.py
│   ├── conftest.py
│   ├── test_header_navigation.py
│   ├── test_login.py
│   ├── test_product_search.py
│   ├── test_registration.py
│   └── test_sorting_and_filtering.py
│
├── pytest.ini
├── requirements.txt
└── README.md


