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
email_table = driver.find_element(By.XPATH, "//div[@class='Cp']//table[@class='F cf zt']")
mails = email_table.find_elements(By.TAG_NAME, "tr")

# selecting first mail from the mails which is the last email
mail = mails[0]
### 4th td element of tr is the button to read mail
btn = mail.find_elements(By.TAG_NAME, "td")[4]
btn.screenshot("test.png")
btn.click()