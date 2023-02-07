from urllib import request
import pytest
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.utilities import *


def pytest_addoption(parser):
    parser.addoption("--json-arg", action="store", help ="Config")

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
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(base_url)
    yield driver
    driver.quit()


# @pytest.fixture(scope="session")
# def get_config_variables():
#     print("READING CONFIG FILES")
#     pytest.user_data = read_config("test-data/user.yaml")

#     config_data = read_config("config.yaml")
#     pytest.base_url = get_base_url(config_data)
#     pytest.num_processes = get_num_processes(config_data)

# def pytest_sessionstart(session):
#     print("READING CONFIG FILES")
#     session.config.user_data = read_config("test-data/user.yaml")

#     config_data = read_config("config.yaml")
#     session.config.base_url = get_base_url(config_data)
#     session.config.num_processes = get_num_processes(config_data)


    # session.config = config
