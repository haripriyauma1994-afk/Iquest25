'''
Created on 03-Dec-2025

@author: hp

"""ActionChains are a way to automate low level interactions such as mouse
 movements, mouse button actions, key press, and context menu interactions.This is useful for doing more complex actions like hover over and drag and
 drop.
 
 Generate user actions.
       When you call methods for actions on the ActionChains object,
       the actions are stored in a queue in the ActionChains object.
       When you call perform(), the events are fired in the order they
       are queued up.
       
ActionChains can be used in a chain pattern::

        menu = driver.find_element(By.CSS_SELECTOR, ".nav")
        hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

        ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

    Or actions can be queued up one by one, then performed.::

        menu = driver.find_element(By.CSS_SELECTOR, ".nav")
        hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

        actions = ActionChains(driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()

    Either way, the actions are performed in the order they are called, one after
    another.

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5) #here we assigned driver for implicit waits
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("https://demo.automationtesting.in/Frames.html")

#3. create ActionChains object

actions = ActionChains(driver)

#4.mouse hover on Webtable menu item
Webtable_menu_item = driver.find_element(By.LINK_TEXT,"WebTable")#Locate the element
actions.move_to_element(Webtable_menu_item).perform()

#assignment frames website ali interactions
#automation pratice site ali copy text double click

