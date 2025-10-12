from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.scroll_into_view_element(element)
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.scroll_into_view_element(element)

    def scroll_into_view_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_to_questions(self):
        questions = self.find_elements(("class name", "accordion__button"))
        if questions:
            self.scroll_into_view_element(questions[0])