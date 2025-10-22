import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.home_locators import (
    ORDER_BUTTON_HEADER,
    ORDER_BUTTON_FOOTER,
    COOKIE_BANNER,
    QUESTIONS_BUTTONS,
    QUESTIONS_ANSWERS,
    ORDER_FIELD_NAME,
    SCOOTER_LOGO,
    YANDEX_LOGO,
)
from utils.config import BASE_URL


class HomePage(BasePage):
    @allure.step("Открываем главную страницу")
    def open_home(self):
        self.open_url(BASE_URL)

    @allure.step("Закрываем cookie-баннер")
    def close_cookie_banner(self):
        button = self.find_element(COOKIE_BANNER)
        button.click()

    @allure.step("Кликаем на кнопку 'Заказать' в хедере")
    def click_order_button_header(self):
        self.click(ORDER_BUTTON_HEADER)
        self.wait_for_visible(ORDER_FIELD_NAME)

    @allure.step("Кликаем на кнопку 'Заказать' в футере")
    def click_order_button_footer(self):
        footer_button = self.wait_for_clickable(ORDER_BUTTON_FOOTER)
        self.scroll_into_view_element(footer_button)
        try:
            footer_button.click()
        except Exception:
            self.js_click(footer_button)
        self.wait_for_visible(ORDER_FIELD_NAME)

    @allure.step("Кликаем на вопрос с индексом {index}")
    def click_question_by_index(self, index):
        self.js_scroll("document.querySelector('.Home_FAQ__3uVm4').scrollIntoView({block: 'center'});")
        questions = self.find_elements(QUESTIONS_BUTTONS)
        element = questions[index]
        self.scroll_into_view_element(element)
        self.js_click(element)

    @allure.step("Получаем текст ответа для вопроса с индексом {index}")
    def get_answer_text_by_index(self, index):
        answers = self.find_elements(QUESTIONS_ANSWERS)
        element = answers[index]
        self.wait_for_visible((By.ID, element.get_attribute("id")))
        return element.text.strip()

    @allure.step("Кликаем на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click(SCOOTER_LOGO)

    @allure.step("Кликаем на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click(YANDEX_LOGO)
        self.wait_for_new_window_and_switch()
        self.wait_for_url_not_blank()