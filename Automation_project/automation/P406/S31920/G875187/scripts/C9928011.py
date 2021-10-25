"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 13 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928011_TestClass(BaseTestCase):
    
    def test_C9928011(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Basic User.
        """
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02)
        
        Step_03 = """
            Step 03 : Click on "Workspaces" in the Resource Tree.
        """
        
        HomePage.Workspaces.ResourcesTree.select('Workspaces')
        utils.capture_screenshot('03.00', Step_03)
         
        Step_04 = """
            Step 04 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Schedule".
        """
        HomePage.Workspaces.ResourcesTree.expand('P406_S31920')
        HomePage.Workspaces.ResourcesTree.select('G784912')
        HomePage.Workspaces.ContentArea.double_click_on_folder('Schedule')
        utils.capture_screenshot('04.00', Step_04)
              
        Step_04 = """
            Step 04 : Right click on "Schedule_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Schedule_Context')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
            Step 04 : Verification - Verify context menu,
            Run.
            Properties.
        """
        expected_menus = ['Run','Properties']
        HomePage.ContextMenu.verify(expected_menus, '04.01')
        utils.capture_screenshot('04.01', Step_04_01, expected_image_verify= True)
        
        Step_05 = """
            Step 05 : Right click on "AccessList_Context" in the content area..
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('AccessList_Context')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
            Step 05 : Verification - Verify context menu,
            View Only.
            Properties..
        """
        expected_menus = ['View Only', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '05.01')
        HomePage.ContextMenu.close()
        utils.capture_screenshot('05.01', Step_05_01, expected_image_verify= True)
        
        Step_06 = """
            Step 06 : Right click on "DistributionList_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('DistributionList_Context')
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """
            Step 06 : Verification - Verify context menu,
            View Only.
            Properties.
        """
        expected_menus = ['View Only', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '06.01')
        utils.capture_screenshot('06.01', Step_06_01, expected_image_verify= True)
        
        Step_07 = """
            Step 7 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('07.00', Step_07)
        
    if __name__ == "__main__":
        unittest.main()