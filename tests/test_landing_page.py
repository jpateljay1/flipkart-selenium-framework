import pytest
from pages.landing_page import LandingPage

def test_flipkart_landing_page_load(driver):
    landing_page = LandingPage(driver)
    landing_page.load()
    
    # Close login popup if it appears
    landing_page.close_login_popup()
    
    # Verify logo visibility
    assert landing_page.is_logo_visible(), "Flipkart logo is not visible on the landing page"
    
    # Verify title
    assert "Flipkart" in landing_page.get_title(), "Page title does not contain 'Flipkart'"

def test_search_functionality(driver):
    landing_page = LandingPage(driver)
    landing_page.load()
    landing_page.close_login_popup()
    
    product = "iPhone 15"
    landing_page.search_for_product(product)
    
    # Simple check to see if we are on the results page
    assert product in driver.title or "Search" in driver.title

def test_navigate_to_mobiles(driver):
    landing_page = LandingPage(driver)
    landing_page.load()
    landing_page.close_login_popup()
    
    landing_page.click_mobiles_category()
    assert "Mobile" in driver.title
