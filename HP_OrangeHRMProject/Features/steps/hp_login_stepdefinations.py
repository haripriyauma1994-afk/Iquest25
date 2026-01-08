'''
Created on 05-Jan-2026

@author: hp
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Chrome browser is launched')#decorator or glue code
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    context.driver = webdriver.Chrome(options)
    context.driver.implicitly_wait(5)


@when(u'User navigates to OrangeHRM Login Page')
def navigate_to_orangehrml(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'User should see auth/login in current page URL')
def validate_login_page(context):
    expected_url= ("auth/login")
    current_page_url = context.driver.current_url
    assert expected_url in current_page_url, "'auth/login' is not present in current page URL"