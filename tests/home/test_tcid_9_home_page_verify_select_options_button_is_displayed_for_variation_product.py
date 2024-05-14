import pytest
from myStoreWebUI.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")
class TestHomePageOptionsButton:
    # Test case for verifying select options button is displayed for variation product
    # Verify the select options button is displayed for variation product on the home page
    @pytest.mark.tcid9
    @pytest.mark.regression
    def test_home_page_verify_select_options_button_is_displayed_for_variation_product(self):
        # Create an instance of HomePage
        home_p = HomePage(self.driver)

        # Navigate to home page
        home_p.go_to_home_page()

        # Verify select options button is displayed for variation product
        home_p.verify_select_options_button_is_displayed()