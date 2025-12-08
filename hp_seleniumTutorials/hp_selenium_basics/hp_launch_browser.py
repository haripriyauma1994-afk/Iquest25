'''
Created on 08-Nov-2025

@author: ABC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()#here options is object and chromeoptions is class 
# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")
print("Navigated to practice site")

# 3. Get the URL of present page

current_page_url = driver.current_url
print("current_page_url:", current_page_url)

# 4. Get the Page Title of current page

current_page_title = driver.title
print("current_page_title:", current_page_title)

# 5. Validation
expected_url = "https://testautomationpractice.blogspot.com/"
expected_page_title = "Automation Testing Practice"

if expected_url == current_page_url:
    print("Test passed!")
else:
    print("Test failed!")
    
    
# 6. Enter name

# 6a. Locating the element
name_txt_bx = driver.find_element(By.ID, "name") 

# 6b. enter name
name_txt_bx.send_keys("Vivek")
