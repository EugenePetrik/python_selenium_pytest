from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

        BasePage.solve_quiz_and_get_code(self)

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_name_message(self):
        product_name_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE)
        return product_name_message.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def get_product_price_message(self):
        product_price_message = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_MESSAGE)
        return product_price_message.text

    def should_be_product_added_message(self):
        assert self.get_product_name() in self.get_product_name_message()

    def should_be_product_price_message(self):
        assert self.get_product_price() in self.get_product_price_message()
