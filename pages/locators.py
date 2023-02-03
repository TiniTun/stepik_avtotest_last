from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a[href*='basket']:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a[href*='basket']:first-child")

class LoginPageLocators():
    LOGIN_PAGE_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocator():
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CARD_NAME_BOOK = (By.CSS_SELECTOR, "div#messages div:first-child strong")
    NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    CARD_COST = (By.CSS_SELECTOR, "div#messages div:last-child p strong")
    COST = (By.CSS_SELECTOR, "div.product_main p.price_color")

class BasketPageLocator():
    def __init__(self,params=''):
        self.params = params

    def get_basket_empty(self):
        return (By.CSS_SELECTOR, f"div#content_inner p a[href*='{self.params}']")

    BASKET_ITEMS = (By.CSS_SELECTOR, "form#basket_formset")

