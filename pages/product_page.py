from pages.base_page import BasePage
from pages.locators import ProductPageLocator


class ProductPage(BasePage):
    def adding_to_card(self):
        add_card = self.browser.find_element(*ProductPageLocator.ADD_CARD_BUTTON)
        add_card.click()
    
    def should_be_name_book(self):
        assert self.is_element_present(*ProductPageLocator.CARD_NAME_BOOK), "Name book in card is not presented"
        card_name_book = self.browser.find_element(*ProductPageLocator.CARD_NAME_BOOK)
        assert self.is_element_present(*ProductPageLocator.NAME_BOOK), "Name book is not presented"
        name_book = self.browser.find_element(*ProductPageLocator.NAME_BOOK)
        assert name_book.text == card_name_book.text, f"Name book incorrect: add card - {card_name_book}, at page - {name_book}"

    def should_be_cost_book(self):
        assert self.is_element_present(*ProductPageLocator.CARD_COST), "Cost book in card is not presented"
        card_cost_book = self.browser.find_element(*ProductPageLocator.CARD_COST)
        assert self.is_element_present(*ProductPageLocator.COST), "Cost book is not presented"
        cost_book = self.browser.find_element(*ProductPageLocator.COST)
        assert card_cost_book.text == cost_book.text, f"Cost book incorrect: add card - {card_cost_book}, at page - {cost_book}"

    def should_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.CARD_NAME_BOOK), "Success message is presented"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocator.CARD_NAME_BOOK), "Success message is disappeared"