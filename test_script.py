from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Chrome driver path
driver = webdriver.Chrome(executable_path="D:\\JavaSelenium\\drivers\\chromedriver-win64\\chromedriver.exe")

# Open a website
driver.get("https://example.com")

# Test: Check page title
if "Example Domain" in driver.title:
    print("Test Passed ✅")
else:
    print("Test Failed ❌")

driver.quit()
