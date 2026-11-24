
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

    # Open side menu
    wait.until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()

    # Wait for Logout link
    logout = wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )

    logout.click()

    # Verify login page
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))

    print("--------------------------------")
    print("TEST CASE: TC26 - Menu Logout Navigation")
    print("Current URL:", driver.current_url)

    if "saucedemo.com" in driver.current_url and driver.find_element(By.ID, "login-button").is_displayed():
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC26 - Menu Logout Navigation")
    print("STATUS: FAIL")
    print("Error:", repr(e))
    print("--------------------------------")

finally:
    driver.quit()
