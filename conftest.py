import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils.locators import BASE_URL


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
