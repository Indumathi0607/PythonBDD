from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import Locators


class LoginPage(BasePage):

    def enter_username(self, username):
        self.enter_text(Locators.username_locator, username)

    def enter_password(self, password):
        self.enter_text(Locators.password_locator, password)

    def click_login_button(self):
        self.click_element(Locators.login_button_locator)

    def get_sign_in_button_text(self):
        sign_in_button_text = self.get_element_text(Locators.login_button_locator)
        return sign_in_button_text

    def get_incorrect_credential_error_text(self):
        error_text = self.find_element(Locators.incorrect_credentials_error_locator)
        return error_text.text
