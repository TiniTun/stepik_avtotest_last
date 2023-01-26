from pages.product_page import ProductPage
import time


def test_adding_to_cart_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_card()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_name_book()
    page.should_be_cost_book()
