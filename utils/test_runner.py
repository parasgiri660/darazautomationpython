# Import webdriver module to control browser
from selenium import webdriver
# Import Options class to customize Chrome browser behavior
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Create and return a Chrome WebDriver instance"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Selenium Manager will automatically handle ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver