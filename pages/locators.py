from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = ''

class LoginPageLocators():
    LOGIN_PAGE_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocator():
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CARD_NAME_BOOK = (By.CSS_SELECTOR, "div#messages div:first-child strong")
    NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    CARD_COST = (By.CSS_SELECTOR, "div#messages div:last-child p strong")
    COST = (By.CSS_SELECTOR, "div.product_main p.price_color")
