from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()


@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket_with_discount(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_not_success_message_present()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)

    product_page.should_not_success_message_present()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_not_success_message_disappeared()

# pytest -s -v --tb=line --language=en test_product_page.py
# pytest -s -v --tb=line --language=en test_product_page.py::test_guest_can_add_product_to_basket_with_discount
