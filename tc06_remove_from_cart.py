
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

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    driver.find_element(
        By.ID, "remove-sauce-labs-backpack"
    ).click()

    wait.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    print("--------------------------------")
    print("TEST CASE: TC06 - Remove Product from Cart")
    print("Current URL:", driver.current_url)

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

    if len(cart_items) == 0:
        print("Cart Status: Empty")
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC06 - Remove Product from Cart")
    print("STATUS: FAIL")
    print("Error:", e)

finally:
    driver.quit()

