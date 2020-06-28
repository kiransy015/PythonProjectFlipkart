from com.org.comp.lib.util import timeout_handlers

class loginPage():
    def __init__(self,driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        timeout_handlers.wait_element_to_be_visible(self.driver,self.driver.find_element_by_xpath("(//span[text()='Login'])[1]"))

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='_39M2dM JB4AMj']/input[@type='text']")
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='_39M2dM JB4AMj']/input[@type='password']")
        except:
            return None

    def get_login_Btn(self):
        try:
            return self.driver.find_element_by_xpath("(//button[@type='submit'])[2]")
        except:
            return None

