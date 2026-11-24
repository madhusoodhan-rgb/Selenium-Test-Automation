
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

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.url_contains("checkout-step-one.html"))

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Madhu")

    driver.find_element(By.ID, "last-name").send_keys("Soodhan")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two.html"))

    print("--------------------------------")
    print("TEST CASE: TC16 - Verify Checkout Information")
    print("Current URL:", driver.current_url)

    if "checkout-step-two.html" in driver.current_url:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC16 - Verify Checkout Information")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("--------------------------------")

finally:
    driver.quit()
