'''
Created on July 31, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5831951
TestCase Name = Verify context menus for Page Templates
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.locators import wf_mainpage_locators
from common.lib import utillity, core_utility
from common.pages import wf_mainpage as wfmain_pages
from common.lib import base

class C5831951_TestClass(BaseTestCase):

    def test_C5831951(self):
        
        """
        TESTCASE VARIABLES
        """
        content_box_css=".explore-box .content-box"
        context_pop_css="[data-ibx-type='ibxMenu'].ibx-popup:not([class*='pop-closed'])"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        mainpage_obj = wfmain_pages.Wf_Mainpage(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        
        """ Step 2: Click Domains from navigation bar.
        """
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """ Step 3: Collapse Domains if Domains is expanded.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 4: Expand Global Resources node and right click on Page Templates folder.
                    Verify that following options are displayed:
                    1.Expand.
                    2.Refresh.
                    3.Security 
                    --> Rules...
                    --> Rules on this resource...
                    --> Effective policy...
                    4.Properties.
        """
        mainpage_obj.expand_repository_folders('Global Resources')
        wfmain_obj.verify_repository_folder_context_menu('Page Templates', ['Expand', 'Refresh', 'Security', 'Properties'], msg='Step 4: Verify that following options are displayed', verification_state='collapse')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 4.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 5: Expand Page Templates folder and right click on Standard sub-folder.
                    Verify that the following options are displayed:
                    1.Expand.
                    2.Refresh.
                    3.Security 
                    --> Rules...
                    --> Rules on this resource...
                    --> Effective policy...
                    4.Properties.
        """
        mainpage_obj.expand_repository_folders('Page Templates')
        wfmain_obj.verify_repository_folder_context_menu('Standard', ['Expand', 'Refresh', 'Security', 'Properties'], msg='Step 5: Verify that following options are displayed', verification_state='collapse')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 5.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 6: Click Standard sub-folder under resource tree and right click on Blank from the content area.
                    Verify that the following options are displayed:
                    1.Copy Ctrl+C
                    2.Security 
                    --> Rules...
                    --> Rules on this resource...
                    --> Effective policy...
                    3.Properties.
        """
        wfmain_obj.verify_repository_folder_item_context_menu('Blank', ['Copy Ctrl+C', 'Security', 'Properties'], msg="Step 6")
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 6.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 7: Right click on Custom sub-folder.
                    Verify that the following options are displayed:
                    1.Expand.
                    2.Paste Ctrl+v (By default greyed out).
                    3.Refresh.
                    4.Security 
                    --> Rules...
                    --> Rules on this resource...
                    --> Effective policy...
                    5.Properties.
        """
        wfmain_obj.verify_repository_folder_context_menu('Custom', ['Expand', 'Paste Ctrl+V', 'Refresh', 'Security', 'Properties'], msg="Step 7", verification_state='collapse')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 7.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 8: Revert back the Home page to its default by clicking Domains under repository tree.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()