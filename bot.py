"""
TODO: Creating a new account
1. Go to https://gmail.com/
2. Click on the "create account" drop down list and choose "for my personal use"
3. Fill the create new account form and click "next" button
4. On the next page, check if the "phone number" is optional. If the phone number is optional goto 4.1, else 4.2.
4.1. Fill the form and click "next" button
4.2. Leave this later
5. Agree the policy
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://gmail.com")

sleep(5)
create_account_button = driver.find_element(By.XPATH, "//*[contains(text(),'Create account')]")
create_account_button.click()

create_account_for_me_btn = driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") if driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") else driver.find_element(By.XPATH, "//*[contains(text(),'For myself')]")
create_account_for_me_btn.click()

"""
TODO: Login using existing account
1. Go to https://gmail.com/
2. Click on the "create account" drop down list and choose "for my personal use"
3. Fill the create new account form and click "next" button
4. On the next page, check if the "phone number" is optional. If the phone number is optional goto 4.1, else 4.2.
4.1. Fill the form and click "next" button
4.2. Leave this later
5. Agree the policy
"""