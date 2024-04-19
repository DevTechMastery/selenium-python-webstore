from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from myStoreWebUI.src.helpers.generic_helpers import generate_random_email_and_password

class CheckoutPage(CheckoutPageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self,first_name="TestFirstName"):
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)


    def input_billing_last_name(self,last_name="TestLastName"):
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_address(self,address="TestAddress"):
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_FIELD, address)

    def input_billing_apartment(self,apartment="TestApartment"):
        self.sl.wait_and_input_text(self.BILLING_APARTMENT_FIELD, apartment)

    def input_billing_city(self,city="TestCity"):
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zip(self,zip="12345"):
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip)

    def input_billing_phone(self,phone="1234567890"):
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    def input_billing_email(self,email=None):
        if not email:
            email = generate_random_email_and_password()['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    # hard coded values for now, can be parameterized, but for now, we will keep it simple
    def fill_in_billing_details(self, first_name="TestFirstName", last_name="TestLastName", address="TestAddress",
                                apartment="TestApartment", city="TestCity", zip="12345", phone="1234567890",
                                email=None):
        self.input_billing_first_name(first_name if first_name is not None else "TestFirstName")
        self.input_billing_last_name(last_name if last_name is not None else "TestLastName")
        self.input_billing_address(address if address is not None else "TestAddress")
        self.input_billing_apartment(apartment if apartment is not None else "TestApartment")
        self.input_billing_city(city if city is not None else "TestCity")
        self.input_billing_zip(zip if zip is not None else "12345")
        self.input_billing_phone(phone if phone is not None else "1234567890")
        self.input_billing_email(email)

    def click_place_order_button(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)









