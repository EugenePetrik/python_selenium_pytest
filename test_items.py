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

# pytest --language=es --browser=chrome test_items.py
# pytest --language=es --browser=firefox test_items.py
