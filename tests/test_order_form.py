import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils.test_data import order_data_set_1, order_data_set_2


@pytest.mark.parametrize("order_data", [order_data_set_1, order_data_set_2])
def test_order_form_header_button_manual_date(driver, order_data):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button_header()

    order_page = OrderPage(driver)
    order_page.fill_order_form(
        name=order_data["name"],
        surname=order_data["surname"],
        address=order_data["address"],
        metro=order_data["metro"],
        phone=order_data["phone"]
    )
    order_page.fill_rent_form(
        date=order_data["date"],
        period=order_data["period"],
        color=order_data["color"],
        comment=order_data["comment"]
    )
    order_page.submit_order()
    assert order_page.is_order_confirmed()