import pytest
from myStoreWebUI.src.pages.HomePage import HomePage
from myStoreWebUI.src.pages.Header import Header
from myStoreWebUI.src.pages.CartPage import CartPage

@pytest.mark.usefixtures('init_driver')
class TestUpdateItemQuantityInCart:
    # Test case for updating the quantity of an item in the cart and verify if the cart updates with the correct total price
    @pytest.mark.tcid6
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_update_item_quantity_in_cart(self):
        # Create instances of HomePage, CartPage
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

        # Navigate to home page
        home_p.go_to_home_page()

        # Add 1 item to cart
        home_p.click_first_add_to_cart_button()

        # Navigate to cart
        header.click_on_cart_on_right_header()

        # Click "+" button to add 4 more items to cart
        cart_p.click_plus_button(4)

        # Verify 5 items in cart
        cart_p.verify_item_count_in_cart(5)

        # Click "-" button to remove 2 items from cart
        cart_p.click_minus_button(2)

        # Verify 3 items in cart
        cart_p.verify_item_count_in_cart(3)

        # Click "+" button to add 2 more items to cart
        cart_p.click_plus_button(2)

        # Verify 5 items in cart
        cart_p.verify_item_count_in_cart(5)

        # Verify total price
        cart_p.verify_total_price_of_items_in_cart(5)
