from selenium.webdriver.common.by import By
from common.locators.charts import common, bar
from .common import Common, Legend

class Bar(Common, Legend):
    
    def __init__(self, parent_locator=common.html5_run_chart):
        
        name = "Bar"
        super().__init__(name, (By.CSS_SELECTOR, "rect[class^='riser'][class$='bar!']"), parent_locator)
        Legend.__init__(self, name, common.Legend.markers, parent_locator)
        
    def verify_frame_color(self, color, step, attribute='fill'):
        """
        Description: verify bar chart frame color 
        :Usage - verify_frame_color('bar_blue;, '01')
        """
        frame = self._utils.validate_and_get_webdriver_object_using_locator(bar.Bar.content_frame, 'Content frame', parent_object=self._parent_object)
        msg = "Step {0} : Verify content frame color".format(step)
        self._webelement.verify_element_color_by_css_property(frame, attribute, color, msg, self._name + " Frame")