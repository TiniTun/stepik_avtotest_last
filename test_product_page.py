from pages.product_page import ProductPage
import time
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('offer', ["offer0", 
                                    "offer1", 
                                    "offer2", 
                                    "offer3", 
                                    "offer4", 
                                    "offer5", 
                                    "offer6", 
                                    pytest.param("offer7", marks=pytest.mark.xfail), 
                                    "offer8", 
                                    "offer9"])
def test_adding_to_cart_from_product_page(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_card()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_name_book()
    page.should_be_cost_book()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_card()
    page.should_be_success_message()

@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_card()
    page.should_be_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
