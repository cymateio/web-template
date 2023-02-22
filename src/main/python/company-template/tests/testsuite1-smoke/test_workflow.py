import pytest

from pages.web.signin import Signin
from pages.web.main import Main
from pages.web.workspaces import Workspaces

from utils.utilities import *


# TEST SIGNIN PAGE
@pytest.mark.functional
# @pytest.mark.dependency
def test_signin(driver, logger, config):
    signin_page = Signin(driver)
    logger.info("TEST SIGNIN")
    user_data = config["user"]
    signin_page.signin(user_data["username"], user_data["password"])


# # TEST MAIN PAGE
# @pytest.mark.smoke
# # @pytest.mark.dependency(depends=["test_signin"])
# def test_main(driver, logger):
#     logger.info("TEST MAIN")
#     main_page = Main(driver)
#     main_page.navigate_workspace()


# # TEST WORKSPACE PAGE
# @pytest.mark.smoke
# # @pytest.mark.dependency(depends=["test_main"])
# def test_workspace(driver, logger):
#     logger.info("TEST WORKSPACES")
#     workspaces_page = Workspaces(driver)
#     workspaces_page.send_api()
