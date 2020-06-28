import unittest
from selenium.webdriver import Chrome

class TestGoogle(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome("G:\Kiran\Softwares\Python\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")

    def tearDown(self):
       self.driver.close()

    def test_gmail_link_of_google(self):
        status = self.driver.find_element_by_xpath("//a[text()='Gmail']").is_enabled()
        print("Gmail is enabled?:",status)
        assert status

    def test_search_textbox_of_google(self):
        print("Max length :",self.driver.find_element_by_xpath("//input[@name='q']").get_attribute("maxlength"))
        self.driver.find_element_by_xpath("//input[@name='q']").send_keys("Java and Python")
        print("Search box value :",self.driver.find_element_by_xpath("//input[@name='q']").get_attribute("value"))
