import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage


@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyAddToCartBtnDisplayed:
    # Test case for verifying the Add to Cart button is displayed
    @pytest.mark.tcid10
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_add_to_cart_btn_displayed(self):
        print("*******")
        print("TEST VERIFY ADD TO CART BUTTON DISPLAYED")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the Add to Cart button is displayed
        product_detail.verify_add_to_cart_btn_displayed()