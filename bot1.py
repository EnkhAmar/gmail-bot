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
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=EN&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S2013941162%3A1673679636252032&emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AeAAQh4ZBpdJ8Q9jgkB1CqK26qMRlYFbGdtPU2D4PRvQ9CcJm1-RIZCmu1HDwaxE4ftREk8QFDNP1w&osid=1&service=mail")

sleep(5)
create_account_button = driver.find_element(By.XPATH, "//*[contains(text(),'Create account')]")
create_account_button.click()

create_account_for_me_btn = driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") if driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") else driver.find_element(By.XPATH, "//*[contains(text(),'For myself')]")
create_account_for_me_btn.click()

sleep(5)
first_name_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'firstName')]")
first_name_btn.click()
first_name_btn.send_keys("Dorji")

last_name_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'lastName')]")
last_name_btn.click()
last_name_btn.send_keys("Siriguleng")

user_name_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Username')]")
user_name_btn.click()
user_name_btn.send_keys("dorjisiriguleng")

password = driver.find_element(By.XPATH, "//*[contains(text(), 'Passwd')]")
password.click()
password.send_keys("1234567890-a")

confirm_passwd = driver.find_element(By.XPATH, "//*[contains(text(), 'Confirm')]")
confirm_passwd.click()
confirm_passwd.send_keys("1234567890-a")

next_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
next_btn.click()

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