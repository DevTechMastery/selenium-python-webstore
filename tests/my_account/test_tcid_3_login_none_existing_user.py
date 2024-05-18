import pytest
from myStoreWebUI.src.pages.AccountSignedOut import AccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginNoneExistingUser:
    # Test case for login with non-existing user
    @pytest.mark.tcid3
    @pytest.mark.my_account
    @pytest.mark.regression
    def test_login_none_existing_user(self):
        print("*******")
        print("TEST LOGIN NON EXISTING USER")
        print("*******")

        # Create an instance of AccountSignedOut
        my_account = AccountSignedOut(self.driver)

        # Navigate to the account page
        my_account.go_to_my_account()

        # Input username and password for login
        my_account.input_login_username("adfjladkf")
        my_account.input_login_password("adfadfadf")

        # Click the login button
        my_account.click_login_button()

        # Verify the error message for non-existing user
        expected_err = "is not registered on this site. If you are unsure of your username"
        my_account.wait_until_error_is_displayed(expected_err)
