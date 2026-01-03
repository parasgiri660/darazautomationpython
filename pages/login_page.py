# Import By class to locate elements using different strategies (ID, XPATH, etc.)
from selenium.webdriver.common.by import By
# Import BasePage class to inherit common methods for element interaction
from pages.base_page import BasePage

# Page Object Model (POM) - LoginPage class
# POM is a design pattern that creates an object repository for web UI elements
# Benefits: Code reusability, maintainability, and readability
class LoginPage(BasePage):
    # Define locators as class attributes using XPATH strategy
    # These are the web elements we will interact with on the login page
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Login']")
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Please enter your Phone or Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Please enter your password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='LOGIN']")
    FORGOT_PASSWORD = (By.XPATH, "//div[text()='Forgot password?']")
    SIGNUP_LINK = (By.XPATH, "//span[text()='Sign up']")
    GOOGLE_LOGIN = (By.XPATH, "//span[normalize-space()='Google']")

    # Constructor method to initialize the LoginPage with a webdriver instance
    def __init__(self, driver):
        # Call the parent class (BasePage) constructor to initialize driver and wait
        super().__init__(driver)

    # Method to click on the login link
    def click_login_link(self):
        """Click on the login link"""
        # Use the click_element method from BasePage to click the login link
        self.click_element(self.LOGIN_LINK)

    # Method to enter username in the username input field
    def enter_username(self, username):
        """Enter username/email"""
        # Use the enter_text method from BasePage to input the username
        self.enter_text(self.USERNAME_INPUT, username)

    # Method to enter password in the password input field
    def enter_password(self, password):
        """Enter password"""
        # Use the enter_text method from BasePage to input the password
        self.enter_text(self.PASSWORD_INPUT, password)

    # Method to click on the login button
    def click_login_button(self):
        """Click on the login button"""
        # Use the click_element method from BasePage to click the login button
        self.click_element(self.LOGIN_BUTTON)

    # Method to click on the forgot password link
    def click_forgot_password(self):
        """Click on forgot password link"""
        # Use the click_element method from BasePage to click the forgot password link
        self.click_element(self.FORGOT_PASSWORD)

    # Method to click on the signup link
    def click_signup_link(self):
        """Click on signup link"""
        # Use the click_element method from BasePage to click the signup link
        self.click_element(self.SIGNUP_LINK)

    # Method to click on the Google login option
    def click_google_login(self):
        """Click on Google login option"""
        # Use the click_element method from BasePage to click the Google login option
        self.click_element(self.GOOGLE_LOGIN)

    # Method to perform the complete login process with given credentials
    def login(self, username, password):
        """Perform login with given credentials"""
        # Click the login link to navigate to the login page
        self.click_login_link()
        # Enter the username in the input field
        self.enter_username(username)
        # Enter the password in the input field
        self.enter_password(password)
        # Click the login button to submit the credentials
        self.click_login_button()
