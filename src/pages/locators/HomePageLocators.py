# Path: src/pages/locators/HeaderLocators.py
from selenium.webdriver.common.by import By


class HomePageLocators:

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a.add_to_cart_button')
    SEARCH_FIELD = (By.ID, 'woocommerce-product-search-field-0')
    SEARCH_RESULT = (By.CLASS_NAME, "woocommerce-result-count")

