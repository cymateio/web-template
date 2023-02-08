from pages.base.base_workspaces import BaseWorkspaces

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Workspaces(BaseWorkspaces):
    dropdown_collection = "//*[@id='app-root']/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]"
    span_api = "//*[@id='app-root']/div/div/div[6]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]"
    button_send = "//*[@id='app-root']/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[1]"

    def __init__(self, driver):
        super().__init__(driver)

    def send_api(self):
        self.click_collection()
        self.click_api()
        self.click_send()

    def click_collection(self):
        self.wait_for_element_to_load(self.dropdown_collection)
        self.driver.find_element("xpath", self.dropdown_collection).click()

    def click_api(self):
        self.wait_for_element_to_load(self.span_api)
        self.driver.find_element("xpath", self.span_api).click()

    def click_send(self):
        self.wait_for_element_to_load(self.button_send)
        self.driver.find_element("xpath", self.button_send).click()

    def wait_for_element_to_load(self, element):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, element))
        )
