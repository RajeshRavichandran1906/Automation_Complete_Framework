'''
Created on November 22,2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510929
TestCase Name =Click Title again and verify sort is default sort
'''

import unittest
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
import time

class C2510928_TestClass(BaseTestCase):

    def test_C2510928(self):
        
        """
        TESTCASE VARIABLES
        """
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        core_utils = CoreUtillityMethods(driver)
        locator = WfMainPageLocators()
        arrow_css="div[class*='grid-cell-title'][data-ibxp-text='Title'] div[class*='ibx-label-glyph']"
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, wfmain_obj.home_page_long_timesleep)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain >'G193250' folder > Click on InfoAssist folder from the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path+"->InfoAssist->Reports")
        
        utillobj.synchronize_with_number_of_element(".toolbar .toolbar-button-div [class*='fa fa-list']", 1, wfmain_obj.chart_medium_timesleep)
        
        """ Step 4: Click on Title heading (twice)
            Verify sort arrow appears next to Title pointing up,
            Reporting Objects folder is first and reports sorted in ascending order.
            Report1 (library access list) is next and Report2 (schedule) is last.
        """
        title_icon_elem=utillobj.validate_and_get_webdriver_object(".grid-cell-title:nth-of-type(1)", 'title_icon')
        core_utils.python_left_click(title_icon_elem)
        time.sleep(5)
        title_icon_elem=utillobj.validate_and_get_webdriver_object(".grid-cell-title:nth-of-type(1)", 'title_icon')
        core_utils.python_left_click(title_icon_elem)
        time.sleep(5)
            
        expected_list_items=['Report1', 'Report2']
        expected_list_folders=['Reporting Objects']
        wfmain_obj.verify_folders_in_list_view(expected_list_folders, 'asListEqual', "Step04.1a: Verify the folder lists in order")
        wfmain_obj.verify_items_in_list_view(expected_list_items, 'asListEqual', "Step04.1a: Verify the items lists in order")
        
        arrow_elem=utillobj.validate_and_get_webdriver_object(arrow_css,"title_arrow_css")
        arrow_elem_text=arrow_elem.text
        utillobj.asequal('arrow_upward',arrow_elem_text,"Step 4.1. Verify the Up arrow next to title")
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        