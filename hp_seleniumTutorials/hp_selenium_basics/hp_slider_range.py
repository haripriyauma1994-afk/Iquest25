'''
Created on 06-Dec-2025

@author: ABC
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

# 3. Create ActionChains object
actions = ActionChains(driver)

#4.slider range code
#actions.drag_and_drop_by_offset(source, xoffset, yoffset) This is used for slider range.
handle = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(handle, -50,0).perform()#x axis to locate

handle_2 = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(handle_2, 60,0).perform() #y axis to locate

