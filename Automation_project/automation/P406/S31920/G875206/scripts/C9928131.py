"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 03 June 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods

class C9928131_TestClass(BaseTestCase):
    
    def test_C9928131(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage    =  ParisHomePage(self.driver)
        OldHomePage =  Wf_Mainpage(self.driver)
        utilobj     =   UtillityMethods(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        property_dialog_titlebar=".propPage .properties-page-label .ibx-label-text"
        properties_close_button_css=".properties-page.propPage .properties-page-close-button [class*='close']"
        property_tablist=['General', 'Advanced', 'Server']
        expected_tab_options=['Workspace', 'Folder']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Administrator
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right click on 'Retail Samples' workspace from repository tree > Click on 'Properties'
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples')
        HomePage.Workspaces.ResourcesTree.right_click('Retail Samples')
        HomePage.ContextMenu.select('Properties')
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=5)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that Properties dialog box opens with the following options:
            1.Title as 'Retail Samples' at the top of the dialog with the X button at the right corner of the dialog box.
            2.Three tabs are available (General, Advanced and Server tabs).
            3.By default 'General' tab is selected.
            4.By default Save button is disabled and Cancel button is enabled.
        """
        utilobj.verify_element_text(property_dialog_titlebar, "Retail Samples", "Step 03.01 : Verify Property dialog title bar")
        utilobj.verify_element_visiblty(element_css=properties_close_button_css, visible=True, msg="Step 03.01 : Verify Property dialog Close button")
        OldHomePage.verify_property_dialog_tab_list(expected_list=property_tablist, msg="Step 03.02 : Verify Property dialog tab list")
        OldHomePage.verify_selected_tab_in_property_dialog(tab_name="General", msg="Step 03.03 : Verify General tab is selected")
        OldHomePage.verify_property_dialog_save_cancel_button_enable_disable(button_name="Save", button_status="disable", msg="Step 03.04 : Verify Save button is diabled")
        OldHomePage.verify_property_dialog_save_cancel_button_enable_disable(button_name="Cancel", button_status="enable", msg="Step 03.04 : Verify Cancel button is enabled")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Click on "Workspaces" from the repository tree
        """
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that Properties dialog box gets closed and Workspace and Folder only appear in the action bar.
        """
        utilobj.synchronize_until_element_disappear(property_dialog_titlebar, 30)
        utilobj.verify_element_visiblty(element_css=property_dialog_titlebar, visible=False, msg="Step 04.01 : Verify Property dialog is closed")
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, "04.01")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)