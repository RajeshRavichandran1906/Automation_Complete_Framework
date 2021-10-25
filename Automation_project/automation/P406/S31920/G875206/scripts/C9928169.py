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

class C9928169_TestClass(BaseTestCase):
    
    def test_C9928169(self):
        
        """
        TESTCASE OBJECTS
        """
        report = Report(self.driver)
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)

        """
        TESTCASE VARIABLES
        """
        schedule_css = "#AddrbookEditor_ribbonTabPane"
        distribution_css = "div[id^='BiTabBar']"
        
        """
            Step 01 : Sign into WebFOCUS Home Page as dev User
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
            Step 04 : Click on 'Schedule' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("SCHEDULE")
        
        """
            Step 05 : Click on 'Distribution List' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Distribution List")
        HomePage.Workspaces.switch_to_default_content()
        report.switch_to_new_window()
        report.wait_for_visible_text(schedule_css, "Distribution List", time_out = 150)
        
        """
            Step 05.01 : Verification - Verify 'Distribution List' window is displayed
        """
        distribution_obj = utils.validate_and_get_webdriver_object(distribution_css, "Distribution css")
        actual_result = distribution_obj.text.strip()
        msg = "Step 05.01 : Verify 'Distribution List' window is displayed"
        utils.asequal(actual_result, "Distribution List", msg)
        
        """
            Step 06 : Close 'Distribution List' window
        """
        core_utils.switch_to_previous_window(window_close = True)
        
        """
            Step 07 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        
if __name__ == "__main__":
    unittest.main()