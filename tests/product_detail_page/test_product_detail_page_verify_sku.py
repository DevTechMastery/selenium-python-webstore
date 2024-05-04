# import pytest
# from myStoreWebUI.src.pages.ProductDetailPage import ProductDetailPage
#
#
# @pytest.mark.usefixtures("init_driver")
# class TestProductDetailPageVerifySku:
#     # Test case for verifying the SKU of a product
#     @pytest.mark.tcid17
#     @pytest.mark.smoke
#     @pytest.mark.regression
#     def test_verify_sku(self):
#         print("*******")
#         print("TEST VERIFY SKU")
#         print("*******")
#
#         # Create an instance of ProductDetailPage
#         product_detail = ProductDetailPage(self.driver)
#
#         # Navigate to the product detail page
#         product_detail.go_to_product_detail_page()
#
#         # Verify the SKU of the product
#         expected_sku = 'SKU: woo-album'
#         product_detail.verify_sku(expected_sku)