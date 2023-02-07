from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.utilities import *


class BaseTest():

    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.config = self.read_config()
        base_url = get_base_url(self.config)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(base_url)
    
    def teardown_method(self):
        self.driver.quit()

    def read_config(self):
        user_data = read_config("test-data/user.yaml")
        config_data = read_config("config.yaml")
        config = {**user_data, **config_data}
        return config