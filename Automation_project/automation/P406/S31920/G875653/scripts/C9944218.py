"""-------------------------------------------------------------------------------------------
Author Name : VPriya
Automated On : 07 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944218_TestClass(BaseTestCase):
    
    def test_C9944218(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mradvid", "mradvpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right click on Schedule_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('Schedule_Context')
        utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify context menu,
            Edit.
            Run.
            View log.
            Disable.
            Duplicate.
            Delete DEL.
            Share.
            Share with...
            Properties.
        """
        context_menu = ['Edit', 'Run', 'View log', 'Disable', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'03.01')
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04 : Right click on AccessList_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('AccessList_Context')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify context menu,
            Edit.
            Duplicate.
            Delete DEL.
            Share.
            Share with...
            Properties.
        """
        context_menu = ['Edit', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'04.01')
        HomePage.ContextMenu.close(location = "middle_right", x = 4)
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            STEP 05 : Right click on DistributionList_Context
        """
        HomePage.MyWorkspace.right_click_on_item('DistributionList_Context')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu,
            Edit.
            Duplicate.
            Delete DEL.
            Share.
            Share with...
            Properties.
        """
        context_menu = ['Edit', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'05.01')
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot('06.00', STEP_06)
        

if __name__ == "__main__":
    unittest.main()