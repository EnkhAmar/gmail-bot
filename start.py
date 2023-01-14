from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
sleep(2)
elem.send_keys("pycon")
sleep(2)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
sleep(20)
driver.close()