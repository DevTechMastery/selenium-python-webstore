from myStoreWebUI.src.pages.locators.AccountSignedInLocators import AccountSignedInLocators
from myStoreWebUI.src.SeleniumExtended import SeleniumExtended

class AccountSignedIn(AccountSignedInLocators):
    # Constructor for the AccountSignedIn class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to verify if the user is signed in
    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)