import pytest
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.utilities import *


def pytest_addoption(parser):
    parser.addoption("--json-arg", action="store", help="Config")


def get_config(request):
    config_param = json.loads(request.config.getoption("--json-arg"))
    return config_param


@pytest.fixture(scope="session")
def config(request):
    return get_config(request)


@pytest.fixture(scope="session")
def driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    base_url = get_base_url(get_config(request))
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(base_url)
    yield driver
    driver.quit()
