from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        logger.info(f"Finding element: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logger.error(f"Element not found: {locator}. Error: {str(e)}")
            raise

    def click(self, locator):
        logger.info(f"Clicking on element: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            logger.error(f"Failed to click on element: {locator}. Error: {str(e)}")
            raise

    def send_keys(self, locator, text):
        logger.info(f"Sending keys '{text}' to element: {locator}")
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            logger.error(f"Failed to send keys to element: {locator}. Error: {str(e)}")
            raise

    def is_visible(self, locator):
        logger.info(f"Checking visibility of element: {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            logger.warning(f"Element not visible: {locator}")
            return False

    def get_title(self):
        title = self.driver.title
        logger.info(f"Page title is: {title}")
        return title
