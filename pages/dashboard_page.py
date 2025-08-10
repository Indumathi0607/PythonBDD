from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import Locators


class DashBoardPage(BasePage):

    # Method to close the New launch popup
    def handle_new_launch_alert(self):
        try:
            if self.find_element(Locators.new_launch_alert):
                self.click_element(Locators.new_launch_alert)
        except NoSuchElementException as e:
            print("No alert present", e)

    def get_download_app_button(self):
        download_app_button = self.get_element_text(Locators.download_app_button)
        return download_app_button

    def click_user_profile(self):
        self.click_element(Locators.profile_name_locator)

    def click_logout_button(self):
        self.click_element(Locators.logout_button_locator)
