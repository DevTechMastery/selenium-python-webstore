import pytest
from myStoreWebUI.src.pages.AccountSignedOut import AccountSignedOut
from myStoreWebUI.src.pages.AccountSignedIn import AccountSignedIn
from myStoreWebUI.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    # Test case for registering a new user
    @pytest.mark.tcid1
    def test_register_valid_new_user(self):
        # Create instances of AccountSignedOut and AccountSignedIn
        my_account_o = AccountSignedOut(self.driver)
        my_account_i = AccountSignedIn(self.driver)

        # Navigate to the account page
        my_account_o.go_to_my_account()

        # Generate random email and password
        rand_email = generate_random_email_and_password()

        # Input the generated email and password for registration
        my_account_o.input_register_email(rand_email["email"])
        my_account_o.input_register_password('1234abc111@')

        # Click the register button
        my_account_o.click_register_button()

        # Verify that the user is registered and signed in
        my_account_i.verify_user_is_signed_in()

