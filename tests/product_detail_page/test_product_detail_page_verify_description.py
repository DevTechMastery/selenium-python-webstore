import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage


@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyDescription:
    # Test case for verifying the description of a product
    @pytest.mark.tcid12
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_description(self):
        print("*******")
        print("TEST VERIFY DESCRIPTION")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the product description
        expected_desc = 'Short description about the product'
        product_detail.verify_product_description(expected_desc)