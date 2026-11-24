
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))

    # Add product
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    # Open cart
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))
    ).click()

    wait.until(EC.url_contains("cart.html"))

    # Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    # Enter information
    driver.find_element(By.ID, "first-name").send_keys("Madhu")
    driver.find_element(By.ID, "last-name").send_keys("Soodhan")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two.html"))

    # Finish order
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Wait for confirmation page
    wait.until(EC.url_contains("checkout-complete.html"))
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    # Locate Back Home button using data-test
    back_home = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='back-to-products']")
        )
    )

    back_home.click()

    # Verify inventory page
    wait.until(EC.url_contains("inventory.html"))

    print("--------------------------------")
    print("TEST CASE: TC25 - Back Home Navigation")
    print("Current URL:", driver.current_url)
    print("STATUS: PASS")
    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC25 - Back Home Navigation")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("Current URL:", driver.current_url)
    print("--------------------------------")

finally:
    driver.quit()
