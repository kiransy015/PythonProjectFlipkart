import unittest
from com.org.comp.lib.util import  create_driver
from com.org.comp.lib.util import timeout_handlers
from com.org.comp.lib.ui.loginPage import loginPage
import json

class testloginFunc(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login = loginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_verifyLogin(self):
        json_data = json.load(open("/PythonProjectFlipkart\\com\\org\\comp\\lib\\sanity\\test_data\\sample_data.json", mode='r'))
        print("Json data :",json_data)
        self.login.wait_for_login_page_to_load()
        timeout_handlers.wait_element_to_be_visible(self.driver,self.login.get_username_textbox())
        self.login.get_username_textbox().send_keys(json_data.get("email"))
        self.login.get_password_textbox().send_keys(json_data.get("password"))
        self.login.get_login_Btn().click()
