from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),
        "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),
        "Register form is not presented"

    def register_new_user(self, email, password, confirm_password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)

        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_pass.send_keys(password)

        reg_conf_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        reg_conf_pass.send_keys(confirm_password)

        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()

    def should_display_success_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MESSAGE), \
            "Registration success message is not displayed"
