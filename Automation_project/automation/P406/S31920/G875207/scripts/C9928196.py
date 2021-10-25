"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 03 February 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928196_TestClass(BaseTestCase):
    
    def test_C9928196(self):
        
        """
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        roles_css = "#ruleList .bi-grid-node .col-2"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Administrator
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on the 'Workspaces' in the tree and Right click on 'Retail Samples' in the tree> Security > Select 'Rules on this Resources'
        """
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.right_click("Retail Samples")
        HomePage.ContextMenu.select("Security->Rules on this resource...")
        HomePage.Workspaces._core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(roles_css, 'WebFOCUS', 60)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that only significant words are capitalized in the Role names as same in the below screenshot:
        """
        expected_roles = ['WebFOCUSManagerDomainRestrictions', 'DomainAdvancedUser', 'DomainBasicUser', 'DomainDeveloperRestrictions', 'DomainDeveloper', 'DomainGroupAdminRestrictions', 'DomainGroupAdmin']
        actual_roles = [role.text.strip() for role in self.driver.find_elements_by_css_selector(roles_css)]
        utils.asequal(expected_roles, actual_roles, "Step 03.01 : Verify that only significant words are capitalized in the Role names")
        utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Close the Rules window
        """
        HomePage.Workspaces._core_utils.switch_to_previous_window()
        utils.capture_screenshot("04.00", STEP_04)
         
        STEP_05 = """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)