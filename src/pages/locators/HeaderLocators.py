from selenium.webdriver.common.by import By


class HeaderLocators:
    HOME_LEFT_HEADER = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[1]/a')

    CART_RIGHT_HEADER = (By.ID, 'site-header-cart')
    CART_ITEM_COUNT = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')
    MENU_ITEMS = (By.CSS_SELECTOR, 'div.menu ul.nav-menu li')
