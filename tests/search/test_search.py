import pytest
from myStoreWebUI.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")
class TestSearch:
    # Test case for searching an item
    # Verify the search functionality on the home page by searching for an item and verifying the search results.
    @pytest.mark.tcid4
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_item(self):
        # Create an instance of HomePage
        home_p = HomePage(self.driver)

        # Navigate to home page
        home_p.go_to_home_page()

        # Search 1 item
        home_p.search_item('T-shirt')

        # Verify an item is displayed in the search result page
        expected_result = ('Showing all 3 results')
        home_p.get_search_result(expected_result)






