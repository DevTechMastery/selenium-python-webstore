import pytest
from myStoreWebUI.src.pages.AccountSignedOut import AccountSignedOut
from myStoreWebUI.src.pages.AccountSignedIn import AccountSignedIn

@pytest.mark.usefixtures("init_driver")
class TestLoginExistingUser:
    # Test case for login with existing user
    @pytest.mark.tcid2
    @pytest.mark.my_account
    @pytest.mark.regression
    def test_login_existing_user(self):
        print("*******")
        print("TEST LOGIN WITH EXISTING USER")
        print("*******")

        # Create an instance of AccountSignedOut
        my_account_o = AccountSignedOut(self.driver)
        my_account_i = AccountSignedIn(self.driver)

        # Navigate to the account page
        my_account_o.go_to_my_account()

        # Input username and password for login
        my_account_o.input_login_username('user101@gmail.com')
        my_account_o.input_login_password('1234abc111@')

        # Click the login button
        my_account_o.click_login_button()

        # Verify the user is signed in
        my_account_i.verify_user_is_signed_in()

