from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest
import random
import string


LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
PRODUCT_CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
PRODUCT_THE_CITY_AND_THE_STARS = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    main_page = MainPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()


@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket_with_discount(browser, promo):
    main_page = MainPage(browser, f"{PRODUCT_CODERS_AT_WORK}/?promo={promo}")
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.should_be_product_added_message()
    product_page.should_be_product_price_message()


@pytest.mark.need_review
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    main_page = MainPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.should_not_success_message_present()


def test_guest_cant_see_success_message(browser):
    main_page = MainPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_success_message_present()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    main_page = MainPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
    main_page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.should_not_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_THE_CITY_AND_THE_STARS)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_THE_CITY_AND_THE_STARS)
    product_page.open()
    product_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_THE_CITY_AND_THE_STARS)
    product_page.open()
    product_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_items_count_equal(0)
    basket_page.should_visible_text_basket_empty()


@pytest.mark.user_authorization
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        random_email = ''.join([random.choice(string.ascii_letters) for _ in range(10)]) + "@example.com"
        random_pass = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(16)])

        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(random_email, random_pass, random_pass)
        login_page.should_display_success_message()
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
        product_page.open()
        product_page.add_item_to_basket()
        product_page.should_be_product_added_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
        product_page.open()
        product_page.add_item_to_basket()
        product_page.should_be_product_added_message()
        product_page.should_be_product_price_message()


# pytest -s -v --tb=line --language=en test_product_page.py
# pytest -s -v --tb=line --language=en test_product_page.py::test_guest_can_add_product_to_basket_with_discount

# -m - run scenarios with specific @pytest.mark
# pytest -v --tb=line --language=en -m need_review

# py.test -s -v --tb=line --language=en test_product_page.py::TestUserAddToBasketFromProductPage
