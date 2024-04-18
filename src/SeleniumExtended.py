from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select

import time


class SeleniumExtended:
    # Constructor for the SeleniumExtended class
    def __init__(self, driver):
        self.driver = driver  # WebDriver instance
        self.default_timeout = 10  # Default timeout for waiting for elements

    # Method to wait for an element to be visible and then input text
    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    # Method to wait for an element to be clickable and then click it
    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    # Method to wait until an element contains a specific text
    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f'Element with locator = {locator}, does not contain text: "{text}", after waiting {timeout} seconds.'
        )

    # Method to wait until an element is visible
    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        if isinstance(locator_or_element, tuple):
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_or_element)
            )
        else:
            import selenium.webdriver.remote.webelement
            if isinstance(locator_or_element, selenium.webdriver.remote.webelement.WebElement):
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(locator_or_element)
                )
            else:
                raise TypeError(
                    f"The locator to check visibility must be a 'tuple' or a 'WebElement'. It was {type(locator_or_element)}")

        return elem

    # Method to wait until all elements are visible
    def wait_until_elements_are_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

        return elem

    # Method to wait for elements to be visible and then return them
    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by '{locator}'," \
                              f"after timeout of {timeout}"
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return elements

    # Method to wait for an element to be visible and then return its text
    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    # Method to wait until the URL contains a specific substring
    def wait_until_url_contains(self, url_substring, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        elem = WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_substring)
        )

    # Method to wait for a dropdown to be visible and then select an option
    def wait_and_select_dropdown(self, locator, to_select, select_by='visible_text'):
        """

        :param locator:
        :param to_select:
        :param select_by: Options are 'visible_text', 'index', or value 'value'
        :return:
        """

        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(
                f"Invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index', or value 'value'.")
