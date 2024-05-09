import pytest
import time
from myStoreWebUI.src.pages.HomePage import HomePage
from myStoreWebUI.src.pages.Header import Header
from myStoreWebUI.src.pages.CartPage import CartPage
from myStoreWebUI.src.pages.CheckoutPage import CheckoutPage
from myStoreWebUI.src.pages.OrderReceivedPage import OrderReceivedPage


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:
    # Test case for end-to-end checkout by a guest user
    @pytest.mark.tcid28
    @pytest.mark.end_to_end
    @pytest.mark.regression
    def test_end_to_end_checkout_guest_user(self):
        # Create instances of HomePage, Header, CartPage, CheckoutPage and OrderReceivedPage
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)

        # Navigate to home page
        home_p.go_to_home_page()

        # Add 1 item to cart
        home_p.click_first_add_to_cart_button()

        # Make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)

        # Navigate to cart
        header.click_on_cart_on_right_header()

        # SKIP - Verify expected item in cart
        # product_names = cart_p.get_all_product_names_in_cart()
        # assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        # Click on checkout
        cart_p.click_proceed_to_checkout_button()

        # Fill in form details for guest user
        checkout_p.fill_in_billing_details()

        # note: the following sleep is added to help with debugging as the page transitions are too fast and issue to click place order button
        # Fill in requires time to load the page before clicking on the place order button
        time.sleep(2)

        # Click on place order button
        checkout_p.click_place_order_button()

        # Verify order is received
        order_received_p.verify_order_received_page_loaded()
