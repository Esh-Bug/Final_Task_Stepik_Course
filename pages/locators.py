from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")

class ProductPageLocators():
    BASKET_ADD_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    MESSAGE_ADD_TO_BASKET_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages> :nth-child(1)> .alertinner>strong")
    MESSAGE_PRICE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages> :nth-child(3)> .alertinner>p>strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "[class='col-sm-6 product_main']>h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "[class='col-sm-6 product_main']>[class='price_color']")
