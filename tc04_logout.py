
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

step = "Opening website"

try:
    driver.get("https://www.saucedemo.com/")

    step = "Entering login details"
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    step = "Waiting for successful login"
    wait.until(EC.url_contains("inventory.html"))
    print("Login successful")

    step = "Opening menu"
    wait.until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()
    print("Menu opened")

    step = "Clicking logout"
    wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    print("Logout clicked")

    step = "Verifying logout"
    wait.until(EC.url_to_be("https://www.saucedemo.com/"))

    print("--------------------------------")
    print("TEST CASE: TC04 - Logout User")
    print("Current URL:", driver.current_url)
    print("STATUS: PASS")
    print("--------------------------------")

except Exception as e:
    print("--------------------------------")
    print("TEST CASE: TC04 - Logout User")
    print("FAILED AT:", step)
    print("ERROR TYPE:", type(e).__name__)
    print("ERROR DETAILS:", repr(e))
    print("STATUS: FAIL")
    print("--------------------------------")

finally:
    driver.quit()

