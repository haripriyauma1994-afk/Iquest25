'''
Created on 01-Dec-2025

@author: hp

XPATH - In selenium automation, if the elements are not found by the general locators like id, name, class etc the xpath is used to find an element on the webpage.

TYPES OF XPATH
1. ABSOLUTE XPATH: it is the direct way to find the element
 - The key characteristics of Xpath is that it begins with the single forward slash, which means you can select the element from the root node

2. RELATIVE XPATH: It starts from the middle of HTML DOM structure
  - It starts with double forward slash. It can search elements anywhere on the webpage, means no need to write a long xpath.
  
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

#3. switch to single frame
driver.switch_to.frame("singleframe")

#3 Enter name in single frame
input_txt_bx = driver.find_element(By.XPATH,'/html/body/section/div/div/div/input')
input_txt_bx.send_keys("hari")

