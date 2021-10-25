"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 08 January 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927900_TestClass(BaseTestCase):
    
    def test_C9927900(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        portal_name = "V5 Context Menu Testing1"
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand 'P406_S31920' workspace and Click on 'G875179' folder from the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(portal_name)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Click on 'APPLICATION' category button > Click on 'Portal' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab('APPLICATION')
        HomePage.Workspaces.ActionBar.select_tab_option('Portal')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Enter Title as 'V5 Context Menu Testing1' and Click 'Create' button
        """
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        utils.wait_for_page_loads(30)
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify 'V5 Context Menu Testing1' appear as a folder with the gray dotted line which means it is unpublished
        """
        HomePage.Workspaces.ContentArea.verify_unpublished_folders([portal_name], "05.01")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify=True)
        
        STEP_06 = """
            STEP 06.00 : Right-click on 'V5 Context Menu Testing1' and Select 'Publish'
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.ContextMenu.select('Publish')
        utils.wait_for_page_loads(60)
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify that 'V5 Context Menu Testing1' got published and it is highlighted in blue color
        """
        HomePage.Workspaces.ContentArea.verify_published_folders([portal_name], "06.01")
        HomePage.Workspaces.ContentArea.verify_folder_border_color(portal_name, "06.02")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify=True)
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)