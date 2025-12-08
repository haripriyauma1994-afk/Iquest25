'''
Created on 24-Nov-2025

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

driver.get("https://testautomationpractice.blogspot.com/")
print("Navigated to practice site")

#3.click on simple alert
simple_alert_btn = driver.find_element(By.ID, "alertBtn")
simple_alert_btn.click()

time.sleep(3)

#4.click on OK on simple alert 
driver.switch_to.alert.accept() #def alert(self)->Alert: Switches focus to an alert on the page. accept() is used for click ok button

#Confirmation alert
#5.click on confirmation alert

confirmation_alert_btn = driver.find_element(By.ID,"confirmBtn")
confirmation_alert_btn.click()

time.sleep(3)

driver.switch_to.alert.dismiss() #dismiss is used for cancel button

#6.click prompt alert

click_promt_alert = driver.find_element(By.ID, "promptBtn")
click_promt_alert.click()

#sendkeys to prompt alert
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("hari")
prompt_alert.accept()
