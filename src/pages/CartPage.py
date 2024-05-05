from myStoreWebUI.src.pages.locators.CartPageLocators import CartPagesLocators
from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.helpers.config_helpers import get_base_url
import logging as logger


class CartPage(CartPagesLocators):
    # end of cart page
    endpoint = '/cart/'

    # Constructor for the CartPage class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to navigate to the cart page
    def go_to_cart_page(self):
        base_url = get_base_url()
        cart_page_url = base_url + self.endpoint
        logger.info(f"Going to: {cart_page_url}")
        self.driver.get(cart_page_url)

    # Method to get all product names in the cart
    def get_all_product_names_in_cart(self):
        # Wait for the product name elements to be present and get them
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        # Extract the text from each product name element and return them as a list
        product_names = [i.text for i in product_name_elements]
        return product_names

    # Method to click the link to add a coupon
    def click_link_add_coupon(self):
        # Wait for the link apply coupon to be present and click it
        self.sl.wait_and_click(self.LINK_ADD_COUPON)

    # Method to input a coupon code
    def input_coupon_code(self, coupon_code):
        # Wait for the coupon code input field to be present and enter the coupon code
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)

    #
    def click_button_apply_coupon(self):
        # Wait for the apply coupon button to be present and click it
        self.sl.wait_and_click(self.APPLY_COUPON_BUTTON)

    # Method to apply a coupon to the cart
    def apply_coupon(self, coupon_code):
        # Click on the link to add a coupon
        self.click_link_add_coupon()
        # Input the coupon code
        self.input_coupon_code(coupon_code)
        # Click the apply coupon button
        self.click_button_apply_coupon()
        # Get the displayed coupon message
        success_message = self.get_displayed_coupon_message()
        # Assert that the coupon applied message is displayed
        assert 'Coupon code "FRIENDS100" has been applied to your cart.' in success_message, f'Expected coupon applied message not found. Found: {success_message}'

    # Method to get the displayed coupon message
    def get_displayed_coupon_message(self):
        return self.sl.wait_and_get_text(self.COUPON_APPLIED_BANNER)

    # Method to click the proceed to checkout button
    def click_proceed_to_checkout_button(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BUTTON)

    # Method to click the "+" button to add items to the cart
    def click_plus_button(self, count):
        for i in range(count):
            self.sl.wait_and_click(self.PLUS_ITEM_BUTTON)


    # Method to click the "-" button to remove items from the cart
    def click_minus_button(self, count):
        for i in range(count):
            self.sl.wait_and_click(self.MINUS_ITEM_BUTTON)

    # Method to verify the number of items in the cart
    def verify_item_count_in_cart(self, count):
        # Wait for the cart item element to be present and get it
        cart_item_elements = self.sl.wait_and_get_elements(self.CART_ITEMS)
        # Get the value attribute of each cart item element and convert it to an integer
        actual_counts = [int(element.get_attribute('value')) for element in cart_item_elements]
        # Assert that the sum of actual counts is equal to the expected count
        assert sum(actual_counts) == count, f'Expected {count} items in cart. Found {sum(actual_counts)} items.'

    # Method to click the "Remove item" button to remove an item from the cart
    def click_remove_item_button(self):
        # Wait for the remove item button to be present and click it
        self.sl.wait_and_click(self.REMOVE_ITEM_BUTTON)

    # Method to verify that the cart is empty as text is displayed "Your cart is currently empty!"
    def verify_cart_is_empty(self):
        # Wait for the empty cart message to be present and get it
        empty_cart_message = self.sl.wait_and_get_text(self.EMPTY_CART_MESSAGE)
        # Assert that the empty cart message is displayed
        assert 'Your cart is currently empty!' in empty_cart_message, f'Expected empty cart message not found. Found: {empty_cart_message}'

    # Method to verify the total price of items in the cart
    def verify_total_price_of_items_in_cart(self, count):
        # Get the total price of the items in the cart
        total_price = self.sl.wait_and_get_text(self.TOTAL_PRICE)
        # Get the price of a single item
        single_item_price = self.sl.wait_and_get_text(self.SINGLE_ITEM_PRICE)
        # Remove the dollar sign and convert the prices to float
        total_price = float(total_price.replace('$', ''))
        single_item_price = float(single_item_price.replace('$', ''))
        # Calculate the expected total price
        expected_total_price = single_item_price * count
        # Assert that the total price is correct
        assert total_price == expected_total_price, f'Expected total price of {expected_total_price}. Found {total_price}'






