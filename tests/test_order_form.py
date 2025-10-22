from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils.test_data import order_data_set_1, order_data_set_2


def test_order_form_black_scooter(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_header()

    order_page = OrderPage(driver)
    order_page.fill_order_form(
        name=order_data_set_1["name"],
        surname=order_data_set_1["surname"],
        address=order_data_set_1["address"],
        metro=order_data_set_1["metro"],
        phone=order_data_set_1["phone"]
    )
    order_page.fill_rent_form_black(
        date=order_data_set_1["date"],
        period=order_data_set_1["period"],
        comment=order_data_set_1["comment"]
    )
    order_page.submit_order()
    assert order_page.is_order_confirmed()


def test_order_form_grey_scooter(driver):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_header()

    order_page = OrderPage(driver)
    order_page.fill_order_form(
        name=order_data_set_2["name"],
        surname=order_data_set_2["surname"],
        address=order_data_set_2["address"],
        metro=order_data_set_2["metro"],
        phone=order_data_set_2["phone"]
    )
    order_page.fill_rent_form_grey(
        date=order_data_set_2["date"],
        period=order_data_set_2["period"],
        comment=order_data_set_2["comment"]
    )
    order_page.submit_order()
    assert order_page.is_order_confirmed()