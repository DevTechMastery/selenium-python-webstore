import pytest
from myStoreWebUI.src.pages.AccountSignedOut import AccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginUsernameFieldIsEmpty:
    # Test case for login with empty password field
    @pytest.mark.tcid6
    @pytest.mark.my_account
    @pytest.mark.regression
    def test_login_username_field_is_empty(self):
        print("*******")
        print("TEST LOGIN PASSWORD FIELD IS EMPTY")
        print("*******")

        # Create an instance of AccountSignedOut
        my_account = AccountSignedOut(self.driver)

        # Navigate to the account page
        my_account.go_to_my_account()

        # Input username and password for login
        my_account.input_login_username('user101@gmail.com')
        my_account.input_login_password('')

        # Click the login button
        my_account.click_login_button()

        # Verify the error message for incorrect password
        expected_err = "The password field is empty."
        my_account.wait_until_error_is_displayed(expected_err)
