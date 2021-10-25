'''
Created on November 22,2018

@author: Vpriya

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510921
TestCase Name =Open sub folder,verify folder and chart appear in Grid View
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510921_TestClass(BaseTestCase):

    def test_C2510921(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        expected_list=['Insight']
        expected_item_list=['Chart1']
        
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(files_box_css,1,45)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain and Click on 'G193250' folder
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        
        """ Step 4: Double click 'Charts' in the content area
            Verify Insight folder and Chart1 appears in Grid View:
        """
        wfmain_obj.double_click_folder_item_and_select_menu('Charts')
        wfmain_obj.verify_folders_in_grid_view(expected_list, 'asequal',"Step:4")
        wfmain_obj.verify_items_in_grid_view(expected_item_list,'asequal',"Step:4.1")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list,"Step 4.2 verify title",label_type='folders')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        