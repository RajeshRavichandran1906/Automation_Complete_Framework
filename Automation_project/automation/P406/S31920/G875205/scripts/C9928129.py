"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 11 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928129_TestClass(BaseTestCase):
    
    def test_C9928129(self):
        
        """
        TESTCASE VARIABLES
        """
        HomePage = ParisHomePage(self.driver)
        
        """
            Step 01 : Sign into WebFOCUS Home Page as Dev User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        
        """
            Step 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
         
        """
            Step 03 : Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        
        """
            Step 03 : Verification - Verify that 5 category buttons (DATA, APPLICATION, INFOASSIST, SCHEDULE and OTHER) are displayed, by default 'DATA category button is selected.
            Also, verify that 'Reporting Object' action bars is displayed under DATA category
        """
        expected_tab = ['DATA', 'APPLICATION', 'INFOASSIST', 'SCHEDULE', 'OTHER']
        expected_tab_options = ['Reporting Object']
        HomePage.Workspaces.ActionBar.verify_tabs(expected_tab, "03.01")
        HomePage.Workspaces.ActionBar.verify_selected_tab(["DATA"], "03.02")
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, "03.03")
        
        """
            Step 04 : Click on 'APPLICATION' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        
        """
            Step 04 : verification - Verify that 'Portal' is displayed under APPLICATION category
        """
        expected_tab_options = ['Portal']
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, "04.01")
        
        """
            Step 05 : Click on 'INFOASSIST' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        
        """
            Step 05 : Verification - Verify 6 Action Bar ( Chart, Visualization, Report, Document, Sample content, Alert) are displayed
        """
        expected_tab_options = ['Chart', 'Visualization', 'Report', 'Document', 'Sample Content', 'Alert']
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, "05.01")
        
        """
            Step 06 : Click on 'SCHEDULE' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("SCHEDULE")
        
        """
            Step 06 : Verification - Verify 3 Action Bar ( Access List, Distribution List, Schedule) are displayed
        """
        expected_tab_options = ['Access List', 'Distribution List', 'Schedule']
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, "06.01")
        
        """
            Step 07 : Click on 'OTHER' category buttons
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        
        """
            Step 07 : Verification - Verify 8 Action Bar (Folder, Upload File, URL, Shortcut, Text Editor, Blog, Portal Page,Collaborative Portal) are displayed
        """
        expected_tab_options = ['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal']
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, "07.01")
        
        """
            Step 8 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        
    if __name__ == "__main__":
        unittest.main()