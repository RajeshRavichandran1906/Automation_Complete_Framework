"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 11 Dec 2019
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods

class C9928132_TestClass(BaseTestCase):
    
    def test_C9928132(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """TESTCASE VARIABLES"""
        
        ACTION_BAR_TAB_LIST = ['DATA', 'APPLICATION', 'INFOASSIST', 'SCHEDULE', 'OTHER']
        DATA_TAB_OPTION  =    ['Reporting Object']
        APPLICATION_TAB_OPTION =  ['Portal']
        INFOASSIST_TAB_OPTION = ['Chart', 'Visualization', 'Report', 'Document', 
                                 'Sample Content', 'Alert']
        SCHEDULE_TAB_OPTION = ['Access List', 'Distribution List', 'Schedule']
        OTHER_TAB_OPTION = ['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 
                            'Portal Page', 'Collaborative Portal']
        
        
        STEP_01 = """
        Step 01.Sign into WebFOCUS as Administrator.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_03_01 = """
        Step 03.01 Verification - Verify that 5 category buttons (DATA, APPLICATION, INFOASSIST, SCHEDULE and OTHER) 
        are displayed, by default 'DATA category button is selected.
        Step 03.02 Verification - Also, verify that 'Reporting Object' action bars is displayed under DATA category
        """
        HomePage.Workspaces.ActionBar.verify_tabs(ACTION_BAR_TAB_LIST,'03.01')
        HomePage.Workspaces.ActionBar.verify_selected_tab(['DATA'],'03.02')
        HomePage.Workspaces.ActionBar.verify_tab_options(DATA_TAB_OPTION,'03.03')
        utils.capture_screenshot('03.01',STEP_03_01,expected_image_verify=True)
        
        STEP_04 = """
        Step 04:Click on 'APPLICATION' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('APPLICATION')
        utils.capture_screenshot('04.00',STEP_04)

        STEP_04_01 = """
        Step 04.01 Verification - Verify that 'Portal' is displayed under APPLICATION category
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(APPLICATION_TAB_OPTION,'04.01')
        utils.capture_screenshot('04.01',STEP_04_01,expected_image_verify=True)

        STEP_05 = """
        Step 05 Click on 'INFOASSIST' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('INFOASSIST')
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05:01 Verification - Verify 6 Action Bar ( Chart, Visualization, Report, 
        Document, Sample content, Alert) are displayed
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(INFOASSIST_TAB_OPTION,'05.01')
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)

        STEP_06 = """
        Step 06 Click on 'SCHEDULE' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('SCHEDULE')
        utils.capture_screenshot('Step 06.00',STEP_06)
        
        STEP_06_01 = """
        Step 06.01 Verification - Verify 3 Action Bar ( Access List, Distribution List, 
        Schedule) are displayed
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(SCHEDULE_TAB_OPTION,'06.01')
        utils.capture_screenshot('06.01',STEP_06_01,expected_image_verify=True)

        STEP_07 = """
        Step 07 Click on 'OTHER' category buttons
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
        Step 07.01 Verification - Verify 8 Action Bar (Folder, Upload File, 
        URL, Shortcut, Text Editor, Blog, Portal Page,Collaborative Portal) are displayed
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(OTHER_TAB_OPTION,'07.01')
        utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Step 8 In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00',STEP_08)