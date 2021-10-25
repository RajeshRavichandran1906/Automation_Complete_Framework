'''
Created on November 23,2018

@author: Magesh

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2510919
TestCase Name = Verify content area toggles from Grid View to List View
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510919_TestClass(BaseTestCase):

    def test_C2510919(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        list_title_css="div[class*='files-box-files-title ibx-widget']"
        expected_folder_list=['Alerts', 'Blogs', 'Charts', 'InfoAssist', 'Mode Manager', 'Page Designer', 'Portals', 'Report Library', 'ReportCaster', 'Shortcuts', 'sub1', 'Test Resources', 'Text Editor', 'Uploaded Files', 'URLs', 'Visualizations']
        expected_title_list=['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        short_wait = 30
        
        """ 
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """
        Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(files_box_css,1,short_wait)
        
        """ 
        Step 3: Expand Domain > 'P292_S10660' domain
        Step 4: Click on 'G193250' folder from the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        
        """
        Step 5: Click on toggle list button to switch to list view
        """
        wfmain_obj.select_list_view()
        
        """ 
        Verify that all the subfolders are displayed in the list view as same in the screenshot
        """
        utillobj.synchronize_with_number_of_element(list_title_css, 1, short_wait)
        wfmain_obj.verify_folders_in_list_view(expected_folder_list, 'asequal', "Step:5")
        wfmain_obj.verify_list_view_title_labels(expected_title_list,"Step 5: Verify list view title")
        wfmain_obj.select_grid_view()
        
        """ 
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        