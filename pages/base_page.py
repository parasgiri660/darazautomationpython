# Import WebDriverWait class to implement explicit waits for elements
from selenium.webdriver.support.ui import WebDriverWait
# Import expected_conditions as EC to define conditions for explicit waits
from selenium.webdriver.support import expected_conditions as EC
# Import TimeoutException to handle timeout scenarios when waiting for elements
from selenium.common.exceptions import TimeoutException


class BasePage:
    # Constructor method to initialize the BasePage with a webdriver instance
    def __init__(self, driver):
        # Store the webdriver instance as an instance variable
        self.driver = driver
        # Create a WebDriverWait instance with a timeout of 10 seconds for explicit waits
        self.wait = WebDriverWait(driver, 10)

    # Method to find a single web element using explicit wait
    def find_element(self, locator):
        """Find a single web element"""
        # Wait until the element is present in the DOM and return it
        return self.wait.until(EC.presence_of_element_located(locator))

    # Method to find a clickable web element using explicit wait
    def find_clickable_element(self, locator):
        """Find a clickable web element"""
        # Wait until the element is clickable and return it
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Method to find a visible web element using explicit wait
    def find_visible_element(self, locator):
        """Find a visible web element"""
        # Wait until the element is visible and return it
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Method to enter text into an input field
    def enter_text(self, locator, text):
        """Enter text into an input field"""
        # Find the element using the locator
        element = self.find_element(locator)
        # Clear any existing text in the input field
        element.clear()
        # Send the specified text to the input field
        element.send_keys(text)


    # Method to click on a web element
    def click_element(self, locator):
        """Click on a web element"""
        # Find the clickable element using the locator
        element = self.find_clickable_element(locator)
        # Click on the element
        element.click()

    # Method to get text from a web element
    def get_text(self, locator):
        """Get text from a web element"""
        # Find the element using the locator
        element = self.find_element(locator)
        # Return the text content of the element
        return element.text

    # Method to check if an element is present on the page
    def is_element_present(self, locator):
        """Check if an element is present"""
        # Try to find the element
        try:
            # Attempt to find the element using the locator
            self.find_element(locator)
            # Return True if element is found
            return True
        # Handle the exception if element is not found
        except TimeoutException:
            # Return False if element is not present within the timeout period
            return False