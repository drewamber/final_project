from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CONTINUE_LINK), "Basket is not empty"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ROW), \
        "Basket row is visible but should not be"

    def should_be_good_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ROW), "Basket is empty"