"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 27 May 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9928199_TestClass(BaseTestCase):
    
    def test_C9928199(self):
        
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
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=5)
        OldHomePage.select_property_tab_value('Advanced')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that only the first word and any designated product names are capitalized in the Interactive Reporting Properties as follows:
            1.Prompt for parameters
            2.Enable AutoLinking
            3.AutoLink target
            4.Enable AutoDrill
            5.Run with OLAP (By default disabled)
            6.Use title for deferred report description
            7.Schedule only
            8.Only run as deferred report
            9.Only allow user to run (By default disabled)
            10.Allow user to run (By default disabled)
        """
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Prompt for parameters', "04.01",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Enable AutoLinking', "04.02",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'AutoLink target', "04.03",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Enable AutoDrill', "04.04",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Run with OLAP', "04.05",checkbox="disable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Use title for deferred report description', "04.06",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Schedule only', "04.07",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Only run as deferred report', "04.08",checkbox="enable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Only allow user to run', "04.09",checkbox="disable")
        OldHomePage.verify_label_in_property_dialog('Advanced', 'Allow user to run', "04.10",checkbox="disable")
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