
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))

    # Add product and open cart
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))

    # Open checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    # Enter first and last names, but leave postal code empty
    driver.find_element(By.ID, "first-name").send_keys("Madhu")
    driver.find_element(By.ID, "last-name").send_keys("Soodhan")

    driver.find_element(By.ID, "continue").click()

    # Verify error message
    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    print("--------------------------------")
    print("TEST CASE: TC22 - Missing Postal Code")
    print("Error Message:", error.text)

    if "Postal Code is required" in error.text:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC22 - Missing Postal Code")
    print("STATUS: FAIL")
    print("Error:", repr(e))

finally:
    driver.quit()

