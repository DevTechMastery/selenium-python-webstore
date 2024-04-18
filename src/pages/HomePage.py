from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.helpers.config_helpers import get_base_url
from myStoreWebUI.src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):
    # Constructor for the HomePage class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to navigate to the home page
    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    # Method to click the first product on the home page to add to cart
    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)