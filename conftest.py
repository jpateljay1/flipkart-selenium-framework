import pytest
import os
import ssl
import undetected_chromedriver as uc
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from utils.logger import logger

# Workaround for SSL certificate verification issue on macOS
if os.name == 'posix':
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

@pytest.fixture(scope="function")
def driver(request):
    logger.info(f"Starting test: {request.node.name}")
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Uncomment for headless execution
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    
    # Adding user-agent to avoid detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    try:
        driver = uc.Chrome(options=chrome_options)
        yield driver
    finally:
        logger.info(f"Finishing test: {request.node.name}")
        if 'driver' in locals():
            driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

    # check if a test failed
    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.fixturenames:
                driver = item.funcargs['driver']
                
                # Create screenshots directory if it doesn't exist
                screenshot_dir = "screenshots"
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)
                
                # Capture screenshot
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_name = f"{item.name}_{timestamp}.png"
                screenshot_path = os.path.join(screenshot_dir, screenshot_name)
                
                driver.save_screenshot(screenshot_path)
                logger.error(f"Test failed. Screenshot saved at: {screenshot_path}")
            else:
                logger.warning("Driver not found in fixture names, cannot take screenshot.")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {str(e)}")
