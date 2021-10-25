from abc import abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from common.lib import utillity
from common.lib.global_variables import Global_variables

class BasePage(object):

    def __init__(self, driver):
        #self._validate_page(driver)
        self.driver = driver
        self.shortwait = WebDriverWait(driver, 50)
        self.mediumwait = WebDriverWait(driver, 100)
        self.longwait = WebDriverWait(driver, 250)
        self.report_short_timesleep=50
        self.report_medium_timesleep=100
        self.report_long_timesleep=350
        self.chart_short_timesleep=50
        self.chart_medium_timesleep=100
        self.chart_long_timesleep=380
        self.home_page_short_timesleep=20
        self.home_page_medium_timesleep=90
        self.home_page_long_timesleep=190
        self.add_field_timesleep=15
        self.document_component_timesleep=15
        self.browser = Global_variables.browser_name
        self.tooltip_wait_time = 0.5 if self.browser in ['ie','edge'] else 1
        
    @abstractmethod
    def _validate_page(self, driver):
        return
 
class InvalidPageException(Exception):
    pass
