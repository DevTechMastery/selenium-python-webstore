import pytest
from myStoreWebUI.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")
class TestHomePageSaleBadge:
    # Test case for verifying sale badge is displayed on one of the items
    # Verify the sale badge is displayed on one of the items on the home page
    @pytest.mark.tcid7
    @pytest.mark.regression
    def test_home_page_verify_sale_badge_is_displayed(self):
        # Create an instance of HomePage
        home_p = HomePage(self.driver)

        # Navigate to home page
        home_p.go_to_home_page()

        # Verify sale badge is displayed on one of the items
        home_p.verify_sale_badge_is_displayed()


