from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.pages.locators.CartPageLocators import CartPagesLocators


class CartPage(CartPagesLocators):
    # Constructor for the CartPage class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to navigate to the cart page
    # Currently, this method is not implemented
    def go_to_cart_page(self):
        pass

    # Method to get all product names in the cart
    def get_all_product_names_in_cart(self):
        # Wait for the product name elements to be present and get them
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        # Extract the text from each product name element and return them as a list
        product_names = [i.text for i in product_name_elements]
        return product_names
