from selenium.webdriver.common.by import By


class CartPagesLocators:
    # TBD - Add locators for Cart page
    # PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, '')

    LINK_ADD_COUPON = (By.CSS_SELECTOR, 'a.wc-block-components-totals-coupon-link')
    COUPON_FIELD = (By.ID, 'wc-block-components-totals-coupon__input-0')
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR,'button.wc-block-components-totals-coupon__button')
    COUPON_APPLIED_BANNER = (By.CLASS_NAME, 'wc-block-components-notice-banner__content')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'a.components-button')
    PLUS_ITEM_BUTTON = (By.CSS_SELECTOR, 'button.wc-block-components-quantity-selector__button--plus')
    MINUS_ITEM_BUTTON = (By.CSS_SELECTOR, 'button.wc-block-components-quantity-selector__button--minus')
    CART_ITEMS = (By.CSS_SELECTOR, 'input.wc-block-components-quantity-selector__input')
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, 'button.wc-block-cart-item__remove-link')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'h2.wc-block-cart__empty-cart__title')
    TOTAL_PRICE = (By.CSS_SELECTOR, 'span.wc-block-components-totals-item__value')
    SINGLE_ITEM_PRICE = (By.CSS_SELECTOR, 'span.wc-block-components-product-price__value')
