from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.pages.locators.HeaderLocators import HeaderLocators


class Header(HeaderLocators):
    # Constructor for the Header class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to click on the cart on the right header
    def click_on_cart_on_right_header(self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER)

    # Method to wait until the cart item count matches the expected count
    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)


