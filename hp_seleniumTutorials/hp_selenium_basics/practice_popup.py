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

#7 popups

click_pop_up = driver.find_element(By.ID, "PopUp")
click_pop_up.click()

#7.0 switch to window

windows = driver.window_handles #predefined function
print("windows:",windows)

#driver.switch_to.window(windows[1])
#selenium_register_suggestion =driver.find_element(By.LINK_TEXT,"Register now!")
#selenium_register_suggestion.click()
time.sleep(2)
driver.switch_to.window(windows[2])

#second window click actions

driver.switch_to.window(windows[2])
selenuim_playright_window =driver.find_element(By.CLASS_NAME,"getStarted_Sjon")
selenuim_playright_window.click()

