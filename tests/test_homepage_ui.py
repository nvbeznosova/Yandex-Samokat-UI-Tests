import allure
from pages.home_page import HomePage


@allure.title("Cookie-баннер закрывается и не мешает работе")
def test_cookie_banner_appears_and_disappears(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_header()
    assert "order" in home.get_current_url()


@allure.title("Кнопка 'Заказать' в хедере открывает форму заказа")
def test_order_button_header_is_clickable_and_opens_order(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_header()
    assert "order" in home.get_current_url()


@allure.title("Кнопка 'Заказать' в футере открывает форму заказа")
def test_order_button_footer_is_clickable_and_opens_order(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_footer()
    assert "order" in home.get_current_url()


@allure.title("Клик по логотипу 'Самокат' ведёт на главную страницу")
def test_scooter_logo_redirects_to_home(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_header()
    home.click_scooter_logo()
    assert home.get_current_url() == "https://qa-scooter.praktikum-services.ru/"


@allure.title("Клик по логотипу 'Яндекс' ведёт на главную страницу Дзена")
def test_yandex_logo_redirects_to_dzen(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_yandex_logo()
    current_url = home.get_current_url()
    assert "dzen" in current_url or "ya.ru" in current_url