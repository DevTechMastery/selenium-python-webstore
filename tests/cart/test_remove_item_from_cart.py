import pytest
from myStoreWebUI.src.pages.HomePage import HomePage
from myStoreWebUI.src.pages.Header import Header
from myStoreWebUI.src.pages.CartPage import CartPage

@pytest.mark.usefixtures('init_driver')
class TestRemoveItemFromCart:
    # Test case for removing an item from the cart
    @pytest.mark.tcid5
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_remove_item_from_cart(self):
        # Create instances of HomePage, CartPage
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

        # Click "+" button to add 4 more items to cart
        cart_p.click_plus_button(4)

        # Verify 5 items in cart
        cart_p.verify_item_count_in_cart(5)

        # Click "-" button to remove 4 items from cart
        cart_p.click_minus_button(4)

        # Click "Remove item" button to remove 1 item from cart
        cart_p.click_remove_item_button()

        # Verify that the cart is empty
        cart_p.verify_cart_is_empty()



