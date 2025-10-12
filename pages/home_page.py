from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import (
    ORDER_BUTTON_HEADER,
    ORDER_BUTTON_FOOTER,
    COOKIE_BANNER,
    QUESTIONS_BUTTONS,
    QUESTIONS_ANSWERS,
    ORDER_FIELD_NAME,
)

class HomePage(BasePage):

    def open_home(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def close_cookie_banner(self):
        try:
            button = self.find_element(COOKIE_BANNER)
            button.click()
        except TimeoutException:
            pass

    def scroll_to_order_button(self, top=True):
        locator = ORDER_BUTTON_HEADER if top else ORDER_BUTTON_FOOTER
        try:
            button = self.find_element(locator)
            self.scroll_into_view_element(button)
        except TimeoutException:
            pass

    def click_order_button(self, top=True):
        locator = ORDER_BUTTON_HEADER if top else ORDER_BUTTON_FOOTER
        self.scroll_to_order_button(top)
        try:
            button = self.find_element(locator)
            button.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(ORDER_FIELD_NAME)
            )
        except TimeoutException:
            pass

    def click_question_by_index(self, index):
        self.scroll_to_questions()
        questions = self.driver.find_elements(*QUESTIONS_BUTTONS)
        if index < len(questions):
            element = questions[index]
            self.scroll_into_view_element(element)
            self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text_by_index(self, index):
        try:
            answers = WebDriverWait(self.driver, 5).until(
                lambda d: d.find_elements(*QUESTIONS_ANSWERS)
            )
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of(answers[index])
            )
            return answers[index].text.strip()
        except (IndexError, TimeoutException):
            return ""

    def scroll_to_questions(self):
        try:
            first_question = self.driver.find_elements(*QUESTIONS_BUTTONS)[0]
            self.scroll_into_view_element(first_question)
        except IndexError:
            pass