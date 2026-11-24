
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

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    # Open cart and checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    # Click Continue without entering any details
    driver.find_element(By.ID, "continue").click()

    # Verify validation error
    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    print("--------------------------------")
    print("TEST CASE: TC20 - Empty Checkout Form")
    print("Error Message:", error.text)

    if "First Name is required" in error.text:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC20 - Empty Checkout Form")
    print("STATUS: FAIL")
    print("Error:", repr(e))

finally:
    driver.quit()

