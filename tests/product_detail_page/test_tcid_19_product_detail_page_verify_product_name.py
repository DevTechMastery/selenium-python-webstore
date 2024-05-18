import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage

@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyProductName:
    # Test case for verifying the name of a product
    @pytest.mark.tcid19
    @pytest.mark.product_page
    @pytest.mark.regression
    def test_verify_product_name(self):
        print("*******")
        print("TEST VERIFY PRODUCT NAME")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the product name
        expected_name = 'Album'
        product_detail.verify_product_name(expected_name)