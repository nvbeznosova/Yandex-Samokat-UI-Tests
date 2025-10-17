from selenium.webdriver.common.by import By

ORDER_BUTTON_HEADER = (
    By.XPATH,
    "//button[contains(@class,'Button') and text()='Заказать' and not(contains(@class,'Middle'))]"
)

ORDER_BUTTON_FOOTER = (
    By.XPATH,
    "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']"
)

COOKIE_BANNER = (By.ID, "rcc-confirm-button")

QUESTIONS_BUTTONS = (By.CSS_SELECTOR, "div.accordion__button[id^='accordion__heading-']")
QUESTIONS_ANSWERS = (By.CSS_SELECTOR, "div.accordion__panel[id^='accordion__panel-']")

ORDER_FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")

SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")