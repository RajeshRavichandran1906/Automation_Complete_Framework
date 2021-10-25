"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 11 February 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9928200_TestClass(BaseTestCase):
    
    def test_C9928200(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage    =  ParisHomePage(self.driver)
        OldHomePage =  Wf_Mainpage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        checkbox_css = ".properties-page .properties-advanced-restrict-schedule"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Administrator
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand 'Retail Samples' from the repository tree > Click on 'Charts' Folder in the tree
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples->Charts')
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Right click on 'Bar - Highest Margin Products' > Select Properties > Click Advanced tab
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Bar - Highest Margin Products')
        HomePage.ContextMenu.select('Properties')
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=5)
        OldHomePage.select_property_tab_value('Advanced')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that only the first word and any designated product names are capitalized in the Scheduling and Library Content Properties as follows:
            Restrict schedule to Library only
        """
        checkbox = self.driver.find_element_by_css_selector(checkbox_css)
        HomePage.Home._javascript.scrollIntoView(checkbox, wait_time=4)
        actual_text = checkbox.text.strip()
        HomePage.Home._utils.asequal('Restrict schedule to Library only', actual_text, "Step 04.01 : Verify that only the first word and any designated product names are capitalized in the Scheduling and Library Content")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click Cancel to close the Properties window
        """
        OldHomePage.select_property_dialog_save_cancel_button('Cancel')
        HomePage.Home._utils.wait_for_page_loads(5, pause_time=2)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)