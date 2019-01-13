import os, sys
from time import sleep
sys.path.append(os.getcwd())
import pytest
from base.base_driver import init_driver
from page.page_001 import Page_001
from base.base_read import readfile
class Test_web():

    def setup(self):

        self.driver = init_driver()
        self.test = Page_001(self.driver)

    @pytest.mark.parametrize("para", readfile())
    def test001(self, para):
        self.test.click_sign()
        username = para["username"]
        password = para["password"]
        text = para["assert"]
        num = para["num"]
        self.test.send_user(username)
        self.test.send_password(password)
        sleep(5)
        self.test.click_sign_in()
        assert self.test.is_text(text, num)
        sleep(5)


    def teardown(self):
        self.driver.quit()
