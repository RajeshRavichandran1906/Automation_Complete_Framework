from abc import abstractmethod
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):

    def __init__(self, driver):
        #self._validate_page(driver)
        self.driver = driver
        self.shortwait = WebDriverWait(self.driver, 50)
        self.mediumwait = WebDriverWait(self.driver, 100)
        self.longwait = WebDriverWait(self.driver, 250)

    @abstractmethod
    def _validate_page(self, driver):
        return
 
class InvalidPageException(Exception):
    pass
