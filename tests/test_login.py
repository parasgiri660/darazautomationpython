import pytest
import time

from pages.login_page import LoginPage
from data.test_data import TEST_USERS, INVALID_USERS
from utils.test_runner import create_driver
from utils.assertions import assert_true, assert_false



class TestLogin:
    def setup_method(self):
        """Setup method to initialize driver for each test"""
        self.driver = create_driver()
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://www.daraz.com.np/#?")

    def teardown_method(self):
        """Teardown method to quit driver"""
        self.driver.quit()

    @pytest.mark.parametrize("user_data", TEST_USERS)
    def test_valid_login(self, user_data):
        """Test valid login with different user credentials using data parametrization"""

        # Perform login steps
        self.login_page.click_login_link()

        self.login_page.enter_username(user_data["username"])

        self.login_page.enter_password(user_data["password"])

        self.login_page.click_login_button()

        # Wait for page transition
        time.sleep(3)

        # Verify successful login
        login_link_present = self.login_page.is_element_present(self.login_page.LOGIN_LINK)
        assert_false(login_link_present, "Login was not successful - login element is still present")

    @pytest.mark.parametrize("user_data", INVALID_USERS)
    def test_invalid_login(self, user_data):
        """Test invalid login with different invalid credentials using data parametrization"""

        # Perform login with invalid credentials
        self.login_page.click_login_link()

        self.login_page.enter_username(user_data["username"])

        self.login_page.enter_password(user_data["password"])

        self.login_page.click_login_button()

        # Wait for error message display
        time.sleep(3)

        # Verify login failed
        login_link_present = self.login_page.is_element_present(self.login_page.LOGIN_LINK)
        assert_true(login_link_present, "Login should have failed but appears to have succeeded")
