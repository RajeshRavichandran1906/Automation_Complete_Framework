"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 26 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9928471_TestClass(BaseTestCase):
    
    def test_C9928471(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign in to WebFOCUS as Basic User.
        """ 
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand Workpsaces > P406_S31920 > G875163 
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875163")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
        Verify user see 'Breadcrumb Trail and Search' folder.
        """
        HomePage.Workspaces.ContentArea.verify_folders(["Breadcrumb Trail and Search"],'03.01')
        utils.capture_screenshot("03.01", STEP_03_01,expected_image_verify=True)
        
        STEP_04 = """
        Expand Breadcrumb Trail and Search > Retail Samples in the tree
        """
        HomePage.Workspaces.ResourcesTree.select('G875163->Breadcrumb Trail and Search->Retail Samples')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """ Click on Visualizations in tree
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples->Visualizations')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
        Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples > Visualizations". 
        Verify Visualizations is selected in tree and items in Visualizations folder appear in the canvas
        """
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Visualizations",'05.01')
        HomePage.Workspaces.ContentArea.verify_files(['Analytical Dashboard', 'Executive Dashboard', 'Sales by Country and Product', 'Store and Product Profits Over Time'],'05.02')
        utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
            Step 06.00 : Revert back the Home Page by its default state (Click on Workspaces from navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)
        
if __name__ == "__main__":
    unittest.main()