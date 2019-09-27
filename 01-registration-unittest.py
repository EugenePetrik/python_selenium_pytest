import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_registration1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")

        first_name = self.driver.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys("Ivan")

        last_name = self.driver.find_element_by_css_selector("input[placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        email = self.driver.find_element_by_css_selector("input[placeholder='Input your email']")
        email.send_keys("ivan.petrov@example.com")

        button = self.driver.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")

        first_name = self.driver.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys("Ivan")

        last_name = self.driver.find_element_by_css_selector("input[placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        email = self.driver.find_element_by_css_selector("input[placeholder='Input your email']")
        email.send_keys("ivan.petrov@example.com")

        button = self.driver.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
