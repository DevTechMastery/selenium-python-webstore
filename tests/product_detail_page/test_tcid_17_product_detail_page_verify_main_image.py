import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage

@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyMainImage:
    # Test case for verifying the main image of a product
    @pytest.mark.tcid17
    @pytest.mark.product_page
    @pytest.mark.regression
    def test_verify_main_image(self):
        print("*******")
        print("TEST VERIFY MAIN IMAGE")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the main image of the product
        expected_main_image = '/album-1-1-416x416.jpg'
        product_detail.verify_main_image(expected_main_image)
