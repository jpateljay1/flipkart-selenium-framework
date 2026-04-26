import pytest
from pages.landing_page import LandingPage

def test_failure_screenshot_capture(driver):
    """This test is designed to fail to verify screenshot capture."""
    landing_page = LandingPage(driver)
    landing_page.load()
    landing_page.close_login_popup()
    
    # Asserting something that is false
    assert False, "Intentional failure to test screenshot capture"
