from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from myStoreWebUI.src.helpers.generic_helpers import generate_random_email_and_password, DataGenerator

class CheckoutPage(CheckoutPageLocators):
    # Constructor for the CheckoutPage class
    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.data_gen = DataGenerator() # Create an instance of the DataGenerator class

    # Method to input billing first name
    def input_billing_first_name(self, first_name=None):
        if not first_name:
            first_name = self.data_gen.generate_first_name()
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    # Method to input billing last name
    def input_billing_last_name(self, last_name=None):
        if not last_name:
            last_name = self.data_gen.generate_last_name()
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    # Method to input billing address
    def input_billing_address(self, address=None):
        if not address:
            address = self.data_gen.generate_address()
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_FIELD, address)

    # Method to input billing apartment
    def input_billing_apartment(self, apartment=None):
        if not apartment:
            apartment = self.data_gen.generate_apartment()
        self.sl.wait_and_input_text(self.BILLING_APARTMENT_FIELD, apartment)

    # Method to input billing city
    def input_billing_city(self, city=None):
        if not city:
            city = self.data_gen.generate_city()
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    # Method to input billing zip
    def input_billing_zip(self, zip=None):
        if not zip:
            zip = self.data_gen.generate_zipcode()
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip)

    # Method to input billing phone
    def input_billing_phone(self, phone=None):
        if not phone:
            phone = self.data_gen.generate_phone()
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    # Method to input billing email
    def input_billing_email(self, email=None):
        if not email:
            email = generate_random_email_and_password()['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    # Method to fill in billing details
    def fill_in_billing_details(self):
        self.input_billing_email()
        self.input_billing_first_name()
        self.input_billing_last_name()
        self.input_billing_address()
        self.input_billing_apartment()
        self.input_billing_city()
        self.input_billing_zip()
        self.input_billing_phone()

    # Method to fill in billing details for an existing user
    def fill_in_billing_details_existing_user(self):
        # No need to input email for existing user as it is already filled in the form by default in the checkout page
        self.input_billing_first_name('John')
        self.input_billing_last_name('Doe')
        self.input_billing_address('123 Main St')
        self.input_billing_apartment('Apt 1')
        self.input_billing_city('Los Angeles')
        self.input_billing_zip('90001')
        self.input_billing_phone('5234567890')

    # Method to click on the place order button
    def click_place_order_button(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)