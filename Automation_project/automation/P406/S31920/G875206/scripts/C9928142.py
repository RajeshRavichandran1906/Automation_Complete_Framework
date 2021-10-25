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
from common.pages.wf_reporting_object import Wf_Reporting_Object

class C9928142_TestClass(BaseTestCase):
    
    def test_C9928142(self):
        
        """
        TESTCASE OBJECTS
        """
        report = Report(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        ro = Wf_Reporting_Object(self.driver)

        """
        TESTCASE VARIABLES
        """
        cancel_button_css = "#IbfsOpenFileDialog7_btnCancel"
        master_dialog_css = "#dlgIbfsOpenFile7"
        rotree_css = "#roTree"
        popup_css = "div[id^='BiDialog']"
        no_button_css = "div[id^='BiDialog'] div[id^='BiButton'][class='bi-button button']:nth-child(4)"
        
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
            Step 04 : Click on 'Data' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("DATA")
        
        """
            Step 05 : Click on 'Reporting Object' action bar under 'Data' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Reporting Object")
        
        """
            Step 05.01 : Verification - Verify the Master File Dialog is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        report.switch_to_new_window()
        report.wait_for_visible_text(cancel_button_css, "Cancel", time_out = 150)
        utils.verify_object_visible(master_dialog_css, True, "Step 05.01 : Verify the Master File Dialog is displayed")
        
        """
            Step 06 : Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        report.wait_for_visible_text(rotree_css, "Reporting Object", time_out = 150)
        
        """
            Step 06.01 : Verification - Verify Reporting Object tool opens
        """
        ro_items = ['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        ro.verify_ro_tree_item(ro_items, "Step 06.01 : Verify Reporting Object tool opens")
        
        """
            Step 07 :  Click on RO Globe > Exit > No
        """
        ro.select_ro_tool_menu_item("menu_exit")
        report.wait_for_visible_text(popup_css, "No")
        no_button = utils.validate_and_get_webdriver_object(no_button_css, "no button css")
        core_utils.python_left_click(no_button)
        core_utils.switch_to_previous_window(window_close = False)

        """
            Step 08 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
 
if __name__ == "__main__":
    unittest.main()