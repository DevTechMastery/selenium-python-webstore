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




