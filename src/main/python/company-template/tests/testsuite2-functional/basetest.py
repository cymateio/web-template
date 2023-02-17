import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.utilities import *


class BaseTest:
    def setup_method(self):
        self.config = self.read_config()
        test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]

        if self.config["env"] == "saucelabs":
            _credentials = (
                self.config["saucelabs_username"]
                + ":"
                + self.config["saucelabs_accesskey"]
            )
            _url = "https://" + _credentials + "@ondemand.saucelabs.com/wd/hub"
            self.config["capabilities"]["sauce:options"]["name"] = test_name
            self.driver = webdriver.Remote(_url, self.config["capabilities"])
        else:
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=chrome_options)

        base_url = self.config["base_url"]
        self.driver.get(base_url)

    def teardown_method(self):
        self.driver.quit()

    def read_config(self):
        user_data = read_config("test-data/user.yaml")
        config_data = read_config("config.yaml")
        config = {**user_data, **config_data}
        return config
