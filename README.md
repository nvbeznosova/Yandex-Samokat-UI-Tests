markdown
# Yandex.Samokat — Selenium WebDriver Tests

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15+-green.svg)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-7.4+-orange.svg)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.13-purple.svg)](https://docs.qameta.io/allure/)
[![Page Object Model](https://img.shields.io/badge/Pattern-POM-blueviolet.svg)](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

Automated UI tests for [Yandex.Samokat](https://qa-scooter.praktikum-services.ru/), a web application for renting electric scooters. The project covers end‑to‑end user flows, FAQ section validation, and logo navigation with Allure reporting.

## Project Description

This project contains end‑to‑end UI tests built with **Selenium WebDriver** and **pytest**.  
It follows the **Page Object Model (POM)** pattern and uses **Allure** for detailed test reports.

## Test Coverage

### Scooter Order (Positive Scenario)
- Full order flow validation:
  - Filling in the order form: first name, last name, address, metro station, phone number
  - Selecting rental date, rental period, scooter color, comment
  - Displaying the order confirmation pop‑up

- **Two entry points** are tested:
  - “Order” button in the **header** (top of the page)
  - “Order” button in the **footer** (bottom of the page, after the steps description and before the FAQ section)

- **Parameterization** is used:
  - 2 different user data sets
  - 2 entry points (top / bottom)

### FAQ (“Questions About Important”)
- 8 separate tests, each verifying a specific question‑answer pair.  
- When the arrow is clicked, the corresponding answer becomes visible.

### Logo Navigation
- Click on “Samokat” logo → stays on the main page
- Click on “Yandex” logo → opens the Dzen homepage in a new window / tab

## Project Structure

```
Yandex-Samokat-UI-Tests/
  ├── README.md
  ├── conftest.py
  ├── pytest.ini
  ├── requirements.txt
  ├── locators/
  │   ├── home_locators.py
  │   └── order_locators.py
  ├── pages/
  │   ├── base_page.py
  │   ├── home_page.py
  │   └── order_page.py
  ├── tests/
  │   ├── test_homepage_ui.py
  │   ├── test_order_form.py
  │   └── test_questions.py
  └── utils/
        ├── config.py
        └── test_data.py
```

text

## Setup & Installation

### Requirements
- Python 3.12+
- Google Chrome / Mozilla Firefox (latest versions)
- Selenium
- pytest
- allure-pytest
- webdriver-manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nvbeznosova/Yandex-Samokat-UI-Tests.git
   cd Yandex-Samokat-UI-Tests
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   # .venv\Scripts\activate    # On Windows 
   ```
   
3. **Install dependencies** 
   ```bash
   pip install -r requirements.txt
   ``` 

### Running tests

1. **Run all tests (default browser = Chrome)**

```bash
  pytest tests/
  ```

2. **Run a specific test file**

```bash
   pytest tests/test_order_form.py 
   ```

3. **Run tests with a specific browser** (Chrome or Firefox)

```bash
   pytest --browser=firefox tests/
   ```

The conftest.py fixture reads the --browser command‑line argument.

### Allure Reports

**To generate and view an Allure report locally**

1. **Run tests with Allure enabled**

```bash
  pytest --alluredir=allure-results
``` 

2. **Generate and open the report**

 ```bash 
  allure serve allure-results
```

In CI/CD (GitHub Actions) the report can be automatically published to GitHub Pages.
