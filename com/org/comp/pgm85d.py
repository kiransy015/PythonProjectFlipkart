import unittest
from selenium.webdriver import Chrome

class TestGoogle(unittest.TestCase):

    def test_gmail_link_of_google(self):
        driver = Chrome("G:\Kiran\Softwares\Python\chromedriver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com/")
        status = driver.find_element_by_xpath("//a[text()='Gmail']").is_enabled()
        print("Gmail is enabled?:",status)
        assert status
        driver.close()

    def test_search_textbox_of_google(self):
        driver = Chrome("G:\Kiran\Softwares\Python\chromedriver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com/")
        print("Max length :",driver.find_element_by_xpath("//input[@name='q']").get_attribute("maxlength"))
        driver.find_element_by_xpath("//input[@name='q']").send_keys("Java and Python")
        print("Search box value :",driver.find_element_by_xpath("//input[@name='q']").get_attribute("value"))
        driver.close()


