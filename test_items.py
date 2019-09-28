from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_item_button_is_displayed(browser):
    browser.get(link)

    add_item_button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )

    assert add_item_button.is_displayed()

# pytest --user_language=es --browser_name=chrome test_items.py
# pytest --user_language=es --browser_name=firefox test_items.py
