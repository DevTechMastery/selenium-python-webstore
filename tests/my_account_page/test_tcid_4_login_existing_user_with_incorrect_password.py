import pytest
from myStoreWebUI.src.pages.AccountSignedOut import AccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginExistingUserWithIncorrectPassword:
    # Test case for login with existing user but incorrect password
    @pytest.mark.tcid4
    @pytest.mark.my_account
    @pytest.mark.regression
    def test_login_existing_user_with_incorrect_password(self):
        print("*******")
        print("TEST LOGIN EXISTING USER WITH INCORRECT PASSWORD")
        print("*******")

        # Create an instance of AccountSignedOut
        my_account = AccountSignedOut(self.driver)

        # Navigate to the account page
        my_account.go_to_my_account()

        # Input username and password for login
        my_account.input_login_username('user101@gmail.com')
        my_account.input_login_password('incorrect_password')

        # Click the login button
        my_account.click_login_button()

        # Verify the error message for incorrect password
        expected_err = (' The password you entered for the email address')
        my_account.wait_until_error_is_displayed(expected_err)