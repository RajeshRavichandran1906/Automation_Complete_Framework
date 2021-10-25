from selenium.webdriver.common.by import By
from common.locators.charts import common
from .common import Common, Legend

class Arc(Common, Legend):
    
    def __init__(self, parent_locator=common.html5_run_chart):
        
        name = "Arc"
        super().__init__(name, (By.CSS_SELECTOR, "path[class^='riser'][class$='mbar!']"), parent_locator)
        Legend.__init__(self, name, common.Legend.markers, parent_locator)