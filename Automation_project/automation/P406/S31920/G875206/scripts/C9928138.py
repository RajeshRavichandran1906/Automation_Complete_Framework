"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 12 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928138_TestClass(BaseTestCase):
    
    def test_C9928138(self):
        
        """
        TESTCASE OBJECTS
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)

        """
        TESTCASE VARIABLES
        """
        cancel_button_css = "#IbfsOpenFileDialog7_btnCancel"
        master_dialog_css = "#dlgIbfsOpenFile7"
        chart_css = "#pfjTableChart_1"
        parent_css = "#pfjTableChart_1"
        
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
            Step 03 : Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
 
        """
            Step 04 : Click on 'INFOASSIST' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        
        """
            Step 05 : Click on 'Chart' action bar under 'InfoAssist' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Chart")
        
        """
            Step 05 : Verification - Verify the Master File Dialog is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        chart.switch_to_new_window()
        chart.wait_for_visible_text(cancel_button_css, "Cancel", time_out = 150)
        utils.verify_object_visible(master_dialog_css, True, "Step 05.01 : Verify the Master File Dialog is displayed")
        
        """
            Step 06 : Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0", time_out = 150)
        
        """
            Step 06 : Verification - sVerify that the default Chart is Displayed
        """
        x_axis_labels = ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        chart.verify_x_axis_label_in_preview(x_axis_labels, parent_css, msg = "Step 06.01 : Verify that the default Chart is Displayed")
        
        """
            Step 07 : Click on IA Globe > Exit
        """
        chart.switch_to_previous_window()
        
        """
            Step 08 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
 
if __name__ == "__main__":
    unittest.main()      