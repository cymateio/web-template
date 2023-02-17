from pages.base.base_main import BaseMain

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main(BaseMain):
    dropdown_workspaces = "//*[@id='app-root']/div/div/div[5]/div[1]/div/div[1]"
    span_myworkspaces = "//*[@id='app-root']/div/div/div[5]/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/a/div/div[2]/span"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_workspace(self):
        self.wait_for_dropdown_to_load()
        self.driver.find_element("xpath", self.dropdown_workspaces).click()
        self.wait_for_span_to_load()
        self.driver.find_element("xpath", self.span_myworkspaces).click()

    def wait_for_dropdown_to_load(self):
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, self.dropdown_workspaces))
        )

    def wait_for_span_to_load(self):
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, self.span_myworkspaces))
        )
