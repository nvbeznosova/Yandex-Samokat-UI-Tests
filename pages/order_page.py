from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_locators import (
    ORDER_FIELD_NAME,
    ORDER_FIELD_SURNAME,
    ORDER_FIELD_ADDRESS,
    ORDER_FIELD_METRO,
    METRO_OPTION,
    ORDER_FIELD_PHONE,
    ORDER_NEXT_BUTTON,
    RENT_DATE_INPUT,
    RENT_PERIOD_DROPDOWN,
    RENT_PERIOD_OPTION,
    COLOR_CHECKBOX,
    RENT_COLOR_BLACK,
    RENT_COLOR_GREY,
    RENT_COMMENT,
    ORDER_SUBMIT_BUTTON,
    ORDER_CONFIRM_BUTTON,
    ORDER_MODAL_TITLE,
)


class OrderPage(BasePage):

    def fill_order_form(self, name, surname, address, metro, phone):
        self.type(ORDER_FIELD_NAME, name)
        self.type(ORDER_FIELD_SURNAME, surname)
        self.type(ORDER_FIELD_ADDRESS, address)

        self.click(ORDER_FIELD_METRO)
        self.wait_for_visible(METRO_OPTION(metro))
        try:
            self.click(METRO_OPTION(metro))
        except Exception:
            element = self.find_element(METRO_OPTION(metro))
            self.driver.execute_script("arguments[0].click();", element)

        self.type(ORDER_FIELD_PHONE, phone)
        self.click(ORDER_NEXT_BUTTON)

        self.wait_for_visible(RENT_DATE_INPUT)
        date_input = self.find_element(RENT_DATE_INPUT)
        self.scroll_into_view_element(date_input)

    def fill_rent_form(self, date, period, color, comment):
        self.wait_for_visible(RENT_DATE_INPUT)
        date_input = self.find_element(RENT_DATE_INPUT)
        self.scroll_into_view_element(date_input)

        date_input.clear()
        date_input.send_keys(date)

        self.click(RENT_PERIOD_DROPDOWN)
        self.click(RENT_PERIOD_OPTION(period))

        if color in ["black", "черный жемчуг"]:
            self.click(RENT_COLOR_BLACK)
        elif color in ["grey", "серая безысходность"]:
            self.click(RENT_COLOR_GREY)
        else:
            self.click(COLOR_CHECKBOX(color))

        self.type(RENT_COMMENT, comment)

    def submit_order(self):
        self.click(ORDER_SUBMIT_BUTTON)
        self.click(ORDER_CONFIRM_BUTTON)

    def is_order_confirmed(self):
        self.wait_for_visible(ORDER_MODAL_TITLE)
        return True