'''
Created on 09-Dec-2025

@author: ABC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(20) #here we assigned driver for implicit waits
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("http://testautomationpractice.blogspot.com/")

#Locate the pagination page
all_data = [] #stores all rows

# Total pages = 4
for page in range(1,5):
    # Click pagination button
    driver.find_element(By.XPATH, f"//a[text()='{page}']").click()
    time.sleep(1)

    print(f"\n--- Page {page} ---")
# Locate table rows
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

    for r in rows:
        id_ = r.find_element(By.XPATH, "./td[1]").text
        name = r.find_element(By.XPATH, "./td[2]").text
        price = r.find_element(By.XPATH, "./td[3]").text

        print(id_, name, price)
        
        all_data.append(id_, name, price)
        print("\nAll Data Collected:")
for row in all_data:
    print(row)

driver.quit()
    
    

driver.find_element(By.XPATH, f"//a[text()='{page}']").click()
