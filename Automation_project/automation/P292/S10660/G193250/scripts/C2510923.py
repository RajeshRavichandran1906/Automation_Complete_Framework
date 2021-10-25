'''
Created on May 09,2019

@author: Niranjan

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2510923
TestCase Name =Verify all headings appears in Settings drop down list
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import base

class C2510923_TestClass(BaseTestCase):

    def test_C2510923(self):
        
        """
        TESTCASE VARIABLES
        """
        breadcrumb_path='P292_S10660->G193250->Charts'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        expected_item_list=['Chart1']
        expected_folder_list=['Insight']
        expected_context_menu_item_list=['Title', 'Name', 'Summary', 'Last modified', 'Created on', 'Size', 'Owner', 'Published','Shown']
        
        """ Step 01:01: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
                
        """Step 02:01: Click on the Content View from the sidebar.
        """
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """ Step 03:01: Expand Domain > 'P292_S10660' domain >'G193250' folder >  Click on Charts folder from the tree
        Verify that still Insight folder and Chart1 appears in List View:
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        utillobj.synchronize_with_visble_text(locator_obj.content_area_css, 'Chart1',base_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_list_view(expected_folder_list, 'asequal', 'Step 03:01(a):Verified that still Insight folder appears in List View')
        main_page_obj.verify_items_in_list_view(expected_item_list,'asequal','Step 03:01(b):Verified that still Chart1 appears in List View')
        
        """Step 04.01:Click on 'Choose Column' button next to the last column heading
        Verify Title, Name, Summary, Last Modified, Created on, Size, Owner, Published and Shown are listed in drop down box
        """
        main_page_obj.select_choose_columns_in_list_view()
        main_page_obj.verify_choose_columns_context_menu_items(expected_context_menu_item_list, 'Step 04.01:Verify Title, Name, Summary, Last Modified, Created on, Size, Owner, Published and Shown are listed in drop down box','asequal')
       
        """ Step 05.01: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        