
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

    product = wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Sauce Labs Backpack")
        )
    )
    product.click()

    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_details_name")
        )
    ).text

    product_price = driver.find_element(
        By.CLASS_NAME, "inventory_details_price"
    ).text

    product_description = driver.find_element(
        By.CLASS_NAME, "inventory_details_desc"
    ).text

    print("--------------------------------")
    print("TEST CASE: TC07 - Verify Product Details")
    print("Product:", product_name)
    print("Price:", product_price)
    print("Description:", product_description)

    if product_name == "Sauce Labs Backpack" and product_price == "$29.99" and product_description:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC07 - Verify Product Details")
    print("STATUS: FAIL")
    print("Error:", e)

finally:
    driver.quit()

