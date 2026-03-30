from selenium.common.exceptions import NoAlertPresentException  

from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_name_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT), "Name of product don't found"


    def should_be_price_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "Product Price not found"


    def should_be_msg_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text

        assert product_name in message, "Product name not found on message"


    def compare_basket_and_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

        assert product_price == basket_price, "Product price and basket price is not equal"


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            assert False, "Second alert is not presented"


    def add_product_to_basket(self):

        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_add_to_basket_button()

        self.add_to_basket()

        self.solve_quiz_and_get_code()
        self.should_be_msg_about_adding()
        self.compare_basket_and_product_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
        "Success message is presented, but should not be"

    def should_not_be_success_message_in_4_sec(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
        "Success message is presented, but should not be in 4 seconds"