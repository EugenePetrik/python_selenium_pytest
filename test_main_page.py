from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    main_page = MainPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page.open()                     # Открываем страницу
    main_page.go_to_login_page()         # Выполняем метод страницы - переходим на страницу логина

    login_page = LoginPage(browser, browser.current_url)

    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    main_page = MainPage(browser, link)
    main_page.open()

    main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"

    main_page = MainPage(browser, link)
    main_page.open()
    main_page.got_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_visible_text_basket_empty()


# tb=line - выводить только одну строку из лога каждого упавшего теста
# pytest -v --tb=line --language=en test_main_page.py
