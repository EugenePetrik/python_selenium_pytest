from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, LINK)
    main_page.open()
    main_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_items_count_equal(0)
    basket_page.should_visible_text_basket_empty()

# tb=line - выводить только одну строку из лога каждого упавшего теста
# pytest -v --tb=line --language=en --browser=chrome test_main_page.py

# -m - run scenarios with specific @pytest.mark
# pytest -v --tb=line --language=en --browser=chrome -m login_guest
