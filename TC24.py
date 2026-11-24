
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

    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    # Enter customer information
    driver.find_element(By.ID, "first-name").send_keys("Madhu")
    driver.find_element(By.ID, "last-name").send_keys("Soodhan")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two.html"))

    # Finish the order
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    wait.until(EC.url_contains("checkout-complete.html"))

    # Verify confirmation heading and message
    heading = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-text"))
    )

    print("--------------------------------")
    print("TEST CASE: TC24 - Order Confirmation Message")
    print("Heading:", heading.text)
    print("Message:", message.text)

    if heading.text == "Thank you for your order!" and message.text:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC24 - Order Confirmation Message")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("--------------------------------")

finally:
    driver.quit()
