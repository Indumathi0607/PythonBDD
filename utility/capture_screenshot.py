import allure
from allure_commons.types import AttachmentType


class CaptureScreenshot:

    def __init__(self, driver):
        self.driver = driver

    #Method to capture the screenshot
    def capture_screenshot(self, screenshot_name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name = screenshot_name,
            attachment_type=AttachmentType.PNG
        )