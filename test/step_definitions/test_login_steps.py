import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from pages.dashboard_page import DashBoardPage
from pages.login_page import LoginPage
from utility.capture_screenshot import CaptureScreenshot

# Defining the feature file to execute
scenarios("login.feature")


# Set up the fixture to create LoginPage object to use in the test steps
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


# Set up the fixture to create DashBoardPage object to use in the test steps
@pytest.fixture
def dashboard_page(driver):
    return DashBoardPage(driver)


# Set up the fixture to create capture screens object to use in the test steps
@pytest.fixture
def take_screenshot(driver):
    return CaptureScreenshot(driver)


# Step definition for 'As a user I launch the Zenclass webportal'
# Since driver fixture will take care of launching the browser and navigate to the application
# Hence only the page title is validated
@given('As a user I launch the Zenclass webportal')
def launch_application(driver):
    print(driver.title)
    assert driver.title == "GUVI", "Zenclass webportal is not launched"


# Step definition to fill in the username, password and click on Sign in button
@when(parsers.cfparse('I login with username "{username}" and password "{password}"'))
def login_with_credentials(login_page, take_screenshot, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    take_screenshot.capture_screenshot("Login_screen")


# Validates login success for valid credentials
@then(parsers.cfparse('Logged in successfully to the "{page_title}" page'))
def validate_login_success(dashboard_page, take_screenshot, page_title):
    dashboard_page.handle_new_launch_alert()
    print(dashboard_page.get_download_app_button())
    take_screenshot.capture_screenshot("Dashboard_screen")
    assert dashboard_page.get_download_app_button() == page_title, "Login failed, Dashboard not loaded"


# Validates logout is success
@then(parsers.cfparse('I should be able to logout successfully and "{sign_in_button}" is available again'))
def validate_logout_is_success(login_page, take_screenshot, dashboard_page, sign_in_button):
    dashboard_page.click_user_profile()
    dashboard_page.click_logout_button()

    # Validates logout button works fine
    assert login_page.get_sign_in_button_text() == sign_in_button, "Logout failed, Sign in button is not shown"
    take_screenshot.capture_screenshot("Logout_success")


# Validates unsuccessful login, by verifying username and password fields throws error for invalid input
@then(parsers.cfparse('login should fail with error message {error_message}'))
def validate_error_message(login_page, take_screenshot, error_message):
    actual_error = login_page.get_incorrect_credential_error_text()
    assert actual_error == error_message, "Invalid error message is shown"
    take_screenshot.capture_screenshot("Login_error")
