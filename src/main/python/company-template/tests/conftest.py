import pytest
import logging
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.utilities import *


###########################
##### CONFTEST METHOD #####
###########################


def pytest_addoption(parser):
    parser.addoption("--json-arg", action="store", help="Config")
    parser.addoption("--log-dir", action="store", help="Current Runtime")


##################
##### CONFIG #####
##################


def get_config(request):
    config_param = json.loads(request.config.getoption("--json-arg"))
    return config_param


@pytest.fixture(scope="session")
def config(request):
    return get_config(request)


##################
##### LOGGER #####
##################


def pytest_configure(config):
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    dir_format = config.getoption("--log-dir")

    if worker_id is not None:
        logging.basicConfig(
            format=config.getini("log_file_format"),
            filename=dir_format + "/{}.log".format(worker_id),
            level=config.getini("log_file_level"),
        )


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


@pytest.fixture(scope="session")
def logger():
    return get_logger()


@pytest.fixture(scope="function", autouse=True)
def log_testname(request, driver):
    logger = get_logger()
    logger.info(
        f"==================================== STARTING TEST: {request.node.name}"
    )

    config = get_config(request)
    if config["env"] == "saucelabs":
        logger.info(
            "SAUCELABS SESSION: https://app.saucelabs.com/tests/" + driver.session_id
        )
    else:
        logger.info("SESSION ID: " + driver.session_id)

    def log_after():
        logger.info(
            f"==================================== FINISHED TEST: {request.node.name}"
        )

    request.addfinalizer(log_after)


##################
##### DRIVER #####
##################


@pytest.fixture(scope="session")
def driver(request):
    config = get_config(request)
    test_name = request.node.name

    if config["env"] == "saucelabs":
        _credentials = (
            config["saucelabs_username"] + ":" + config["saucelabs_accesskey"]
        )
        _url = "https://" + _credentials + "@ondemand.saucelabs.com/wd/hub"
        config["capabilities"]["sauce:options"]["name"] = test_name
        driver = webdriver.Remote(_url, config["capabilities"])
    else:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

    base_url = config["base_url"]
    driver.get(base_url)

    yield driver
    driver.quit()
