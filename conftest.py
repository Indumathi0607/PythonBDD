import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    #To disable notifications in Chrome browser
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}  # 1 = Allow, 2 = Block
    options.add_experimental_option("prefs", prefs)

    # Initialize the Chrome webdriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://v2.zenclass.in/login") #Navigate to Zenclass webportal
    driver.maximize_window() #Maximize the browser window

    yield driver #Hand over the driver to execute test functions
    driver.quit() #Closes the browser session after the test execution

