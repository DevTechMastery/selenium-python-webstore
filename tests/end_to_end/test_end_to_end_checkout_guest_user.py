import pytest
from myStoreWebUI.src.pages.HomePage import HomePage
from myStoreWebUI.src.pages.Header import Header
from myStoreWebUI.src.pages.CartPage import CartPage
from myStoreWebUI.src.configs.generic_configs import GenericConfigs


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
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        # Click on checkout
        cart_p.click_proceed_to_checkout_button()

        # TBD- Complete the end-to-end test
        # Fill in form
        # Click on place order
        # Verify order is received
        # Verify order is recorded in db (vi SQL or via API)


        import pdb;
        pdb.set_trace()