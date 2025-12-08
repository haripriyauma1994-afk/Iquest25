'''
Created on 06-Dec-2025

@author: hp
def key_down(self, value: str, element: WebElement | None = None) -> ActionChains:
        """Sends a key press only, without releasing it. Should only be used
        with modifier keys (Control, Alt and Shift).

        Args:
            value: The modifier key to send. Values are defined in `Keys` class.
            element: The element to send keys.
                If None, sends a key to current focused element.

        Example, pressing ctrl+c::

            ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
            
    def key_up(self, value: str, element: WebElement | None = None) -> ActionChains:
        """Releases a modifier key.

        Args:
            value: The modifier key to send. Values are defined in Keys class.
            element: The element to send keys.
                If None, sends a key to current focused element.

        Example, pressing ctrl+c::

            ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

#4.select the content in field1 --> Ctrl+A
field1 = driver.find_element(By.ID, "field1")
actions.key_down(Keys.CONTROL, field1).send_keys("A").key_up(Keys.CONTROL).perform()


#5.Copy content from field1--> Ctrl+C
field1 = driver.find_element(By.ID, "field1")
actions.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()

#6 paste the content into field2--> Ctrl+V
field2 = driver.find_element(By.ID, "field2")
actions.key_down(Keys.CONTROL, field2).send_keys("V").key_up(Keys.CONTROL).perform()


