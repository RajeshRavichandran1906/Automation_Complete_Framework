'''
Created on November 22,2018

@author: Vpriya

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2510926
TestCase Name =Toggle to List View,verify folder and chart appear in List View
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510926_TestClass(BaseTestCase):

    def test_C2510926(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        breadcrumb_path='P292_S10660->G193250->InfoAssist'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        expected_item_list=['Reporting Objects', 'Report1', 'Report2']
        content_area_file_css="#files-box-files-area"
        arrow_css="div[data-ibxp-text=\"Title\"] .ibx-label-icon"
        
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(files_box_css,1,45)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain >'G193250' folder > InfoAssist folder > Click on Reports from the tree
            Verify that Reporting Objects, Report1 and Report2 appear in List View and also verify that no sort arrow appears next to any heading. 
            Reporting Objects folder appears first, Report1 (library access list) is next and Report2 (schedule) is last
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        wfmain_obj.expand_repository_folder('Reports')
        content_area_elem=utillobj.validate_and_get_webdriver_object(content_area_file_css,"content area file css")
        content_area_text=content_area_elem.text.split("\n")
        content_title_list=[]
        for i in content_area_text:
            if 'Report' in i:
                content_title_list.append(i)
        utillobj.asequal(expected_item_list,content_title_list,"Step:3")
        arrow_elem=utillobj.validate_and_get_webdriver_object(arrow_css,"title_arrow_css")
        arrow_elem_text=arrow_elem.text
        utillobj.asequal('',arrow_elem_text,"Step:3.1")
        
        """ Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        