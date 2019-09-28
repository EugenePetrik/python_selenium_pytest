from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # Открываем страницу
    page.go_to_login_page()         # Выполняем метод страницы - переходим на страницу логина

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# tb=line - выводить только одну строку из лога каждого упавшего теста
# pytest -v --tb=line --language=en test_main_page.py
