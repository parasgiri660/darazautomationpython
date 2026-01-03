# Import By class to locate elements using different strategies (ID, XPATH, etc.)
from selenium.webdriver.common.by import By
# Import BasePage class to inherit common methods for element interaction
from pages.base_page import BasePage

# Page Object Model (POM) - SearchPage class
# POM is a design pattern that creates an object repository for web UI elements
# Benefits: Code reusability, maintainability, and readability
class SearchPage(BasePage):
    # Define locators as class attributes using XPATH strategy
    # These are the web elements we will interact with on the search page
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search in Daraz']")
    SEARCH_BUTTON = (By.XPATH, "//a[normalize-space(text())='SEARCH']")
    def __init__(self, driver):
        # Call the parent class (BasePage) constructor to initialize driver and wait
        super().__init__(driver)

    # Method to enter search query in the search input field
    def enter_search_query(self, query):
        """Enter search query in the search input field"""
        self.enter_text(self.SEARCH_INPUT, query)

    # Method to click on the search button
    def click_search_button(self):
        """Click on the search button"""
        self.click_element(self.SEARCH_BUTTON)

    # Method to validate if the search results page shows the searched product
    def validate_search_results(self, expected_product):
        """Validate if the search results page shows the searched product"""
        # Check if the expected product name appears in the page source
        #inbuilt function to convert lowercase
        page_text = self.driver.page_source.lower()
        return expected_product.lower() in page_text