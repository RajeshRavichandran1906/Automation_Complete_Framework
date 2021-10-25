'''
Created on November 22,2018

@author: Magesh

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2510917
TestCase Name = Sign in as developer and verify Grid View
'''

import unittest
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510917_TestClass(BaseTestCase):

    def test_C2510917(self):
        
        """
        TESTCASE VARIABLES
        """
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locator = WfMainPageLocators()
        expected_list=['Alerts', 'Blogs', 'Charts', 'InfoAssist', 'Mode Manager', 'Page Designer', 'Portals', 'Report Library', 'ReportCaster', 'Shortcuts', 'sub1', 'Test Resources', 'Text Editor', 'Uploaded Files', 'URLs', 'Visualizations']

        """ 
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """
        Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, wfmain_obj.home_page_long_timesleep)
        
        """ 
        Step 3: Expand Domain > 'P292_S10660' domain
        Step 4: Click on 'G193250' folder from the tree
        """
        wfmain_obj.click_repository_folder("Domains")
        wfmain_obj.expand_repository_folder('P292_S10660')
        utillobj.synchronize_with_visble_text("div.files-box-files", "G193250", wfmain_obj.home_page_long_timesleep)
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        utillobj.synchronize_with_visble_text("div.files-box-files", "Alert", wfmain_obj.home_page_long_timesleep)
        
        """ 
        Verify all the subfolders appears in the grid view as same in the below screenshot
        """
        wfmain_obj.verify_folders_in_grid_view(expected_list, 'asequal', "Step:4.1")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step:4.2 verify title", label_type='folders')
        
        """ 
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        