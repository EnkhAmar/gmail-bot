from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
load_dotenv()

# import undetected_chromedriver as uc

# useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"
profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override", useragent)
profile_path = "/Users/enkh-amarganbat/Library/Application Support/Firefox/Profiles/lax1e3v4.default-release"
options = webdriver.FirefoxOptions()

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

# options.set_preference('options', profile_path)
# options.set_preference('network.proxy.type', 1)
# options.set_preference('network.proxy.socks', '127.0.0.1')
# options.set_preference('network.proxy.socks_port', 9050)
# options.set_preference('network.proxy.socks_remote_dns', False)

# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
# for arg in ['--disable-web-security', '--allow-running-insecure-content' ]:
#     options.add_argument(arg)


# driver = webdriver.Firefox(firefox_profile=profile, options=options)
# driver = uc.Chrome()
driver = webdriver.Firefox(options=options)
driver.delete_all_cookies()
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