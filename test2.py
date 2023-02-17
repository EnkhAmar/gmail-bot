from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


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
sleep(15)

### Now we are on email list page
email_table = driver.find_element(By.XPATH, "//div[@class='Cp']//table[@class='F cf zt']")
mails = email_table.find_elements(By.TAG_NAME, "tr")

# selecting first mail from the mails which is the last email
mail = mails[0]
### 4th td element of tr is the button to read mail
btn = mail.find_elements(By.TAG_NAME, "td")[4]
btn.click()

# now we are on reading email item page.

gmail_title = driver.find_element(By.XPATH, "//div[@class='nH V8djrc byY']//h2").text
message_of_the_gmail = driver.find_element(By.XPATH, "//div[@class='ii gt']").text
if driver.find_element(By.CLASS_NAME, "aQH") == True:
    
    actions_chain_for_hovering_on_attachments = ActionChains(driver)
    attachments = driver.find_elements(By.XPATH, "//div[@class='aQH']//span[@class='aZo a5r']")
    first_attachment = attachments[0]
    driver.execute_script("arguments[0].setAttribute('class', 'aZo a5r aZp')", first_attachment) # This changed the code of the html line from 'aZo a5r' to 'aZo a5r aZp', which hovers on the attachment
    hovering_procedure = driver.find_elements(By.XPATH, "//div[@class='aQH']//span[@class='aZo a5r aZp']")
    # attachments = attachments_box.find_elements(By.CLASS_NAME, "aZo a5r")
    download_btn = hovering_procedure.find_elements(By.CLASS_NAME, "aSK J-J5-Ji aYr")
    attachment = actions_chain_for_hovering_on_attachments.move_to_element(download_btn).click().perform()
    save_dir = '/Users/daoerji/Downloads' # Need to change
    save_path = os.path.join(save_dir, attachment)
from_who_box = driver.find_elements(By.XPATH, "//div[@class='gE iv gt']//div[@class='cf gJ']")

print("This is the message from ", "and the title is ", gmail_title, "this is the message:\n", message_of_the_gmail, "the attachements are in the folder that is named: attachment-folder(which is in this directory:",  save_dir, ")")
