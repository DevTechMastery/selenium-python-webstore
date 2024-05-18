import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage

@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyDescriptionHeader:
    # Test case for verifying the description header of a product
    @pytest.mark.tcid16
    @pytest.mark.product_page
    @pytest.mark.regression
    def test_verify_description_header(self):
        print("*******")
        print("TEST VERIFY DESCRIPTION HEADER")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the product description header
        expected_desc_header = 'Description'
        product_detail.verify_product_description_header(expected_desc_header)