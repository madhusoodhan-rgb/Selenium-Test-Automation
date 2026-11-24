
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.saucedemo.com/")

    print("--------------------------------")
    print("TEST CASE: TC01 - Open Homepage")
    print("Website:", driver.current_url)
    print("Page Title:", driver.title)

    if driver.title == "Swag Labs":
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

    print("--------------------------------")

finally:
    driver.quit()
