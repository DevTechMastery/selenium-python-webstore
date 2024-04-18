import pytest
from myStoreWebUI.src.pages.HomePage import HomePage
from myStoreWebUI.src.pages.Header import Header
from myStoreWebUI.src.pages.CartPage import CartPage


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:
    # Test case for end-to-end checkout by a guest user
    @pytest.mark.tcid3
    def test_end_to_end_checkout_guest_user(self):
        # Create instances of HomePage, Header, and CartPage
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

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

        # Apply free coupon


        # Click on checkout
        # Select free shipping
        # Fill in form
        # Click on place order
        # Verify order is received
        # Verify order is recorded in db (vi SQL or via API)
        # These steps are yet to be implemented

