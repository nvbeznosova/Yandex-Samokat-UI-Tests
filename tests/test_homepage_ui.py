import pytest
from pages.home_page import HomePage
from utils import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cookie_banner_appears_and_disappears(driver):
    home = HomePage(driver)
    home.open_home()

    cookie_banner = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locators.COOKIE_BANNER)
    )
    assert cookie_banner.is_displayed()

    home.close_cookie_banner()
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(locators.COOKIE_BANNER)
    )

@pytest.mark.parametrize("top", [True, False])
def test_order_button_is_clickable(driver, top):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()

    locator = locators.ORDER_BUTTON_HEADER if top else locators.ORDER_BUTTON_FOOTER
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    assert True

@pytest.mark.parametrize("top", [True, False])
def test_click_order_button_opens_order_page(driver, top):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()

    home.click_order_button(top=top)

    assert "order" in driver.current_url

    name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locators.ORDER_FIELD_NAME)
    )
    assert name_field.is_displayed()