from selenium.webdriver.common.by import By
from common.locators.charts import common, scatter
from .common import Common, Legend

class Scatter(Common, Legend):
    
    def __init__(self, parent_locator=common.html5_run_chart):
        
        name = "Scatter"
        super().__init__(name, (By.CSS_SELECTOR, "circle[class^='riser'][class$='mmarker!']"), parent_locator)
        Legend.__init__(self, name, common.Legend.markers, parent_locator)
        self._locator = scatter.Scatter
        
    def verify_xaxis_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify chart x axis labels 
        Parameters :
            expected_labels = ['0','10','12']
            step_num = example "04.01"
        Usage:
            verify_yaxis_labels(['CAR','COUNTRY'], "04.01")
        """
        name = self._name + " X-Axis Labels"
        self._webelement.verify_elements_text(self._locator.xaxis_label, expected_labels, step_num, name, assert_type, label_len, slicing, parent_instance=self._parent_object)
    