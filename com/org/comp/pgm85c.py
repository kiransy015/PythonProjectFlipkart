import unittest
from selenium.webdriver import Chrome

class TestGoogle(unittest.TestCase):
    driver = Chrome("G:\Kiran\Softwares\Python\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.google.com")
    actual_title = driver.title
    print(actual_title)
    assert actual_title=="Google1"
    driver.close()