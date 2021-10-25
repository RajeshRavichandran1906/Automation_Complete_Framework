from selenium.webdriver.common.by import By
from common.locators.charts import common, pie
from .common import Common, Legend

class Pie(Common, Legend):
    
    def __init__(self, parent_locator=common.html5_run_chart):
        
        name = "Pie"
        super().__init__(name, (By.CSS_SELECTOR, "path[class^='riser'][class$='mwedge!']"), parent_locator)
        Legend.__init__(self, name, common.Legend.markers, parent_locator)
        self._parent = parent_locator
        self._locators = pie.Pie
        
    def verify_total_lables(self, expected_lables, step_num):
        """
        Description: This function will verify pie total lables 
        :Usage - verify_total_lables(['1.1B'], '01.01')
        """
        self._webelement.verify_elements_text(self._locators.total_label, expected_lables, step_num, "Pie Total lables", parent_instance=self._parent_object)
        
    def verify_pie_labels(self, expected_lables, step_num): 
        """
        Description: This function will verify pie lables
        :Usage - verify_pie_lables(['Revenue'], '01.02')
        """
        self._webelement.verify_elements_text(self._locators.pie_lables, expected_lables, step_num, "Pie Lables", parent_instance=self._parent_object)
    
    def verify_data_lables(self, expected_lables, step_num):
        """
        Description: This function will verify pie data lables
        :Usage - verify_data_lables(['100%'], '01.02')
        """
        self._webelement.verify_elements_text(self._locators.data_lables, expected_lables, step_num, "Pie Lables", parent_instance=self._parent_object)
        
    