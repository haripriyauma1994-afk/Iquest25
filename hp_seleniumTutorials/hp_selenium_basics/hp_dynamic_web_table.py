'''
Created on 08-Dec-2025

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

#//tbody[@id='rows']/tr[4]/td[contains(text(),"MB") and not(contains(text(),"/s"))]