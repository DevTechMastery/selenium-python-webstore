
import random
import string
import logging as logger
from html.parser import HTMLParser


# Function to generate a random email and password
def generate_random_email_and_password(domain=None, email_prefix=None):
    # If no domain is provided, use 'happyharbor.com' as the default domain
    if not domain:
        domain = 'happyharbor.com'
    # If no email prefix is provided, use 'testuser' as the default prefix
    if not email_prefix:
        email_prefix = 'testuser'

    # Generate a random string of 10 lowercase letters
    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    # Construct the email using the prefix, random string, and domain
    email = email_prefix + '_' + random_string + '@' + domain

    # Log the generated email
    logger.info(f"Generated random email: {email}")

    # Generate a random password of 20 letters (both lowercase and uppercase)
    rand_psswd_length = 20
    rand_password = ''.join(random.choices(string.ascii_letters, k=rand_psswd_length))

    # Return the generated email and password as a dictionary
    random_info = {"email": email, "password": rand_password}
    return  random_info

# Function to convert HTML to plain text
def convert_html_to_text(input_html_string):
    # Define a class used to convert HTML to text
    class HTMLFilter(HTMLParser):
        text = ""

        # Method to handle the data in the HTML
        # This method is called when the parser encounters raw data
        def handle_data(self, data):
            self.text += data

    # Create an instance of the HTMLFilter class
    f = HTMLFilter()
    # Feed the HTML string to the parser
    f.feed(input_html_string)
    # Return the text attribute of the HTMLFilter instance
    return f.text
