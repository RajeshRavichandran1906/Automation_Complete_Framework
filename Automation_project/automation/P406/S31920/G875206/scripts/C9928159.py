"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 13 Dec 2019
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools.paris_home_page import ParisHomePage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C9928159_TestClass(BaseTestCase):
    
    def test_C9928159(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        report = Report(self.driver)
        Coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        report_css = "#TableChart_1"
    
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
        Step 05 Click on 'Report' action bar under 'InfoAssist' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Report")
        HomePage.Workspaces.switch_to_default_content()
        report.switch_to_new_window()
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_06 = """
            Step 06 : Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        report.wait_for_visible_text(report_css, "Drag", time_out = 150)
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
        Step 06.01 Verification - Verify that default Visualization is Displayed.
        """
        text_obj = utils.validate_and_get_webdriver_object("#TableChart_1", "Report css")
        actual_output = text_obj.text
        msg = "Step 06.01 : Verify IA tool will open"
        utils.asin("Drag and drop", actual_output, msg)
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