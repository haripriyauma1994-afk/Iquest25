'''
Created on 02-Dec-2025

@author: ABC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(20) #here we assigned driver for implicit waits
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("https://demo.automationtesting.in/Frames.html")

#3.switch to iframe within an iframe

driver.switch_to_frame = driver.find_element(By.CLASS_NAME, "analystic")
driver.switch_to_frame.click()