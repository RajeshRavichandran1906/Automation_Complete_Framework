'''
Created on November 22,2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510931
TestCase Name =Click Default Sort, verify items in drop down list
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510931_TestClass(BaseTestCase):

    def test_C2510931(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        item_list=['Default sort', 'Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        default_css=".content-title-buttons .content-title-btn-name .ibx-label-text"
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(files_box_css,1,wfmain_obj.home_page_long_timesleep)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain >'G193250' folder > InfoAssist folder > Click on Reports from the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path+"->InfoAssist->Reports")
        utillobj.synchronize_with_visble_text("div.files-box-files", "Report1", wfmain_obj.home_page_long_timesleep)
        
        """ Step 4: Click on 'Default Sort'
            Verify the following appear in drop down list:
            1.Default Sort
            2.Title
            3.Summary
            4.Last Modified
            5.Size
            6.Published
            7.Shown            
        """
        default_css_elem=utillobj.validate_and_get_webdriver_object(default_css,"default_css")
        utillobj.default_click(default_css_elem, click_option=0)
        utillobj.synchronize_with_number_of_element(".pop-top", 1, wfmain_obj.home_page_long_timesleep)
        menu_items=self.driver.find_elements_by_css_selector(".ibx-popup .ibx-menu-item")
        actual_popup_list=[el.text.strip() for el in menu_items  if el.is_displayed()]
        utillobj.as_List_equal(item_list, actual_popup_list, 'Step 4. Verify popup items under Default sort')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        