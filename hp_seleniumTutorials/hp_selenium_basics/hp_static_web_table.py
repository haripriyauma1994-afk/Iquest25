'''
Created on 07-Dec-2025

@author: hp
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from debugpy._vendored.pydevd.pydevd_attach_to_process.winappdbg.win32.defines import TRUE

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# 2. Navigating to application URL

driver.get("http://testautomationpractice.blogspot.com/")

#3.printing the static web table

for r in range(2, 8):     # rows 2 to 7
    for c in range(1, 5): # columns 1 to 4
        cell = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]")
        print(cell.text, end=" | ")
    print()



        
        
                   




