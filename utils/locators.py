from selenium.webdriver.common.by import By

BASE_URL = "https://qa-scooter.praktikum-services.ru"

ORDER_BUTTON_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
ORDER_BUTTON_FOOTER = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")

COOKIE_BANNER = (By.XPATH, "//button[text()='да все привыкли']")

QUESTIONS_BUTTONS = (By.CSS_SELECTOR, "[id^='accordion__heading-']")
QUESTIONS_ANSWERS = (By.CSS_SELECTOR, "[id^='accordion__panel-']")

ORDER_FIELD_NAME = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(1) > input")
ORDER_FIELD_SURNAME = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(2) > input")
ORDER_FIELD_ADDRESS = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(3) > input")
ORDER_FIELD_METRO = (By.CSS_SELECTOR, ".select-search__input")
ORDER_FIELD_PHONE = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(5) > input")
ORDER_NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

def METRO_OPTION(station_name):
    return (By.XPATH, f"//div[contains(@class, 'select-search__option') and text()='{station_name}']")

RENT_DATE_INPUT = (By.CSS_SELECTOR, ".react-datepicker__input-container > input")
CALENDAR_DAY = (By.CSS_SELECTOR, ".react-datepicker__day:not(.react-datepicker__day--outside-month)")

RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

def RENT_PERIOD_OPTION(period):
    return (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{period}']")

RENT_COLOR_BLACK = (By.ID, "black")
RENT_COLOR_GREY = (By.ID, "grey")

RENT_COMMENT = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(4) > input")

ORDER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Заказать']")
ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
ORDER_MODAL_TITLE = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")

SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")