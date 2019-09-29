from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    main_page = MainPage(browser, link)
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()


@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket_with_discount(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"

    main_page = MainPage(browser, link)
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    main_page = MainPage(browser, link)
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_not_success_message_present()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    main_page = MainPage(browser, link)
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)

    product_page.should_not_success_message_present()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    main_page = MainPage(browser, link)
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()

    product_page.should_not_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)

    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.got_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_items_count_equal(0)
    basket_page.should_visible_text_basket_empty()


# pytest -s -v --tb=line --language=en test_product_page.py
# pytest -s -v --tb=line --language=en test_product_page.py::test_guest_can_add_product_to_basket_with_discount
# pytest -s -v --tb=line --language=en test_product_page.py::test_guest_should_see_login_link_on_product_page
# pytest -s -v --tb=line --language=en test_product_page.py::test_guest_can_go_to_login_page_from_product_page
# pytest -s -v --tb=line --language=en test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page
