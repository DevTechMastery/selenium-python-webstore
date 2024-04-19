from selenium.webdriver.common.by import By


class CartPagesLocators:
    pass

    # TBD - Add locators for Cart page
    # PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, '')

    LINK_ADD_COUPON = (By.CSS_SELECTOR, 'a.wc-block-components-totals-coupon-link')
    COUPON_FIELD = (By.ID, 'wc-block-components-totals-coupon__input-0')
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR,'button.wc-block-components-totals-coupon__button')

    COUPON_APPLIED_BANNER = (By.CLASS_NAME, 'wc-block-components-notice-banner__content')
