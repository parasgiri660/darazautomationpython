# Login Test Report

## Test Details
- **Test Name:** Valid Login Test
- **Tested By:** Paras Giri
- **Date:** 2026-01-02
- **Environment:** Chrome, Windows 10
- **Website:** [Daraz Nepal](https://www.daraz.com.np/#?)

---

## Test Description
Test the login functionality using multiple valid user credentials with **data-driven testing**.

---

## Steps Executed
1. Open the Daraz website.
2. Click on the **Login** link.
3. Enter **username** from test data.
4. Enter **password** from test data.
5. Click the **Login** button.
6. Verify the user is logged in successfully.

---

## Test Data
| Username          | Password      |
|------------------|---------------|
| standard_user     | secret_sauce  |
| test_user1        | password123   |
| demo_user         | demo123       |

---

## Test Results
| Step                        | Status |
|-----------------------------|--------|
| Open website                 | PASS   |
| Click login link             | PASS   |
| Enter username               | PASS   |
| Enter password               | PASS   |
| Click login button           | PASS   |
| Verify login                 | PASS   |

---

## Notes
- Each test step is logged in the **Extent Report**.
- The test can run multiple times for different users using **data parametrization**.

---

## Conclusion
Login functionality works as expected for all tested users. No defects found.
