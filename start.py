from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox() # gets the webdriver from Firefox
driver.get("http://www.python.org") # goes to the given url
assert "Python" in driver.title # checks if the title of the given url cotains the word "Python"
elem = driver.find_element(By.NAME, "q") # finds the elem(element) "q" inside name="q", name="q is inside the html code of the website"
elem.clear() # clearing the things in the searchbox
sleep(2) # wait for 2 seconds to show the user what is happening
elem.send_keys("pycon") # types the word "pycon" inside the search box
sleep(2)
elem.send_keys(Keys.RETURN) # clicks the enter key(return key on macos)
assert "No results found." not in driver.page_source # checks if the text "No results found." was in the page_source of the driver
sleep(2)
driver.close() # closes the driver 
# shift command p to open the search