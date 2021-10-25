'''
Created on November 22,2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510930
TestCase Name =Click toggle button,verify default sort in grid view
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510930_TestClass(BaseTestCase):

    def test_C2510930(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        default_css=".content-title-buttons .content-title-btn-name .ibx-label-text"
        arrow_css=".content-title-buttons .content-title-btn-arrow .ibx-label-icon"
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(files_box_css,1, wfmain_obj.home_page_medium_timesleep)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain >'G193250' folder > InfoAssist folder > Click on Reports from the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path+"->InfoAssist->Reports")
        
        utillobj.synchronize_with_number_of_element(".toolbar .toolbar-button-div [class*='fa fa-th']", 1, wfmain_obj.home_page_medium_timesleep)
        
        """ Step 4: Click on toggle Grid View button
            Verify sort arrow appears next to Title pointing up,
            Reporting Objects folder is first and reports sorted in ascending order.
            Report1 (library access list) is next and Report2 (schedule) is last.
            
        """
        expected_list_items=['Report1', 'Report2']
        expected_list_folders=['Reporting Objects']
        wfmain_obj.verify_folders_in_grid_view(expected_list_folders, 'asListEqual', "Step04.1a: Verify the folder grid in order")
        wfmain_obj.verify_items_in_grid_view(expected_list_items, 'asListEqual', "Step04.1a: Verify the items grid in order")
        utillobj.synchronize_with_visble_text("div.files-box-files", "Report1", wfmain_obj.home_page_long_timesleep)
        utillobj.verify_element_text(arrow_css, "arrow_upward", 'Step 4. Verify Default sort arrow')
        utillobj.verify_element_text(default_css, "Default sort", 'Step 4. Verify Default sort text')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        