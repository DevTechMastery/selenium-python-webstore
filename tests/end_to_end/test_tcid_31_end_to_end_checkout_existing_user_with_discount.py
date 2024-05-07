import pytest
from myStoreWebUI.src.pages.AccountSignedOut import AccountSignedOut
from myStoreWebUI.src.pages.HomePage import HomePage
from myStoreWebUI.src.pages.Header import Header
from myStoreWebUI.src.pages.CartPage import CartPage
from myStoreWebUI.src.pages.CheckoutPage import CheckoutPage
from myStoreWebUI.src.pages.OrderReceivedPage import OrderReceivedPage
from myStoreWebUI.src.configs.generic_configs import GenericConfigs

import time

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutExistingUserWithDiscount:
    # Test case for end-to-end checkout by a registered user with discount (free coupon)
    @pytest.mark.tcid31
    @pytest.mark.end_to_end
    @pytest.mark.regression
    def test_end_to_end_checkout_existing_user_with_discount(self):
        # Create instances of AccountSignedOut, HomePage, Header, CartPage, CheckoutPage and OrderReceivedPage
        my_account_o = AccountSignedOut(self.driver)
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)

        # Navigate to the account page
        my_account_o.go_to_my_account()

        # Input username and password for login
        my_account_o.input_login_username('user101@gmail.com')
        my_account_o.input_login_password('1234abc111@')

        # Click the login button
        my_account_o.click_login_button()

        # Click on the home page
        header.click_on_home_on_left_header()

        # Add 1 item to cart
        home_p.click_first_add_to_cart_button()

        # Make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)

        # Navigate to cart
        header.click_on_cart_on_right_header()

        # SKIP - Verify expected item in cart
        # product_names = cart_p.get_all_product_names_in_cart()
        # assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        # Apply free coupon
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        # Click on checkout
        cart_p.click_proceed_to_checkout_button()

        # Fill in form
        checkout_p.fill_in_billing_details_existing_user()

        # note: the following sleep is added to help with debugging as the page transitions are too fast and issue to click place order button
        time.sleep(2)

        # Click on place order button
        checkout_p.click_place_order_button()

        # Verify order is received
        order_received_p.verify_order_received_page_loaded()