# Import necessary modules for Selenium and ChromeDriver setup
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time

# Launch the browser with SeleniumWire capabilities
driver = webdriver.Chrome()
# Perform actions to trigger XHR requests
driver.get("https://www.google.com/")
search_bar = driver.find_element(By.ID, "APjFqb")
search_bar.send_keys("selenium")

# Wait for a short time to ensure XHR requests have been triggered
time.sleep(1)
# Access requests via the `requests` attribute
for request in driver.requests:
    if request.method== "POST":
        print(request)
		#print(f"URL: {request.url}")
        #print(f"Method: {request.method}")
        #print(f"Response Status Code: {request.response.status_code}")
