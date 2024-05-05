from myStoreWebUI.src.pages.locators.AccountSignedOutLocators import AccountSignedOutLocators
from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.helpers.config_helpers import get_base_url
import logging as logger


class AccountSignedOut(AccountSignedOutLocators):
    # end of web page account
    endpoint = '/my-account/'

    # Constructor for the AccountSignedOut class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to navigate to the account page
    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    # Method to input username for login
    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    # Method to input password for login
    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    # Method to click the login button
    def click_login_button(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN)

    # Method to wait and verify the error message is displayed
    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    # Method to input email for registration
    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    # Method to input password for registration
    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    # Method to click the register button
    def click_register_button(self):
        logger.debug("Clicking 'Register' button.")
        self.sl.wait_and_click(self.REGISTER_BTN)
