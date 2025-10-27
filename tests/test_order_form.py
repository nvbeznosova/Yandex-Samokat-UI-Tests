import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils.test_data import order_data_set_1, order_data_set_2


@pytest.mark.parametrize(
    "order_data, color_method, entry_point, title",
    [
        (order_data_set_1, "fill_rent_form_black", "header", "Полный сценарий заказа чёрного самоката (через хедер)"),
        (order_data_set_1, "fill_rent_form_black", "footer", "Полный сценарий заказа чёрного самоката (через футер)"),
        (order_data_set_2, "fill_rent_form_grey", "header", "Полный сценарий заказа серого самоката (через хедер)"),
        (order_data_set_2, "fill_rent_form_grey", "footer", "Полный сценарий заказа серого самоката (через футер)"),
    ],
)
def test_order_form(driver, order_data, color_method, entry_point, title):
    home = HomePage(driver)
    home.open_home()
    home.close_cookie_banner()

    if entry_point == "header":
        home.click_order_button_header()
    else:
        home.click_order_button_footer()

    order_page = OrderPage(driver)
    order_page.fill_order_form(
        name=order_data["name"],
        surname=order_data["surname"],
        address=order_data["address"],
        metro=order_data["metro"],
        phone=order_data["phone"]
    )

    getattr(order_page, color_method)(
        date=order_data["date"],
        period=order_data["period"],
        comment=order_data["comment"]
    )

    order_page.submit_order()

    with allure.step("Проверяем, что заказ успешно оформлен"):
        assert order_page.is_order_confirmed(), f"Заказ не был подтверждён: {title}"