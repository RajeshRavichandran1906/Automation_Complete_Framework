"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 13 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage
from common.pages.wf_alert_assist import Wf_Alert_Assist

class C9928148_TestClass(BaseTestCase):
    
    def test_C9928148(self):
        
        """
        TESTCASE OBJECTS
        """
        report = Report(self.driver)
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        aa = Wf_Alert_Assist(self.driver)

        """
        TESTCASE VARIABLES
        """
        alert_css = "#aaTree"
        
        """
            Step 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        
        """
            Step 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        
        """
            Step 03 : Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        
        """
            Step 04 : Click on 'InfoAssist' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        
        """
            Step 05 : Click on 'Alert' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Alert")
        
        """
            Step 05.01 : Verification - Verify 'Alert Assist' window is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        report.switch_to_new_window()
        report.wait_for_visible_text(alert_css, "Alert", time_out = 150)
        aa_tool_elems = self.driver.find_elements_by_css_selector("#aaTree table span")
        aa_tool_values = [el.text.strip() for el in aa_tool_elems]
        alert_tree_item = ['Alert', 'Test', 'Result']
        msg = "Step 05.01 : Verify 'Alert Assist' window is displayed"
        utils.as_List_equal(aa_tool_values, alert_tree_item, msg)

        """
            Step 06 : Close 'Alert Assist' window
        """
        aa.select_aa_tool_menu_item("menu_exit")
        core_utils.switch_to_previous_window(window_close = False)
        
        """
            Step 07 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()

if __name__ == "__main__":
    unittest.main()