from selenium.webdriver.common.by import By

ORDER_FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
ORDER_FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
ORDER_FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
ORDER_FIELD_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
ORDER_FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

def METRO_OPTION(name):
    return (By.XPATH, f"//div[contains(@class,'select-search__option') and contains(text(),'{name}')]")

ORDER_NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

RENT_DATE_INPUT = (By.XPATH, "//input[contains(@placeholder,'Когда привезти')]")

RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "div.Dropdown-control")
def RENT_PERIOD_OPTION(text):
    return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{text}']")

RENT_COLOR_BLACK = (By.ID, "black")
RENT_COLOR_GREY = (By.ID, "grey")

RENT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

ORDER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Заказать']")
ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
ORDER_MODAL_TITLE = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")
