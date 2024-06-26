from selenium.webdriver.common.by import By

class ProductDetailPageLocators:

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')

    CATEGORY = (By.CSS_SELECTOR, 'span.posted_in a')

    DESCRIPTION = (By.XPATH, "//p[contains(text(), 'Lorem ipsum dolor sit amet')]")

    DESCRIPTION_HEADER = (By.XPATH, "//h2[text()='Description']")

    MAIN_IMAGE = (By.CSS_SELECTOR, 'img.wp-post-image')

    PRICE = (By.CSS_SELECTOR, 'p.price > span.woocommerce-Price-amount.amount')

    NAME = (By.CSS_SELECTOR, 'h1.product_title.entry-title')

    SKU = (By.CSS_SELECTOR, 'span.sku_wrapper > span.sku')


