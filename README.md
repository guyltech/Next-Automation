# Next.co.uk Automation Project

⚠️ Work in Progress

This project is a work in progress.
More tests and improvements coming soon.

Automated UI tests for [Next.co.uk](https://www.next.co.uk/) using Python, Playwright, and Pytest.

📂 Project Structure

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

⚙️ Technologies

- ✅ Python
- ✅ Playwright
- ✅ Pytest
- ✅ Allure for test reporting

🚀 How to Run Tests

Install dependencies:
pip install -r requirements.txt

Install Playwright browsers:
playwright install

Run the tests:
pytest

Run tests with Allure reporting:
pytest --alluredir=reports/
allure serve reports/

🧠 Key Concepts
Page Object Model (POM) structure
Component-based composition for reusable sections
Base classes for common logic
Strong typing (type hints) for better code quality
Readable and maintainable test code


📄 License
This project is free and open-source.
