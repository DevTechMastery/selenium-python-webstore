import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage


@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyPrice:
    # Test case for verifying the price of a product
    @pytest.mark.tcid15
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_price(self):
        print("*******")
        print("TEST VERIFY PRICE")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the price of the product
        expected_price = '$15.00'
        product_detail.verify_price(expected_price)