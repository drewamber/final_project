# Без этой части base page тесты не запускаются 
import sys 
import os 
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# Без этой части base page тесты не запускаются

import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.multicheck
@pytest.mark.parametrize(
    'link',
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail(reason="Известная проблема с этим промо")
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    """
    Тест кейс для проверки того, что юзер может добавить продукт в корзину
    """
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()

@pytest.mark.negative_checks
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    """
    Тест кейс для проверки того, что юзер не видит сообщение об успешном добавлении в корзину при открытии страницы
    """
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.negative_checks
@pytest.mark.xfail(reason="падает по заданию")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    """
    Тест кейс для проверки того, что юзер не видит сообщение об успешном добавлении в корзину при добавлении товара в корзину
    """
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

@pytest.mark.negative_checks
@pytest.mark.xfail(reason="падает по заданию")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    """
    Тест кейс для проверки того, что сообщение о добавлении исчезает максимум в течение 4 секунд после добавления 
    """
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message_in_4_sec()

@pytest.mark.current
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.current
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page.should_be_login_url()

@pytest.mark.checks
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.checks
def test_guest_cant_see_product_in_basket_opened_from_product_page_no_row(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()

@pytest.mark.actions_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()



    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        """
        Тест кейс для проверки того, что юзер не видит сообщение об успешном добавлении в корзину при открытии страницы
        """
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        """
        Тест кейс для проверки того, что юзер может добавить продукт в корзину
        """
        product_page = ProductPage(browser, link)
        product_page.open()
        time.sleep(5)
        product_page.add_product_to_basket()