from selenium.common import NoSuchElementException, ElementNotVisibleException, TimeoutException, \
    ElementNotInteractableException, ElementClickInterceptedException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # Constructor to initialize driver, timeout window
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    # Method to find elements
    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (TimeoutError, NoSuchElementException, ElementNotVisibleException) as error:
            print("Error: ", error)

    # Method to click on an element
    def click_element(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
        except (ElementNotInteractableException, ElementClickInterceptedException) as error:
            print("Error: ", error)

    # Method to fill in text in a textbox
    def enter_text(self, locator, value):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(value)
        except (ElementNotInteractableException, ElementClickInterceptedException) as error:
            print("Error: ", error)

    # Method to get the text value of a given element
    def get_element_text(self, locator):
        try:
            element = self.find_element(locator)
            return element.text
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as error:
            print("Error: ", error)

    # Method to handle browser alert if any
    def handle_browser_alert(self):
        try:
            browser_alert = self.driver.switch_to.alert
            print("Browser alert text:", browser_alert.text)
            browser_alert.accept()
        except NoAlertPresentException as e:
            print("No browser alert is present", e)
