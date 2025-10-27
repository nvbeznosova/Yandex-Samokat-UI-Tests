from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_locators import (
    ORDER_FIELD_NAME,
    ORDER_FIELD_SURNAME,
    ORDER_FIELD_ADDRESS,
    ORDER_FIELD_METRO,
    ORDER_FIELD_PHONE,
    ORDER_NEXT_BUTTON,
    RENT_DATE_INPUT,
    RENT_PERIOD_DROPDOWN,
    RENT_COLOR_BLACK,
    RENT_COLOR_GREY,
    RENT_COMMENT,
    ORDER_SUBMIT_BUTTON,
    ORDER_CONFIRM_BUTTON,
    ORDER_MODAL,
    ORDER_MODAL_TITLE,
)


class OrderPage(BasePage):

    def fill_order_form(self, name, surname, address, metro, phone):
        self.type(ORDER_FIELD_NAME, name)
        self.type(ORDER_FIELD_SURNAME, surname)
        self.type(ORDER_FIELD_ADDRESS, address)

        metro_input = self.find_element(ORDER_FIELD_METRO)
        metro_input.clear()
        prefix = metro[:3]
        metro_input.send_keys(prefix)

        WebDriverWait(self.driver, self.timeout).until(
            lambda d: (d.find_element(*ORDER_FIELD_METRO).get_attribute("value") or "").startswith(prefix)
        )

        selected = False
        for _ in range(10):
            metro_input = self.find_element(ORDER_FIELD_METRO)
            metro_input.send_keys(Keys.ARROW_DOWN)
            current = metro_input.get_attribute("value") or ""
            if current.strip().lower() == metro.strip().lower():
                metro_input.send_keys(Keys.ENTER)
                selected = True
                break

        if not selected:
            metro_input = self.find_element(ORDER_FIELD_METRO)
            metro_input.send_keys(Keys.ENTER)
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: (d.find_element(*ORDER_FIELD_METRO).get_attribute("value") or "").strip().lower() == metro.strip().lower()
            )

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
        date_input.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        dropdown = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(RENT_PERIOD_DROPDOWN)
        )
        self.scroll_into_view_element(dropdown)
        try:
            dropdown.click()
        except:
            self.driver.execute_script("arguments[0].click();", dropdown)

        menu = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.Dropdown-menu[aria-expanded='true']"))
        )

        options = menu.find_elements(By.CSS_SELECTOR, "div.Dropdown-option")
        print("Опции в выпадашке:", [opt.text for opt in options])

        for opt in options:
            if opt.text.strip().lower() == period.strip().lower():
                self.scroll_into_view_element(opt)
                opt.click()
                break
        else:
            raise Exception(f"Не найдена опция срока аренды: {period}")

    def submit_order(self):
        self.click(ORDER_SUBMIT_BUTTON)

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(ORDER_MODAL)
        )

        confirm_btn = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(ORDER_CONFIRM_BUTTON)
        )
        self.scroll_into_view_element(confirm_btn)
        try:
            confirm_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", confirm_btn)

    def is_order_confirmed(self):
        self.wait_for_visible(ORDER_MODAL_TITLE)
        return True