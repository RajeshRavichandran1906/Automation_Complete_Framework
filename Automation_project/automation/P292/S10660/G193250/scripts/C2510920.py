'''
Created on November 23,2018

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2510920
TestCase Name = Hover over toggle button, verify tooltip is Grid View
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2510920_TestClass(BaseTestCase):

    def test_C2510920(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        domain = 'Domains'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        grid_css=".toolbar .toolbar-button-div [class*='fa fa-th']"
        short_wait = 30
        sleep_time = 5
        
        """ 
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """
        Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(files_box_css,1,45)
        
        """ 
        Step 3: Click on Domain from the tree
        """
        wfmain_obj.select_option_from_crumb_box(domain)
        
        """ 
        Step 4: Hover the mouse to the grid view toggle button
        Verify the tooltip as 'Grid View'
        """
        utillobj.synchronize_with_number_of_element(grid_css, 1, short_wait)
        wfmain_obj.select_list_view()
        grid_view_css=".toolbar .toolbar-button-div [data-ibxp-glyph-classes^='fa fa-th']"
        grid_view_description="grid view toggle button is displayed under toolbar"
        grid_view_btn=utillobj.validate_and_get_webdriver_object(grid_view_css, grid_view_description)
        status = grid_view_btn.is_displayed()
        utillobj.asequal(status, True, "Step:4 Hover the mouse to the list view toggle button - 'Grid View' button displayed")
        utillobj.click_on_screen(grid_view_btn, 'middle')
        actual_title = grid_view_btn.get_attribute('title')
        expected_title="Grid view"
        utillobj.asequal(expected_title, actual_title, "Step:4 Verify the tooltip as 'Grid View'")
        time.sleep(sleep_time)
        
        """ 
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        