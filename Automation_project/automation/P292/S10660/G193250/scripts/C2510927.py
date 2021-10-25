'''
Created on November 23,2018

@author: Vpriya

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://http://172.19.2.180/testrail/index.php?/cases/view/2510927
TestCase Name =Click Title and verify sort is descending
'''

import unittest
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility

class C2510927_TestClass(BaseTestCase):

    def test_C2510927(self):
        
        """
        TESTCASE VARIABLES
        """
        breadcrumb_path='P292_S10660->G193250->InfoAssist->Reports'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locator = WfMainPageLocators()
        expected_item_list=['Reporting Objects', 'Report2', 'Report1']
        content_area_file_css="#files-box-files-area"
        arrow_css= "div[class*='grid-cell-title'][data-ibxp-text='Title'] div[class*='ibx-label-glyph']"
        title_css="div[class*='grid-cell-title ibx-widget'][data-ibxp-text='Title']"
        
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content View from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, wfmain_obj.home_page_long_timesleep)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain >'G193250' folder > InfoAssist folder > Click on Reports from the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        
        
        """ Step 4: Click on Title heading
            Verify sort arrow appears next to Title pointing down, 
            Reporting Objects folder is first and reports are sorted alphabetically in descending order. Report2 (schedule) is next and Report1 (schedule) is last.
        """
        title_elem=utillobj.validate_and_get_webdriver_object(title_css,"title_css_in_list_view")
        core_utill_obj.python_left_click(title_elem)
        utillobj.synchronize_until_element_is_visible(arrow_css, wfmain_obj.home_page_medium_timesleep)
        content_area_elem=utillobj.validate_and_get_webdriver_object(content_area_file_css,"content area file css")
        content_area_text=content_area_elem.text.split("\n")
        content_title_list=[]
        for i in content_area_text:
            if 'Report' in i:
                content_title_list.append(i)
        utillobj.asequal(expected_item_list,content_title_list,"Step:3")
        arrow_elem=utillobj.validate_and_get_webdriver_object(arrow_css,"title_arrow_css")
        arrow_elem_text=arrow_elem.text
        utillobj.asequal('arrow_downward',arrow_elem_text,"Step:3.1")
        
        """ Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        