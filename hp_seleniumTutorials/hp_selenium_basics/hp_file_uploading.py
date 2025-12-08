"""
Created on 06-Dec-2025
@author: ABC
Escape sequence/Escape character
slash u is unicode escape character 
"""

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

#3.upload single file *choosen file button

single_file_input = driver.find_element(By.ID, "singleFileInput")
single_file_input.send_keys(r"C:\Users\ABC\Desktop\Manual Testing for Freshers.pdf")#using r (raw text)
#single_file_input.send_keys("C:\\Users\\ABC\\Desktop\Manual Testing for Freshers.pdf")#\\ double forward slash
#single_file_input.send_keys(r"C:/Users/ABC/Desktop/Manual Testing for Freshers.pdf") #/ using backward slash

#4.clickon upload single file

#click_on_single_file = driver.find_element(By.XPATH, '//*[@id="singleFileForm"]/button')
upload_single_file = driver.find_element(By.XPATH, '//button[text()="Upload Single File"]') #this is manually done xpath linkusing xpath format example
upload_single_file.click()

#5.get or fetch the upload status message
single_file_status = driver.find_element(By.ID, "singleFileStatus")
print(single_file_status.text)# using element.text we got text displayed





