from selenium.webdriver.common.by import By

class LandingPageLocators:
    LOGO = (By.CSS_SELECTOR, 'img[title="Flipkart"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[title="Search for Products, Brands and More"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[title="Login"]')
    CART_BUTTON = (By.CSS_SELECTOR, 'a[title="Cart"]')
    MOBILES_CATEGORY = (By.CSS_SELECTOR, 'a[href="/mobile-phone-ab-at-store"]')
    LOGIN_POPUP_CLOSE = (By.XPATH, "//span[@role='button' and text()='✕']")
