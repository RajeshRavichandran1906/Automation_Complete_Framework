"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 12 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9928140_TestClass(BaseTestCase):
    
    def test_C9928140(self):
        
        """
        TESTCASE OBJECTS
        """
        report = Report(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)

        """
        TESTCASE VARIABLES
        """
        cancel_button_css = "#IbfsOpenFileDialog7_btnCancel"
        master_dialog_css = "#dlgIbfsOpenFile7"
        report_css = "#TableChart_1"
        
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
            Step 04 : Click on 'InfoAssist' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        
        """
            Step 05 : Click on 'Report' action bar under 'InfoAssist' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Report")
        
        """
            Step 05.01 : Verify the Master File Dialog is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        report.switch_to_new_window()
        report.wait_for_visible_text(cancel_button_css, "Cancel", time_out = 150)
        utils.verify_object_visible(master_dialog_css, True, "Step 05.01 : Verify the Master File Dialog is displayed")
        
        """
            Step 06 : Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        report.wait_for_visible_text(report_css, "Drag", time_out = 150)
        
        """    
            Step 06.01 : Verify IA tool will open
        """
        text_obj = utils.validate_and_get_webdriver_object("#TableChart_1", "Report css")
        actual_output = text_obj.text
        msg = "Step 06.01 : Verify IA tool will open"
        utils.asin("Drag and drop", actual_output, msg)
        
        """
            Step 07 : Click on IA Globe > Exit
        """
        report.select_ia_application_menu("exit")
        core_utils.switch_to_previous_window(window_close = False)
        
        """
            Step 8 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()

        
if __name__ == "__main__":
    unittest.main()   