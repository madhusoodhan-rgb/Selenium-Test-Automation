from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

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

    sort_dropdown = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    sort_dropdown.select_by_value("lohi")

    wait.until(
        lambda d: d.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text == "$7.99"
    )

    first_price = driver.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print("--------------------------------")
    print("TEST CASE: TC08 - Verify Product Sorting")
    print("First Product Price:", first_price)

    if first_price == "$7.99":
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC08 - Verify Product Sorting")
    print("STATUS: FAIL")
    print("Error:", e)

finally:
    driver.quit()
    