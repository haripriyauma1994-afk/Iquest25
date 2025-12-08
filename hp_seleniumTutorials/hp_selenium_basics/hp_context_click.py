'''
Created on 06-Dec-2025

Context click- means right click
@author: ABC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# 2. Navigating to application URL

driver.get("https://practice.expandtesting.com/context-menu")

#3.right click function


element = driver.find_element(By.ID, "hot-spot")

actions = ActionChains(driver)
actions.context_click(element).perform()

time.sleep(3)