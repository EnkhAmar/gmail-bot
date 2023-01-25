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
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os
import random
import string
from datetime import datetime
load_dotenv()


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

def generate_random_string(length=10, include_number:bool=False, include_symbol=False):
    letters = string.ascii_letters
    if include_number: letters += string.digits
    if include_symbol: letters += "!@#$%^&*()_+=-"
    return "".join(random.choice(letters) for _ in range(length))

class GmailBot:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://gmail.com")

    def __del__(self) -> None:
        # self.driver.close()
        pass

    def _check_default_language(self) -> bool:
        try:
            next_btn = self.driver.find_element(
                By.XPATH, "//*[contains(text(), 'Next')]")
        except NoSuchElementException:
            next_btn = False
        return bool(next_btn)

    def _change_language_to_en(self):
        # CLASS_NAME check the element by its classname
        language_list_btn = self.driver.find_element(By.CLASS_NAME, "TquXA")
        language_list_btn.click()  # we could add the click() right after the line above]
        for elem in self.driver.find_elements(By.XPATH, "//div[@data-value='en']"):
            if "English (United States)" in elem.text: elem.click()

    def _goto_signup_page(self):
        sleep(3)
        # XPATH checks the element by the screen, just like, ctrl + F
        create_account_button = self.driver.find_element(
            By.XPATH, "//*[contains(text(),'Create account')]")
        create_account_button.click()
        create_account_for_me_btn = self.driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") if self.driver.find_element(
            By.XPATH, "//*[contains(text(),'For my personal use')]") else self.driver.find_element(By.XPATH, "//*[contains(text(),'For myself')]")
        create_account_for_me_btn.click()

    def _fill_sign_up_form(self, data:dict):
        self.driver.find_element(By.ID, "firstName").send_keys(data['first_name'])
        self.driver.find_element(By.ID, "lastName").send_keys(data['last_name'])
        self.driver.find_element(By.ID, "username").send_keys(data['username'])
        self.driver.find_element(By.NAME, 'Passwd').send_keys(data['password'])
        self.driver.find_element(By.NAME, 'ConfirmPasswd').send_keys(data['password'])
        
    def create_account(self, data: dict):
        """
        If username is not given, it will generate username
        If password is not given, it will generate password
        """
        self._goto_signup_page()
        if not self._check_default_language():
            self._change_language_to_en()
        if not data["username"]: data["username"] = generate_random_string()
        if not data["password"]: data["password"] = generate_random_string(length=12, include_number=True, include_symbol=True)
        self._fill_sign_up_form(data)
        self._click_next_btn()
        data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return data

    def _click_next_btn(self):
        self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Next')]").click()
        sleep(3)

    def login(self, username: str, password: str):
        username_input = self.driver.find_element(By.ID, "identifierId")
        username_input.clear()
        username_input.send_keys(username)
        self._click_next_btn()
        password_input = self.driver.find_element(By.NAME, "Passwd")
        password_input.send_keys(password)
        self._click_next_btn()

    def read_email(self):
        pass

    def send_email(self, message: str, title: str, to: str):
        compose = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Compose')]").click()
        if compose == False:
            self.login()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'To')]").send_keys("daoerji.si.2030@Esm.edu.mn")
        title = self.driver.find_element(By.NAME, "subjectbox").click()
        title.send_keys("Hello")
        message = self.driver.find_element(By.CLASS_NAME, "Am Al editable LW-avf tS-tW")
        message.send_keys("Test")
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Send')]").click()

bot = GmailBot()
user1 = bot.create_account({
    "first_name": "User",
    "last_name": "User",
    "username": None,
    "password": None
})
print(user1)

# bot.login(
#      username=os.getenv("GMAIL_USERNAME"),
#      password=os.getenv("GMAIL_PASSWORD"),
# )

