
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

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    cart_quantity = cart_badge.text

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    product_name = cart_item.text

    print("--------------------------------")
    print("TEST CASE: TC05 - Add Product toCart")
    print("Product:", product_name)
    print("Cart Quantity:", cart_quantity)

    if product_name == "Sauce Labs Backpack" and cart_quantity == "1":
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC05 - Add Product to Cart")
    print("STATUS: FAIL")
    print("Error:", e)

finally:
    driver.quit()

