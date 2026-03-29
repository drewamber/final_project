from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form>h2")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form>h2")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")

class BasketPageLocators():
    EMPTY_CONTINUE_LINK = (By.CSS_SELECTOR, "#content_inner>p>a[href]")
    BASKET_ROW = (By.CSS_SELECTOR, ".basket-title>.row")