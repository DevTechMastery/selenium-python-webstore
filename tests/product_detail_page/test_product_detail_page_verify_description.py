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
        expected_desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis orci ac odio dictum tincidunt. Donec ut metus leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed luctus, dui eu sagittis sodales, nulla nibh sagittis augue, vel porttitor diam enim non metus. Vestibulum aliquam augue neque. Phasellus tincidunt odio eget ullamcorper efficitur. Cras placerat ut turpis pellentesque vulputate. Nam sed consequat tortor. Curabitur finibus sapien dolor. Ut eleifend tellus nec erat pulvinar dignissim. Nam non arcu purus. Vivamus et massa massa.'
        product_detail.verify_product_description(expected_desc)