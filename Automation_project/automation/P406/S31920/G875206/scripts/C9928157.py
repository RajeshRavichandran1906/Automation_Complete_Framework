"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 12 Dec 2019
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.wftools.paris_home_page import ParisHomePage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C9928157_TestClass(BaseTestCase):
    
    def test_C9928157(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        Coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        chart = Chart(self.driver)
    
        """
        TESTCASE VARIABLES
        """
        chart_css = "#pfjTableChart_1"
        parent_css = "#pfjTableChart_1"
    
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
        Step 05 Click on 'Chart' action bar under 'InfoAssist' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Chart")
        Coreutils.switch_to_new_window()
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_06 = """
        Step 06 Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0", time_out = 150)
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
        Step 06.01 Verification - Verify that the default Chart is Displayed
        """
        x_axis_labels = ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        chart.verify_x_axis_label_in_preview(x_axis_labels, parent_css, msg = "Step 06.01 : Verify that the default Chart is Displayed")
        utils.capture_screenshot('06.01',STEP_06_01)
        
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