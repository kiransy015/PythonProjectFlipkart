from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def wait_element_to_be_visible(driver,element):
    wait = WebDriverWait(driver,30)
    wait.until(expected_conditions.visibility_of(element))

def wait_element_to_be_clickable(driver,element):
    wait = WebDriverWait(driver,30)
    wait.until(expected_conditions.element_to_be_clickable(element))
