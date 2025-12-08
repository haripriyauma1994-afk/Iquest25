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

#3.upload multiple file
multiple_file_upload = driver.find_element(By.ID, "multipleFilesInput")
multiple_file_upload.send_keys(r"C:\Users\ABC\Desktop\githup pwd.txt")
multiple_file_upload.send_keys(r"C:\Users\ABC\Desktop\SONNA RESUME.txt")
multiple_file_upload.send_keys(r"C:\Users\ABC\Desktop\haririya resume.pdf")

#4 click on upload multiple file

upload_multiple_file = driver.find_element(By.XPATH, '//button[text()="Upload Multiple Files"]')
upload_multiple_file.click()

#5.get or fetch the upload status message
multiple_file_status = driver.find_element(By.ID, "multipleFilesStatus")
print(multiple_file_status.text)# using element.text we got text displayed

