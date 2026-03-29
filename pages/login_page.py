from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login url is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "registration form is not presented"
    
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "lindalampeniuspeteparkkonenliekinheitin"
        # поле email
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)

        # поле пароль
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)

        # подтверждение пароля
        password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_confirm.send_keys(password)

        # кнопка регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()