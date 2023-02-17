from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup
from datetime import datetime



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


tr_list = driver.find_element(By.XPATH, "//div[contains(@class,'Cp')]//div[contains(@class,'F cf zt')]")
tr_list.click()

title_of_the_gmail = driver.find_elements(By.CLASS_NAME, "//div[contains(@class,'nH V8djrc byY')]//div[contains(@class,'hj')]//div[contains(@class, 'nH')]//div[contain(@class, 'ha')]")

soup_title = BeautifulSoup(title_of_the_gmail, "html.parser")

gmail_title = soup_title.find("h2").text

message_of_the_gmail = driver.find_element(By.CLASS_NAME, "//div[contains(@class, 'ii gt')]//div[contains(@class, 'a3s aiL')]")

actions_chain_for_hovering_on_attachments = ActionChains(driver)

attachments_box = driver.find_element(By.CLASS_NAME, "aQH")
attachments = attachments_box.find_elements(By.TAG_NAME, "span")

print("This is the message from ", "and the title is ", gmail_title, "this is the message:\n", message_of_the_gmail)

