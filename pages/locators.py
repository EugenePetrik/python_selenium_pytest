from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_ICON = (By.CSS_SELECTOR, "span.btn-group a[href='/ru/basket/']")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_ADDED_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]")
    ITEM_PRICE_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + p.price_color")


class BasketPageLocator:
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
