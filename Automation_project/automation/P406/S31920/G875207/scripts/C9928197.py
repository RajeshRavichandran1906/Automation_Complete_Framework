"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 01 June 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9928197_TestClass(BaseTestCase):
    
    def test_C9928197(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage    =  ParisHomePage(self.driver)
        OldHomePage =  Wf_Mainpage(self.driver)
        
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
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=8)
        OldHomePage.select_property_tab_value('Advanced')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that only the first word and any designated product names are capitalized in the Explorer/Portal Properties as follows
            1.Thumbnail
            2.Sort order
            3.Language
            4.Load in iframe
            5.Default width
            6.Default height
            
        """
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Thumbnail', "04.01")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Sort order', "04.02")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Language', "04.03")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Load in iframe', "04.05")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Default width', "04.06")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Default height', "04.07")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click Cancel to close the Properties window
        """
        OldHomePage.select_property_dialog_save_cancel_button('Cancel')
        HomePage.Home._utils.wait_for_page_loads(5, pause_time=3)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)