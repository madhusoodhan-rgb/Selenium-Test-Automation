
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

    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    wait.until(EC.url_contains("cart.html"))

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    wait.until(EC.url_contains("checkout-step-one.html"))

    # Wait until the actual checkout heading appears
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "[data-test='title']"),
            "Checkout: Your Information"
        )
    )

    heading = driver.find_element(
        By.CSS_SELECTOR, "[data-test='title']"
    ).text

    print("--------------------------------")
    print("TEST CASE: TC15 - Verify Checkout Navigation")
    print("Page Heading:", heading)
    print("Current URL:", driver.current_url)

    if heading == "Checkout: Your Information":
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC15 - Verify Checkout Navigation")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("--------------------------------")

finally:
    driver.quit()