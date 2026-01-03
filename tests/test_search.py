import pytest
import time

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from data.test_data import TEST_USERS, SEARCH_PRODUCTS
from utils.test_runner import create_driver
from utils.assertions import assert_true


class TestSearch:
    def setup_method(self):
        """Setup method to initialize driver for each test"""
        self.driver = create_driver()
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.driver.get("https://www.daraz.com.np/#?")

    def teardown_method(self):
        """Teardown method to quit driver"""
        self.driver.quit()

    @pytest.mark.parametrize("search_data", SEARCH_PRODUCTS)
    def test_search_product(self, search_data):
        """Test searching for a product and validating the search results"""

        product_name = search_data["product_name"]
        self.search_page.enter_search_query(product_name)
        self.search_page.click_search_button()

        # Wait for search results to load
        time.sleep(3)

        # Validate that the search results page shows the searched product
        search_results_valid = self.search_page.validate_search_results(product_name)
        assert_true(search_results_valid, f"Search results do not contain the expected product: {product_name}")