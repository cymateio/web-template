import time
import pytest

from pages.web.signin import Signin
from pages.web.main import Main
from pages.web.workspaces import Workspaces


from utils.utilities import *


### TEST SIGNIN PAGE
@pytest.mark.smoke
@pytest.mark.dependency
def test_signin(driver, config):
    signin_page = Signin(driver)
    user_data = config["user"]
    signin_page.signin(user_data["username"], user_data["password"])


### TEST MAIN PAGE
@pytest.mark.smoke
@pytest.mark.dependency(depends=["test_signin"])
def test_main(driver):
    main_page = Main(driver)
    main_page.navigate_workspace()


### TEST WORKSPACE PAGE
@pytest.mark.smoke
@pytest.mark.dependency(depends=["test_main"])
def test_workspace(driver):
    workspaces_page = Workspaces(driver)
    workspaces_page.send_api()


