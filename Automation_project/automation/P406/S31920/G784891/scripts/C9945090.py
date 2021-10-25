"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 16 July 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.pages.security_center import Security_Center

class C9945090_TestClass(BaseTestCase):
    
    def test_C9945090(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        SecurityCenter = Security_Center(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Administrator.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on the 'Settings' icon in the Banner link.
        """
        HomePage.Banner.click_settings()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on 'Security Center
        """
        HomePage.ContextMenu.select('Security Center')
        HomePage.Home._core_utils.switch_to_new_window(window_maximize=False)
        HomePage.Home._utils.synchronize_with_visble_text("#SecurityManagerDialog_tabUserGroups", "Users", 120)
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify Security Center window opens in a new window appears outside of the main browser.
        """
        HomePage.Home._utils.asequal('Security Center', self.driver.title, 'Step 03.01 : Verify "security center" new window opens')
        HomePage.Home._utils.capture_screenshot('03.01',STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Maximize the Security Center window.
        """
        self.driver.maximize_window()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify Security Center window gets maximized
        """
        status = self.driver.execute_script("return window.innerWidth == window.screen.width")
        HomePage.Home._utils.asequal(True, status, "STEP 04.01 : Verify Security Center window gets maximized")
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05.00 : Create five new users and assign to its corresponding Workspaces/group:
            1.SC_Admin assign to Administrators.
            2.SC_Basic assign to Retail_Samples/BasicUsers.
            3.SC_Advanced assign to Retail_Samples/Advanced Users.
            4.SC_Developer assign to Retail_Samples/Developers.
            5.SC_Groupadmin assign to Retail_Samples/GroupAdmins.
            STEP 05.01 : Verify the users are added to their respective groups.
        """
        users = {
            'SC_Admin' : 'Administrators',
            'SC_Basic' : 'Retail_Samples->BasicUsers',
            'SC_Advanced' : 'Retail_Samples->AdvancedUsers',
            'SC_Developer' : 'Retail_Samples->Developers',
            'SC_Groupadmin' : 'Retail_Samples->GroupAdmins'
        }
        for user, groups in users.items():
            SecurityCenter.create_user_(user , btn='ok')
            SecurityCenter.add_user_to_group(user.lower(), groups, [user.lower()], 'Step 05.01', collapse_group=False)
        HomePage.Home._utils.capture_screenshot('05.00' ,STEP_05)
        
        STEP_06 = """
            STEP 06 : Click close to close the Security Center window.
        """
        SecurityCenter.close_security_center_window()
        HomePage.Home._core_utils.switch_to_previous_window(False)
        HomePage.Home._utils.capture_screenshot('06.00' ,STEP_06)
        
        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)