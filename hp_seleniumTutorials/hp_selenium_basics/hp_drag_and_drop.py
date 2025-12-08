'''
Created on 05-Dec-2025

@author: hp
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

# 4. Scrolling
# actions.scroll_by_amount(0, 1680).perform() 

# 5. Drag and drop
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
# print(target.rect)

actions.scroll_from_origin(ScrollOrigin.from_element(target), 0, 200).perform()
actions.drag_and_drop(source, target).perform()


