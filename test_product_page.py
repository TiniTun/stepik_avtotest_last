from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time
import pytest
import base64

@pytest.mark.basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        message_bytes = email.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        password = base64_message[:9]
        page.register_new_user(email,password)
        page.should_be_authorized_user()
        time.sleep(10)
    
    
    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_success_message()

    #@pytest.mark.parametrize('offer', ["offer0", 
    #                                    "offer1", 
    #                                    "offer2", 
    #                                    "offer3", 
    #                                    "offer4", 
    #                                    "offer5", 
    #                                    "offer6", 
    #                                    pytest.param("offer7", marks=pytest.mark.xfail), 
    #                                    "offer8", 
    #                                    "offer9"])
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.adding_to_card()
        #page.solve_quiz_and_get_code()
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

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_card()
    page.should_be_success_message_disappeared()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    time.sleep(10)
    basket_page.should_be_basket_items()
    basket_page.should_be_basket_empty()