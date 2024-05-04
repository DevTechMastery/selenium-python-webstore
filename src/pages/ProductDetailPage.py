from myStoreWebUI.src.pages.locators.ProductDetailPageLocators import ProductDetailPageLocators
from myStoreWebUI.src.SeleniumExtended import SeleniumExtended
from myStoreWebUI.src.helpers.config_helpers import get_base_url

class ProductDetailPage(ProductDetailPageLocators):
    # end of web page account
    endpoint = '/product/album/'

    # Constructor for the ProductDetailPage class
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # Method to navigate to the product page
    def go_to_product_detail_page(self):
        base_url = get_base_url()
        product_url = base_url + self.endpoint
        self.driver.get(product_url)

    # Method to verify the Add to Cart button is displayed
    def verify_add_to_cart_btn_displayed(self):
        self.sl.wait_until_element_is_visible(ProductDetailPageLocators.ADD_TO_CART_BTN)
        assert self.sl.is_element_displayed(ProductDetailPageLocators.ADD_TO_CART_BTN)

    # Method to verify the category of the product
    def verify_category(self, expected_category):
        category = self.sl.wait_and_get_text(ProductDetailPageLocators.CATEGORY)
        assert category == expected_category

    # Method to verify the product description
    def verify_product_description(self, expected_desc):
        desc = self.sl.wait_and_get_text(ProductDetailPageLocators.DESCRIPTION)
        assert desc == expected_desc

    # Method to verify the product description header
    def verify_product_description_header(self, expected_desc_header):
        desc_header = self.sl.wait_and_get_text(ProductDetailPageLocators.DESCRIPTION_HEADER)
        assert desc_header == expected_desc_header

    # Method to verify the main image of the product
    def verify_main_image(self, expected_main_image):
        main_image = self.sl.wait_and_get_attribute(ProductDetailPageLocators.MAIN_IMAGE, 'src')
        assert  main_image.endswith(expected_main_image), f"Expected image {expected_main_image} not found in {main_image}"

    # Method to verify the price of the product
    def verify_price(self, expected_price):
        price = self.sl.wait_and_get_text(ProductDetailPageLocators.PRICE)
        assert price == expected_price, f"Expected price {expected_price} not found in {price}"

    # Method to verify the product name
    def verify_product_name(self, expected_name):
        name = self.sl.wait_and_get_text(ProductDetailPageLocators.NAME)
        assert name == expected_name, f"Expected name {expected_name} not found in {name}"

    # Method to verify the SKU of the product
    def verify_sku(self, expected_sku):
        sku = self.sl.wait_and_get_text(ProductDetailPageLocators.SKU)
        assert sku == expected_sku, f"Expected SKU {expected_sku} not found in {sku}"

