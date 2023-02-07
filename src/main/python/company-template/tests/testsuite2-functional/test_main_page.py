import pytest

from basetest import BaseTest
from pages.web.signin import Signin
from pages.web.main import Main

from utils.utilities import *

class TestLogin(BaseTest):

    @pytest.mark.functional
    def test_NavigatingToWorkspacesFromMain(self):
        signin_page = Signin(self.driver)
        user_data = get_user_data(self.config)
        signin_page.signin(user_data["username"], user_data["password"])

        main_page = Main(self.driver)
        main_page.navigate_workspace()
        assert "Postman" in self.driver.title
