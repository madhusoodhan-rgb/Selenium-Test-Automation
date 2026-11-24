
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

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    cart_icon = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.shopping_cart_link")
        )
    )

    cart_icon.click()

    wait.until(EC.url_contains("cart.html"))

    print("--------------------------------")
    print("TEST CASE: TC13 - Verify Cart Navigation")
    print("Current URL:", driver.current_url)

    if "cart.html" in driver.current_url:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC13 - Verify Cart Navigation")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("--------------------------------")

finally:
    driver.quit()

