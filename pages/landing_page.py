from pages.base_page import BasePage
from utils.locators import LandingPageLocators

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.flipkart.com"

    def load(self):
        self.driver.get(self.url)

    def close_login_popup(self):
        if self.is_visible(LandingPageLocators.LOGIN_POPUP_CLOSE):
            self.click(LandingPageLocators.LOGIN_POPUP_CLOSE)

    def search_for_product(self, product_name):
        self.send_keys(LandingPageLocators.SEARCH_INPUT, product_name)
        # Using return key for search submission
        from selenium.webdriver.common.keys import Keys
        self.find_element(LandingPageLocators.SEARCH_INPUT).send_keys(Keys.ENTER)

    def click_mobiles_category(self):
        self.click(LandingPageLocators.MOBILES_CATEGORY)

    def is_logo_visible(self):
        return self.is_visible(LandingPageLocators.LOGO)

    def click_cart(self):
        self.click(LandingPageLocators.CART_BUTTON)

    def click_login(self):
        self.click(LandingPageLocators.LOGIN_BUTTON)
