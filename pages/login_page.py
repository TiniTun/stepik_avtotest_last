from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time
import base64


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_PAGE_URL in self.browser.current_url, "Url login is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input_email.send_keys(email)

        input_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        input_pass1.send_keys(password)

        input_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        input_pass2.send_keys(password)

        button_reg = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_reg.click()

    def make_login_pass(self):
        email = str(time.time()) + "@fakemail.org"
        message_bytes = email.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        password = base64_message[:9]
        return (email, password)
