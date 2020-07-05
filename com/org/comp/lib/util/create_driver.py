import pytest
import os
from selenium.webdriver import Chrome,Firefox,Ie


def get_browser_instance():
    browser_info = pytest.config.option.browser
    url_info = pytest.config.option.url

    # browser_info = "chrome"
    # url_info = "test"

    print("Browser name :",browser_info)

    fileDir = os.path.dirname(os.path.abspath(__file__))
    libDirPath = os.path.dirname(fileDir)
    comDirPath = os.path.dirname(libDirPath)
    if browser_info.lower()=="chrome":
        driver = Chrome(comDirPath+"\\Browser_servers\\chrome\\chromedriver.exe")
    elif browser_info.lower()=="firefox":
        driver = Firefox(comDirPath+"\\Browser_servers\\chrome\\chromedriver.exe")
    else:
        print("Invalid Browser , please provide correct one")
        return None

    driver.maximize_window()
    driver.implicitly_wait(30)

    if url_info.lower()=="test":
        driver.get("https://www.flipkart.com/")
    elif url_info.lower()=="prod":
        driver.get("https://www.flipkart.com/")

    return driver