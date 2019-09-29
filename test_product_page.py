from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()

# pytest -v --tb=line --language=en test_product_page.py
