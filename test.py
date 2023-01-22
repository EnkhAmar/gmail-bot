from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
load_dotenv()


driver = webdriver.Firefox()
sleep(5)
driver.get("https://gmail.com")

sleep(5)
username_input = driver.find_element(By.ID, "identifierId")
username_input.clear()
username_input.send_keys(os.getenv("GMAIL_USERNAME"))
driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]").click()
sleep(3)
passwd_input = driver.find_element(By.NAME, "Passwd")
passwd_input.clear()
passwd_input.send_keys(os.getenv("GMAIL_PASSWORD"))
driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]").click()
sleep(5)
