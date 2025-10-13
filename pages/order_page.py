from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import (
    ORDER_FIELD_NAME,
    ORDER_FIELD_SURNAME,
    ORDER_FIELD_ADDRESS,
    ORDER_FIELD_METRO,
    ORDER_FIELD_PHONE,
    ORDER_NEXT_BUTTON,
    METRO_OPTION,
    RENT_DATE_INPUT,
    CALENDAR_DAY,
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
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ORDER_FIELD_NAME)
        )
        self.scroll_into_view_element(element)
        element.clear()
        element.send_keys(name)

        self.type(ORDER_FIELD_SURNAME, surname)
        self.type(ORDER_FIELD_ADDRESS, address)

        self.click(ORDER_FIELD_METRO)
        self.click(METRO_OPTION(metro))

        self.type(ORDER_FIELD_PHONE, phone)
        self.click(ORDER_NEXT_BUTTON)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RENT_DATE_INPUT)
        )

    def fill_rent_form(self, date, period, color, comment):
        date_input = self.find_element(RENT_DATE_INPUT)
        self.scroll_into_view_element(date_input)
        date_input.send_keys(date)
        self.click(CALENDAR_DAY)

        self.click(RENT_PERIOD_DROPDOWN)
        self.click(RENT_PERIOD_OPTION(period))

        if color == "black":
            self.click(RENT_COLOR_BLACK)
        elif color == "grey":
            self.click(RENT_COLOR_GREY)

        self.type(RENT_COMMENT, comment)

    def submit_order(self):
        self.click(ORDER_SUBMIT_BUTTON)
        self.click(ORDER_CONFIRM_BUTTON)

    def is_order_confirmed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(ORDER_MODAL_TITLE)
            )
            return True
        except:
            return False