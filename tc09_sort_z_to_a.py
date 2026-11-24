
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
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
        lambda d: len(d.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )) > 0
    )

    sort_dropdown = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )
    sort_dropdown.select_by_value("za")

    wait.until(
        lambda d: d.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )[0].text == "Test.allTheThings() T-Shirt (Red)"
    )

    first_product = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )[0].text

    print("--------------------------------")
    print("TEST CASE: TC09 - Sort Products Z to A")
    print("First Product:", first_product)

    if first_product == "Test.allTheThings() T-Shirt (Red)":
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("TEST CASE: TC09 - Sort Products Z to A")
    print("STATUS: FAIL")
    print("Error:", repr(e))

finally:
    driver.quit()

