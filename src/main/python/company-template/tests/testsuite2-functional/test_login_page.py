import pytest

from basetest import BaseTest
from pages.web.signin import Signin

from utils.utilities import *


class TestLogin(BaseTest):
    @pytest.mark.functional
    def test_LoginToPageAndCheckTitle(self):
        signin_page = Signin(self.driver)
        user_data = self.config["user"]
        signin_page.signin(user_data["username"], user_data["password"])
        assert self.driver.title == "Postman - Sign In"
