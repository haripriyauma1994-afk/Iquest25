'''
Created on 09-Dec-2025

@author: ABC

shadow dom 
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")

#get rows and colums count
rows = driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr')
rows_count = len(rows)
print("rows_count:", rows_count)

columns = driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr[2]/td')
columns_count = len(columns)
print("columns_count:", columns_count)

#3.Locate shadow dom element
ap_shadow_host = driver.find_element(By.ID,"shadow_host")
ap_shadow_root = ap_shadow_host.shadow_root

shadow_text_field = ap_shadow_root.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')
shadow_text_field.send_keys("hari")

