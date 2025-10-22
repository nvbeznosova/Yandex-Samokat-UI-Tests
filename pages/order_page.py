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

        self.type(ORDER_FIELD_METRO, metro)
        self.wait_for_visible(METRO_OPTION(metro))
        try:
            self.click(METRO_OPTION(metro))
        except Exception:
            element = self.find_element(METRO_OPTION(metro))
            self.js_click(element)

        self.type(ORDER_FIELD_PHONE, phone)

        next_btn = self.find_element(ORDER_NEXT_BUTTON)
        self.scroll_into_view_element(next_btn)
        try:
            self.click(ORDER_NEXT_BUTTON)
        except Exception:
            self.js_click(next_btn)

        self.wait_for_visible(RENT_PERIOD_DROPDOWN)

    def fill_rent_form_black(self, date, period, comment):
        self._fill_common_rent_fields(date, period)
        self.click(RENT_COLOR_BLACK)
        self.type(RENT_COMMENT, comment)

    def fill_rent_form_grey(self, date, period, comment):
        self._fill_common_rent_fields(date, period)
        self.click(RENT_COLOR_GREY)
        self.type(RENT_COMMENT, comment)

    def fill_rent_form_custom(self, date, period, color_locator, comment):
        self._fill_common_rent_fields(date, period)
        self.click(color_locator)
        self.type(RENT_COMMENT, comment)

    def _fill_common_rent_fields(self, date, period):
        date_input = self.find_element(RENT_DATE_INPUT)
        self.scroll_into_view_element(date_input)
        date_input.clear()
        date_input.send_keys(date)

        self.click(RENT_PERIOD_DROPDOWN)
        self.click(RENT_PERIOD_OPTION(period))

    def submit_order(self):
        self.click(ORDER_SUBMIT_BUTTON)
        self.click(ORDER_CONFIRM_BUTTON)

    def is_order_confirmed(self):
        self.wait_for_visible(ORDER_MODAL_TITLE)
        return True