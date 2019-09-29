from .base_page import BasePage
from .locators import BasketPageLocator


class BasketPage(BasePage):

    def get_basket_empty_text(self):
        element = self.browser.find_element(*BasketPageLocator.BASKET_EMPTY_TEXT)
        return element.text

    def get_items_count_in_basket(self):
        all_items = self.browser.find_elements(*BasketPageLocator.BASKET_ITEM)
        return len(all_items)

    def should_visible_text_basket_empty(self):
        assert "Your basket is empty." in self.get_basket_empty_text()

    def should_items_count_equal(self, number):
        return self.get_items_count_in_basket() == number
