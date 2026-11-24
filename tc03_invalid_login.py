
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    print("--------------------------------")
    print("TEST CASE: TC03 - Invalid Login")
    print("Error Message:", error_message.text)

    if "Username and password do not match" in error_message.text:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

finally:
    driver.quit()
