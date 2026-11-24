
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

    wait.until(EC.url_contains("cart.html"))

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    wait.until(EC.url_contains("checkout-step-one.html"))

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Madhu")

    driver.find_element(By.ID, "last-name").send_keys("Soodhan")
    driver.find_element(By.ID, "postal-code").send_keys("560001")
    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two.html"))

    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        )
    ).text

    product_price = driver.find_element(
        By.CSS_SELECTOR, ".cart_item .inventory_item_price"
    ).text

    item_total = driver.find_element(
        By.CLASS_NAME, "summary_subtotal_label"
    ).text

    print("--------------------------------")
    print("TEST CASE: TC17 - Verify Checkout Overview")
    print("Product:", product_name)
    print("Product Price:", product_price)
    print("Item Total:", item_total)

    if (product_name == "Sauce Labs Backpack"
            and product_price == "$29.99"
            and item_total == "Item total: $29.99"):
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC17 - Verify Checkout Overview")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("--------------------------------")

finally:
    driver.quit()

