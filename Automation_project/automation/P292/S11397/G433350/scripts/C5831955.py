'''
Created on August 07, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5831955
TestCase Name = Verify context menus for Page Templates (Legacy)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility
from common.pages import wf_mainpage as wfmain_pages
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C5831955_TestClass(BaseTestCase):

    def test_C5831955(self):
        
        """
        TESTCASE VARIABLES
        """
        content_box_css=".explore-box .content-box"
        context_pop_css="[data-ibx-type='ibxMenu'].ibx-popup:not([class*='pop-closed'])"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        mainpage_obj = wfmain_pages.Wf_Mainpage(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """ Step 2: Click Domains from Resource bar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        wfmain_obj.click_repository_folder('Domains')
        
        """ Step 3: Collapse Domains if Domains is expanded.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 4: Expand Global Resources node and Right click on Page Templates Legacy folder.
                    Verify that following options are displayed:
                    1.Expand.
                    2.Refresh.
                    3.Security 
                    --> Rules
                    --> Rules on this resources..
                    --> Effective policy...
                    4.Properties.
        """
        mainpage_obj.expand_repository_folders('Global Resources')
        wfmain_obj.verify_repository_folder_context_menu('Page Templates (Legacy)', ['Expand', 'Refresh', 'Security', 'Properties'], msg='Step 4: Verify that following options are displayed', verification_state='collapse')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 4.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        utillobj.wait_for_page_loads(10)
        
        """ Step 5: Expand Page Templates Legacy folder > Select Standard sub-folder > right click on "1 Column" page.
                    Verify that following options are displayed:
                    1.Copy (Ctrl+C)
                    2.Security 
                    --> Rules
                    --> Rules on this resources..
                    --> Effective policy...
                    3.Properties.
        """
        utillobj.synchronize_with_visble_text('#files-box-area', 'Standard', Global_variables.mediumwait)
        wfmain_obj.verify_repository_folder_item_context_menu('1 Column', ['Copy Ctrl+C', 'Security', 'Properties'], folder_path='Page Templates (Legacy)->Standard', msg='Step 5')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 5.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 6: Expand Standard sub-folder and right click on Resources.
                    Verify that following options are displayed:
                    1.Expand.
                    2.Refresh.
                    3.Security 
                    --> Rules
                    --> Rules on this resources..
                    --> Effective policy...
                    4.Properties.
        """
        mainpage_obj.expand_repository_folders('Standard')
        wfmain_obj.verify_repository_folder_context_menu('Resources', ['Expand', 'Refresh', 'Security', 'Properties'], msg='Step 6: Verify that following options are displayed', verification_state='collapse')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 6.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        utillobj.wait_for_page_loads(10)
        
        """ Step 7: Click on Resources folder and right click on "1 Column" from the content area.
                    Verify that the following options are displayed:
                    1.View.
                    2.View in new window.
                    3.Copy (Ctrl+C)
                    4.Security 
                    --> Rules
                    --> Rules on this resources..
                    --> Effective policy...
                    5.Properties.
        """
        wfmain_obj.verify_repository_folder_item_context_menu('1 Column', ['View', 'View in new window', 'Copy Ctrl+C', 'Security', 'Properties'], folder_path='Resources', msg='Step 7')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 7.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 8: Right click on Custom folder under resource tree.
                    Verify that the following options are displayed:
                    1.Expand.
                    2. Paste Ctrl+V.
                    3.Refresh.
                    4.Security 
                    --> Rules
                    --> Rules on this resources..
                    --> Effective policy...
                    5.Properties.
        """
        wfmain_obj.verify_repository_folder_context_menu('Custom', ['Expand', 'Paste Ctrl+V', 'Refresh', 'Security', 'Properties'], msg='Step 8: Verify that following options are displayed', verification_state='collapse')
        mainpage_obj.select_context_menu_item('Security')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element(context_pop_css, 2, 19)
        mainpage_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...'], msg="Step 8.1: Verify that the following options 'Rules...', 'Rules on this resource...', 'Effective policy...' are displayed under Security.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 9: Revert back the Home page to its default by clicking Domains under repository tree.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()