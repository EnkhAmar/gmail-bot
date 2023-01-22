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
        sleep(1)
        language_list_btn = self.driver.find_element(
            By.XPATH, "//div[@data-value='en']")
        language_list_btn.click()
        print(language_list_btn)

    def _goto_signup_page(self):
        sleep(3)
        # XPATH checks the element by the screen, just like, ctrl + F
        create_account_button = self.driver.find_element(
            By.XPATH, "//*[contains(text(),'Create account')]")
        create_account_button.click()
        create_account_for_me_btn = self.driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]") if self.driver.find_element(
            By.XPATH, "//*[contains(text(),'For my personal use')]") else self.driver.find_element(By.XPATH, "//*[contains(text(),'For myself')]")
        create_account_for_me_btn.click()

    def create_account(self, data: dict):
        self._goto_signup_page()
        if not self._check_default_language():
            self._change_language_to_en()

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
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Compose')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'To')]").send_keys("daoerji.si.2030@Esm.edu.mn")
        title = self.driver.find_element(By.NAME, "subjectbox").click()
        title.send_keys("Hello")
        message = self.driver.find_element(By.CLASS_NAME, "Am Al editable LW-avf tS-tW")
        message.send_keys("Test")
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Send')]").click()

bot = GmailBot()
# bot.create_account({
#     "first_name": "User",
#     "last_name": "User",
# })
bot.login(
    username=os.getenv("GMAIL_USERNAME"),
    password=os.getenv("GMAIL_PASSWORD"),
)
