"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 12 Dec 2019
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.wftools.paris_home_page import ParisHomePage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C9928158_TestClass(BaseTestCase):
    
    def test_C9928158(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        visual = Visualization(self.driver)
        Coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        cancel_button_css = "#IbfsOpenFileDialog7_btnCancel"
        master_dialog_css = "#dlgIbfsOpenFile7"
        visual_css = "#pfjTableChart_1"
    
        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as dev User.
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00',STEP_01)

        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Step 04 Click on 'InfoAssist' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('INFOASSIST')
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
        Step 05 Click on 'Visualization' action bar under 'InfoAssist' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Visualization")
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05.01 Verify the Master File Dialog is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        Coreutils.switch_to_new_window()
        visual.wait_for_visible_text(cancel_button_css, "Cancel", time_out = 150)
        utils.verify_object_visible(master_dialog_css, True, "Step 05.01 : Verify the Master File Dialog is displayed")
        utils.capture_screenshot('05.01',STEP_05_01)
        
        STEP_06 = """
        Step 06 Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        visual.wait_for_visible_text(visual_css, "Drop", time_out = 150)
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
        Step 06.01 Verification - Verify that default Visualization is Displayed.
        """
        visual.verify_number_of_risers("#pfjTableChart_1 rect", 3, 4, "Step 06.01")
        utils.capture_screenshot('06.01',STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """
            Step 07 : Click on IA Globe > Exit
        """
        Coreutils.switch_to_previous_window()
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_08 = """
        Step 08  In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00',STEP_08)