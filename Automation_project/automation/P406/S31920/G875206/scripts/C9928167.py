"""----------------------------------------------------
Author Name : Aftab/Joyal
Automated on : 13 Dec 2019
----------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9928167_TestClass(BaseTestCase):
    
    def test_C9928167(self):
        
        """TESTCASE OBJECTS"""
        
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """TESTCASE VARIABLES"""
        
        alert_css = '#aaTree table>tbody>tr'
        
        Step1 = """
        Step 01.Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00', Step1)

        Step2 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00', Step2)
        
        Step3 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.expand("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00', Step3)
        
        Step4 = """
        Step 04.Click on 'InfoAssist' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        utils.capture_screenshot('04.00', Step4)
        
        Step5 = """
        Step 05.Click on 'Alert' action bar
        Verify 'Alert Assist' window is displayed
        """
        HomePage.Workspaces.ActionBar.select_tab_option('Alert')
        core_utils.switch_to_new_window()
        alert_element = utils.validate_and_get_webdriver_objects(alert_css, 'Alert')
        alert_items = [x.text for x in alert_element]
        del(alert_items[-1])
        expected_alert_list = ['Alert', 'Test', 'Result']
        utils.asequal(expected_alert_list, alert_items, 'Step 05.00: Verify Alert Assist window is displayed')
        core_utils.switch_to_previous_window()
        utils.capture_screenshot('05.00', Step5,expected_image_verify= True)
        
        Step6 = """
        Step 06.In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('06.00', Step6)
        
if __name__ == '__main__':
    unittest.main()