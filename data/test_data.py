# Test data for login tests
TEST_USERS = [
    {"username": "abc.com", "password": "abcd*88"},
    {"username": "test@example.com", "password": "test123"},
    {"username": "user@domain.com", "password": "password123"},
    {"username": "thapasandhya1301@gmail.com", "password": "Sandhya@123"}
]

# Invalid user credentials for testing failed login
INVALID_USERS = [
    {"username": "", "password": "abcd*88"},  # Empty username
    {"username": "invalid.com", "password": ""},  # Empty password
    {"username": "", "password": ""},  # Both empty
    {"username": "nonexistent@example.com", "password": "wrongpassword"}  # Invalid credentials
]

# Test data for search functionality
SEARCH_PRODUCTS = [
    {"product_name": "iPhone 13"},
    {"product_name": "Samsung Galaxy"},
    {"product_name": "laptop"},
    {"product_name": "headphones"},
    {"product_name": "shoes"}
]