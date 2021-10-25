"""----------------------------------------------------
Author Name  : Robert
Automated on : 13-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946219_TestClass(BaseTestCase):
    
    def test_C9946219(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
       
        """
            TESTCASE VARIABLES
        """
        PORTAL_NAME="V5Portal_Context_Delete"
        PORTAL_LIST=[PORTAL_NAME]
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5Portal_Context_Delete' > Click Delete > Click OK
        """
        HomePage.MyWorkspace.right_click_on_item(PORTAL_NAME)
        HomePage.ContextMenu.select("Delete")
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify 'V5Portal_Context_Delete' portal deleted from the content area.
                        
        """
        HomePage.MyWorkspace.verify_items(PORTAL_LIST, "03.01", 'asnotin')
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)

        STEP_04 = """
            STEP 04.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
