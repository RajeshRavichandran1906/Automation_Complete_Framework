from common.locators.loginpage_locators import LoginPageLocators
import time
from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self,driver):
        self.driver=driver

class LoginPage(BasePage):
    """ Inherit attributes of the parent class=Baseclass """
    def is_title_mathces(self):
        return "Sign In" in self.driver.title

    def click_login(self):
        """
        Triggers login to webfocus
        """
        usename= self.driver.find_element(*LoginPageLocators.uname)
        usename.send_keys("admin")
        passwd =self.driver.find_element(*LoginPageLocators.pword)
        passwd.send_keys("admin")
        sign_in =self.driver.find_element(*LoginPageLocators.submit)
        sign_in.click()

    def login_BUE(self, username, password):
        usename= self.driver.find_element(*LoginPageLocators.uname)
        usename.send_keys(username)
        passwd =self.driver.find_element(*LoginPageLocators.pword)
        passwd.send_keys(password)
        sign_in =self.driver.find_element(*LoginPageLocators.submit)
        sign_in.click()
        time.sleep(4)
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                continue_to_login.click()
        except NoSuchElementException:
            return False

