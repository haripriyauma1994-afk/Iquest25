'''
Created on 19-Nov-2025

@author: ABC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Launching the chrome browser 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
print("Chrome browser is launched")

# 2. Navigating to application URL

driver.get("https://testautomationpractice.blogspot.com/")
print("Navigated to practice site")

# 3. Enter text in wiki search text box
# Locate the element
wiki_search_bx = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")

# Action
wiki_search_bx.send_keys("Selenium")

# 4. Click on wiki search button
# Locate
wiki_search_button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")

# Action
wiki_search_button.click()

#time.sleep(2) #Hard wait

windows = driver.window_handles
print("windows:",windows)


print("Before clicking on search result:",driver.title)

#5.click on a search result
#locate using link text
wiki_search_suggestion =driver.find_element(By.LINK_TEXT,"Selenium (software)")
#click action
wiki_search_suggestion.click()

print("After clicking on search result:",driver.title)


#6.Switch the tab/ Window
windows = driver.window_handles #predefined function
print("windows:",windows)

#wiki_search_suggestion =driver.find_element(By.ID,"toc_History")
#wiki_search_suggestion.click()

driver.switch_to.window(windows[1])
wiki_search_suggestion =driver.find_element(By.ID,"toc-History")
wiki_search_suggestion.click()

#7.click on simple alert

click_simple_alert =driver.find_element(By.ID, "alertBtn")
click_simple_alert.click()

