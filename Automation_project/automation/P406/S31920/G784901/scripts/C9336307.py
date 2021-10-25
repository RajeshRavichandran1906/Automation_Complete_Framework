"""-------------------------------------------------------------------------------------------
Author Name  : Prabhakaran
Automated On : 27 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9336307_TestClass(BaseTestCase):
    
    def test_C9336307(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        File = 'Visualization Example'
        
        STEP_01 = """
            STEP 01 : Log into WF as Administrator
        """
        HomePage.invoke_with_login('mridadm', 'mrpassadm')
        HomePage.Banner.close_page_message()
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Check all the Tooltips
            1.WebFOCUS (Tooltip:Home)
            2.My Workspace(Tooltip:My Workspace)
            3.Shared with Me (Tooltip: Share with Me)
            4.Workspaces (Tooltip: Workspaces
            5.Tools(Tooltip:Utilities)
            6.Settings(Tooltip:Settings)
            7.Help(Tooltip:Help)
            8.Account(Tooltip:User)
        """
        home_tooltip = self.driver.find_element(*HomePage.Banner.locators.home).get_attribute('title')
        HomePage.Home._utils.asequal('WebFOCUS Home', home_tooltip, "Step 02.01 : Verify WebFOCUS home tooltip")
        
        my_workspace_tooltip = self.driver.find_element(*HomePage.Banner.locators.my_workspace).get_attribute('title')
        HomePage.Home._utils.asequal('My Workspace', my_workspace_tooltip, "Step 02.02 : Verify MyWorkspace tooltip")
        
        shared_with_me_tooltip = self.driver.find_element(*HomePage.Banner.locators.shared_with_me).get_attribute('title')
        HomePage.Home._utils.asequal('Shared with Me', shared_with_me_tooltip, "Step 02.03 : Verify Shared with me tooltip")
        
        workspaces_tooltip = self.driver.find_element(*HomePage.Banner.locators.workspaces).get_attribute('title')
        HomePage.Home._utils.asequal('Workspaces', workspaces_tooltip, "Step 02.04 : Verify Workspaces tooltip")
        
        utilities_tooltip = self.driver.find_element(*HomePage.Banner.locators.utilities).get_attribute('title')
        HomePage.Home._utils.asequal('Utilities', utilities_tooltip, "Step 02.05 : Verify Utilities tooltip")
        
        settings_tooltip = self.driver.find_element(*HomePage.Banner.locators.settings).get_attribute('title')
        HomePage.Home._utils.asequal('Settings', settings_tooltip, "Step 02.06 : Verify Settingd tooltip")
        
        help_tooltip = self.driver.find_element(*HomePage.Banner.locators.help).get_attribute('title')
        HomePage.Home._utils.asequal('Help', help_tooltip, "Step 02.07 : Verify Help tooltip")
        
        user_tooltip = self.driver.find_element(*HomePage.Banner.locators.user).get_attribute('title')
        HomePage.Home._utils.asequal('User', user_tooltip, "Step 02.08 : Verify User tooltip")
        
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02, True)
        
        STEP_03 = """
            STEP 03 : Click the Workspaces link
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that 'Getting Started' workspace is available
        """
        HomePage.Workspaces.ResourcesTree.select('Getting Started')
        HomePage.Workspaces.ResourcesTree.verify_items(['Getting Started'], '03.01')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, File, 60)
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Run 'Visualization Example' under 'Getting Started'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(File)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Close 'Visualization Example' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : Right-click on 'Visualization Example' > Click on 'Add to Favorites'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(File)
        HomePage.ContextMenu.select('Add to Favorites')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Click the WebFOCUS link (Home tab)
        """
        HomePage.Banner.click_home()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07 : Verify that the 'Visualization Example' is added to Recent and also to Favorites sections
        """
        HomePage.Home.Recents.verify_items([File], '07.01')
        HomePage.Home.Favorites.verify_items([File], '07.02')
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Sign Out
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)