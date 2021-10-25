"""-------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 09-September-2019
-------------------------------------------------------------"""

from common.lib.core_utility import CoreUtillityMethods
from common.wftools.visualization import Visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.pages import visualization_metadata
import unittest

class C9868056_TestClass(BaseTestCase):
    
    def test_C9868056(self):
        
        """
            CLASS OBJECTS
        """
        visual = Visualization(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
            VARIABLES
        """
        field_path = 'Filters and Variables->Product Filter'
        msg_dialog_css = "div[id^='BiDialog'][style*='inherit']"
        msg_dialog_ok_btn_css = msg_dialog_css + " .bi-button.button-focus"
        expected_msg = "MessageThe field cannot be used to create a filterOK"
        
        """
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2F&master=baseapp%2Fwf_retail_lite&tool=idis
        """
        visual.invoke_visualization_using_api("baseapp/wf_retail_lite")
        visual.wait_for_visible_text("#pfjTableChart_1", "Drop", visual.chart_long_timesleep)
        
        """
            STEP 01 - Expected : Default predefined filter value displayed in data pane
        """
        data_pane_list=['Filters and Variables', 'Product Filter']
        metaobj.verify_all_data_panel_fields(data_pane_list, 'Step 07.01: Verify Data pane is resetted', comparison_type='asin')
        
#         visual.verify_field_listed_under_datatree('Filters and Variables', 'Product Filter', 1, "Step 01.01 ")
        
        """
            STEP 02 : Drag and drop "Product Filter" variable into the Filter pane
        """
        visual.drag_and_drop_from_data_tree_to_filter(field_path, 1)
        visual.wait_for_visible_text(msg_dialog_css, "OK", visual.chart_short_timesleep)
        
        """
            STEP 02 - Expected : It displays warning message
        """
        msg_dialog = utils.validate_and_get_webdriver_object(msg_dialog_css, "Message dialog")
        actual_msg = msg_dialog.text.strip().replace("\n", "")
        utils.asequal(expected_msg, actual_msg, "Step 02.01 : Verify waring message dialog")
        
        """
            STEP 03 : Click OK button.
        """
        msg_dialog_ok_btn = utils.validate_and_get_webdriver_object(msg_dialog_ok_btn_css, "Message dialog ok button")
        core_utils.left_click(msg_dialog_ok_btn)
        utils.synchronize_until_element_disappear(msg_dialog_css, visual.chart_short_timesleep)
        
        """
            STEP 04 : Double click "Product Filter"
        """
        utils.wait_for_page_loads(5, pause_time=5)
        visual.double_click_on_datetree_item(field_path, 1)
        visual.wait_for_visible_text(msg_dialog_css, "OK", visual.chart_short_timesleep)
        
        """
            STEP 04 - Expected : The same warning message displayed
        """
        msg_dialog = utils.validate_and_get_webdriver_object(msg_dialog_css, "Message dialog")
        actual_msg = msg_dialog.text.strip().replace("\n", "")
        utils.asequal(expected_msg, actual_msg, "Step 04.01 : Verify waring message dialog")
        
        """
            STEP 05 : Click OK button.
        """
        msg_dialog_ok_btn = utils.validate_and_get_webdriver_object(msg_dialog_ok_btn_css, "Message dialog ok button")
        core_utils.left_click(msg_dialog_ok_btn)
        utils.synchronize_until_element_disappear(msg_dialog_css, visual.chart_short_timesleep)
        
        """
            STEP 06 : Logout using API. http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()