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

username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys(os.getenv("GMAIL_USERNAME"))
driver.find_element(
    By.XPATH, "//*[contains(text(), 'Next')]").click()
sleep(3)
driver.find_element(By.NAME, "Passwd").send_keys("Thisistestpassw0rd")
driver.find_element(
    By.XPATH, "//*[contains(text(), 'Next')]").click()
sleep(3)

### Now we are on email list page


tr_list = driver.find_elements(By.XPATH, "//div[contains(@class,'Cp')]//div[contains(@class,'F cf zt')]")