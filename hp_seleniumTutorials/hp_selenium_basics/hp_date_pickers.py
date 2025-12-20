'''
Created on 11-Dec-2025

@author: ABC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")

#3. Enter the date picker
date_picker_1 = driver.find_element(By.ID, "datepicker")
date_picker_1.send_keys("01/01/2000")

#4 Enter Date in date picker 2
date_picker_2 = driver.find_element(By.ID, "txtDate")
# Remove readonly attribute using JavaScript
driver.execute_script("arguments[0].removeAttribute('readonly');",date_picker_2)
date_picker_2.send_keys("01/01/2000")

#5.