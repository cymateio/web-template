from selenium import webdriver
from pages.base.base_signin import BaseSignin

class Signin(BaseSignin):

    textbox_username = "username"
    textbox_password = "password"
    button_signin = "//*[@id='sign-in-btn']"

    def __init__(self, driver):
        super().__init__(driver)

    def signin(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_signin()

    def set_username(self, username):
        self.driver.find_element("id", self.textbox_username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element("id", self.textbox_password).send_keys(password)
    
    def click_signin(self):
        self.driver.find_element("xpath", self.button_signin).click()

    