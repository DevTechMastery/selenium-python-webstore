import pytest
from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage


@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVerifyCategory:
    # Test case to verify the category of the product
    @pytest.mark.tcid11
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_category(self):
        print("*******")
        print("TEST VERIFY CATEGORY")
        print("*******")

        # Create an instance of ProductDetailPage
        product_detail = ProductDetailPage(self.driver)

        # Navigate to the product detail page
        product_detail.go_to_product_detail_page()

        # Verify the category of the product
        expected_category = 'Music'
        product_detail.verify_category(expected_category)
