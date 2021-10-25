from selenium.webdriver.common.by import By
from common.locators.charts import common, map
from .common import Common, Legend

class Map(Common, Legend):
    
    def __init__(self, parent_locator=common.html5_run_chart):
        
        name = "Map"
        super().__init__(name, (By.CSS_SELECTOR, "[class^='riser'][class$='mregion!']"), parent_locator)
        Legend.__init__(self, name, common.Legend.markers, parent_locator)
        self._locators = map.Map
        
    def verify_legend_title(self, expected_title, step_num):
        """
        Description: This function will verify map legend titles
        :Usage - verify_legend_title(['Revenue'], '01.01')
        """
        self._webelement.verify_elements_text(self._locators.legend_title, expected_title, step_num, "Map legend titles", parent_instance=self._parent_object)
    
    def verify_legend_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description: This function will verify map legend lables
        :Usage - verify_legend_lables(['Revenue'], '01.01')
        """
        self._webelement.verify_elements_text(self._locators.legend_lables, expected_labels, step_num, 'Map Legend lables', assert_type, label_len, slicing, self._parent_object)
    
    def verify_map_title(self, expected_title, step_num):
        """
        Description: This function will verify map title
        :Usage - verify_map_title(['Revenue'], '01.01')
        """
        self._webelement.verify_elements_text(self._locators.map_title, expected_title, step_num, "Map title", parent_instance=self._parent_object)
    
    def verify_scale_title(self, expected_title, step_num):
        """
        Description: This function will verify scale title
        :Usage - verify_scale_title(['Revenue'], '01.01')
        """
        self._webelement.verify_elements_text(self._locators.scale_title, expected_title, step_num, "Scale title", parent_instance=self._parent_object)
    
    def verify_scale_values(self, expected_values, step_num):
        """
        Description: This function will verify scale values
        :Usage - verify_scale_values(['Revenue'], '01.01')
        """
        self._webelement.verify_elements_text(self._locators.scale_values, expected_values, step_num, "Scale values", parent_instance=self._parent_object)
    