# This class contains locators of all webpages of the application under test
from selenium.webdriver.common.by import By


class Locators:

    #Locators of Login page
    username_locator = (By.XPATH, "//input[@placeholder = 'Enter your mail']")        #XPATH
    password_locator = (By.XPATH,"//input[@placeholder = 'Enter your password ']")    #XPATH
    login_button_locator = (By.XPATH, "//button[text()= 'Sign in']")                  #XPATH
    incorrect_credentials_error_locator = (By.XPATH, "//p[@class= 'MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium MuiFormHelperText-contained MuiFormHelperText-filled css-1ju8it0']")     #XPATH

    #Locators of Dashboard page
    new_launch_alert = (By.XPATH, "//button[@aria-label = 'Close popup']")           #XPATH
    download_app_button = (By.XPATH,"//button[@class='download-app-button']")        #XPATH
    profile_name_locator = (By.CLASS_NAME,"user-name-div")                           #CLASS NAME
    logout_button_locator = (By.XPATH,"//div[text() = 'Log out']")                   #XPATH



