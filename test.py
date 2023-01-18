from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Firefox()
sleep(5)
driver.get("https://gmail.com")

sleep(5)
create_account_button = driver.find_element(By.XPATH, "//*[contains(text(),'Create account')]")
create_account_button.click()

create_account_for_me_btn = driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") if driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") else driver.find_element(By.XPATH, "//*[contains(text(),'For myself')]")
create_account_for_me_btn.click()

sleep(5)
try:
    next_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
except NoSuchElementException:
    next_btn = False