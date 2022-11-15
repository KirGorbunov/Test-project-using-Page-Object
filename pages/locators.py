from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BUSKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    PRODUCT_ADD_TO_BUSKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    COST_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items .row")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

