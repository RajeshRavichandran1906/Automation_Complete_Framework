from selenium.webdriver.common.by import By
from common.locators.charts import common
from .common import Common, Legend

class Area(Common, Legend):
    
    def __init__(self, parent_locator=common.html5_run_chart):
        
        name = "Area"
        super().__init__(name, (By.CSS_SELECTOR, "path[class^='riser'][class$='marea!']"), parent_locator)
        Legend.__init__(self, name, common.Legend.markers, parent_locator)