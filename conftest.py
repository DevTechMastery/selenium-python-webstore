import pytest
from selenium import webdriver
import os


# Define a pytest fixture that initializes a WebDriver instance
# This fixture has a scope of 'class', meaning it's invoked once per test class
@pytest.fixture(scope="class")
def init_driver(request):
    # List of supported browsers
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    # Get the 'BROWSER' environment variable. If it's not set, raise an exception
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    # If the provided browser is not in the list of supported browsers, raise an exception
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    # Initialize a WebDriver instance based on the provided browser
    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()


    # Assign the WebDriver instance to the 'driver' attribute of the test class
    request.cls.driver = driver
    # Yield control back to the test function. After the test function finishes,
    # the rest of this fixture function will be executed
    yield
    # Quit the WebDriver instance, effectively closing the browser
    driver.quit()
