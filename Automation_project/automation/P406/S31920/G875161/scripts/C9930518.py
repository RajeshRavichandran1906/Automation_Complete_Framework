"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 8th January 2020
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage
from common.lib.core_utility import CoreUtillityMethods

class C9930518_TestClass(BaseTestCase):
    
    def test_C9930518(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
    
        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as Basic
        """
        HomePage.invoke_with_login('mridbas','mrpassbas')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Click on the 'Utilities' icon in the banner link.
        """
        HomePage.Banner.click_utilities()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_02_01 = """Verification-
        Verify the following options are displayed:
        Deferred Status
        Stop Requests
        Magnify Search Page
        """
        HomePage.ContextMenu.verify(['Deferred Status', 'Stop Requests', 'Magnify Search Page'],'02.01')
        utils.capture_screenshot('02.01',STEP_02_01,expected_image_verify=True)
        
        STEP_03 = """
        Step 03.Click on Workspaces tab > Expand 'P406_S31920' > Click on the 'G875161' folder from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G875161')
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Right-click on 'Stop_Request' fex > Select 'Run' > Close the run window
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Stop_Request')
        HomePage.ContextMenu.select("Run")
        HomePage.RunWindow.wait_for_visible()
        HomePage.RunWindow.close()
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
        Click on the 'Utilities' icon > Click on 'Stop Request'
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('Stop Requests')
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """Verification-
        Verify that 'Stop Requests' popup stating '1 request(s) stopped'
        """
        HomePage.ModalDailogs.Alert.verify_title('Stop Requests','05.01')
        HomePage.ModalDailogs.Alert.verify_message("1 request(s) stopped.",'05.02')
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Click the 'OK' button to close the 'Stop Request' popup
        """
        HomePage.ModalDailogs.Alert.OKButton.click()
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_07 = """
        Click on the 'Utilities' icon > Click on 'Deferred Status'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('Deferred Status')
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """Verification-
        Verify the following 'Deferred Report Status' window gets displayed.
        """
        core_utils.switch_to_new_window()
        utils.verify_current_tab_name("Deferred Report Status","Step 07.01 Verify the 'Deferred Report Status' window gets displayed.")
        utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Close the 'Deferred Report Status' window
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot('08.00',STEP_08)
        
        STEP_09 = """
        Click on the 'Utilities' icon > Click on 'Magnify Search Page'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('Magnify Search Page')
        utils.capture_screenshot('09.00',STEP_09)
        
        STEP_09_01 = """Verification-
        Verify the following 'Magnify Search Page' window gets displayed with the URL http://machine_name:port/alias/search
        """
        core_utils.switch_to_new_window()
        utils.verify_current_url('search',"Step 09.01 Magnify Search Page URL")
        utils.capture_screenshot('09.01',STEP_09_01,expected_image_verify=True)
        
        STEP_10 = """
        Close the 'Magnify Search Page' window
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot('10.00',STEP_10)
        
        STEP_11 = """
        In the banner link, click on the top right username > Sign out."""
        HomePage.Banner.sign_out()
        utils.capture_screenshot('11.00',STEP_11)
        
        
if __name__ == "__main__":
    unittest.main() 