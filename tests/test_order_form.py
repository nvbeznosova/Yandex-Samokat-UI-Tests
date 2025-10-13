import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils.tests_data import order_data_set_1, order_data_set_2

@pytest.mark.parametrize("order_data", [order_data_set_1, order_data_set_2])
@pytest.mark.parametrize("button_top", [True, False])
@pytest.mark.parametrize("date_mode", ["manual", "calendar"])
def test_order_form(driver, order_data, button_top, date_mode):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_order_button(top=button_top)

    order_page = OrderPage(driver)
    order_page.fill_order_form(
        name=order_data["name"],
        surname=order_data["surname"],
        address=order_data["address"],
        metro=order_data["metro"],
        phone=order_data["phone"]
    )

    if date_mode == "manual":
        date_value = order_data["date"]
    else:
        date_value = None  

    order_page.fill_rent_form(
        date=date_value,
        period=order_data["period"],
        color=order_data["color"],
        comment=order_data["comment"]
    )

    order_page.submit_order()
    assert order_page.is_order_successful()