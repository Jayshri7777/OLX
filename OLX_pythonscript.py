from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Chrome WebDriver (ensure chromedriver is installed and added to PATH)
driver = webdriver.Chrome()

# Target OLX URL for 'Car Cover'
url = "https://www.olx.in/items/q-car-cover"
driver.get(url)

time.sleep(60)  # Wait for dynamic content to load

titles = []
prices = []

# Collect listing elements
items = driver.find_elements(By.XPATH, "//li[contains(@data-aut-id,'itemBox')]")

for item in items:
    try:
        title = item.find_element(By.TAG_NAME, "h6").text
        price = item.find_element(By.XPATH, ".//span").text
        titles.append(title)
        prices.append(price)
    except:
        continue

driver.quit()

# Save to CSV
df = pd.DataFrame({'Title': titles, 'Price': prices})
df.to_csv('olx_car_covers.csv', index=False)

print("Saved results to olx_car_covers.csv")
