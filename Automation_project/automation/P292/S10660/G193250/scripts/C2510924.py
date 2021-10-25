'''
Created on May 9 2019

@author: Vpriya

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510926
TestCase Name =Uncheck/Check a heading and verify the columns disappears/appears
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.lib import base

class C2510924_TestClass(BaseTestCase):

    def test_C2510924(self):
        
        """
        TESTCASE VARIABLES
        """
        breadcrumb_path='P292_S10660->G193250->Charts'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        expected_item_list=['Chart1']
        expected_context_menu_item_list=['Title', 'Name', 'Summary', 'Last modified', 'Created on', 'Size', 'Owner', 'Published','Shown']
        choose_context_menu_css="div[class*='pop-top'][data-ibx-type='ibxMenu']"
        expected_list_title=['Title', 'Last modified', 'Size', 'Published', 'Shown']
        expected_list_title_summary=['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        
        """ Step 01: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 02: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """ Step 03: Expand Domain > 'P292_S10660' domain >'G193250' folder >  Click on Charts folder from the tree
        Verify that still Insight folder and Chart1 appears in List View:
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        utillobj.synchronize_with_visble_text(locator_obj.content_area_css, 'Chart1',base_obj.home_page_medium_timesleep)
        wfmain_obj.verify_items_in_list_view(expected_item_list,'asequal','Step 03:Verify that still Insight folder and Chart1 appears in List View:')
        wfmain_obj.verify_folders_in_list_view(['Insight'], 'asequal','Step 03.01:Verify that still Insight folder and Chart1 appears in List View:')
        
        """Step 04:Click on 'Choose Column' button next to the last column heading
        Verify Title, Name, Summary, Last Modified, Created on, Size, Owner, Published and Shown are listed in drop down box
        """
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_context_menu_item_list, 'Step 04:Verify Title, Name, Summary, Last Modified, Created on, Size, Owner, Published and Shown are listed in drop down box','asequal')
        
        """Step 05:Uncheck Summary
           Verify Summary heading does not appear and drop down list remains open 
        """
        wfmain_obj.select_list_view_columns(['Summary'])
        wfmain_obj.verify_list_view_title_labels(expected_list_title,"Step 05:Verify Summary heading does not appear")
        wfmain_obj.verify_choose_columns_context_menu_items(expected_context_menu_item_list, 'Step 04:Verify Title, Name, Summary, Last Modified, Created on, Size, Owner, Published and Shown are listed in drop down box','asequal')
        
        
        """Step 06:Check Summary
        Verify Summary heading appears and drop down list remains open
        """
        wfmain_obj.select_list_view_columns(['Summary'])
        wfmain_obj.verify_list_view_title_labels(expected_list_title_summary,"Step 05:Verify Summary heading does not appear")
        wfmain_obj.verify_choose_columns_context_menu_items(expected_context_menu_item_list, 'Step 04:Verify Title, Name, Summary, Last Modified, Created on, Size, Owner, Published and Shown are listed in drop down box','asequal')
        
        """
        Step 07:Click anywhere outside drop down list
        Verify drop down list closes
        """
        content_area_elem=utillobj.validate_and_get_webdriver_object(locator_obj.content_area_css,'Content_area_css')
        core_utill_obj.left_click(content_area_elem)
        utillobj.verify_object_visible(choose_context_menu_css,False,'Step 7:Verify drop down list closes')
    
       
        """ Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        