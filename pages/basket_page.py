from pages.base_page import BasePage
from pages.locators import BasketPageLocator
from urllib.parse import urlparse


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        url_parse = urlparse(self.browser.current_url)
        url_path = url_parse.path.split('/')[1]
        assert self.is_element_present(*BasketPageLocator(url_path).get_basket_empty()), "Basket is not empty"

    def should_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_ITEMS), "Basked is not empty"