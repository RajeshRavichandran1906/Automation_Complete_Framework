'''
Created on April 4, 2019

@author: varun
Testcase Name : Create folder under portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261625
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.pages.wf_mainpage import Wf_Mainpage as homepage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
import time

class C8261625_TestClass(BaseTestCase):
    
    def test_C8261625(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        homePage_obj = homepage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        
        """
        Test case variables
        """
        action_bar_text = "Action Bar"
        portal_name = 'v5folder1'
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on the Content Sidebar.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'V5 Domain Testing' -> v5portal1;
        Click on Folder tile from Action Bar.
        """
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing->v5portal1')
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Folder')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'New Folder', main_page_obj.report_medium_timesleep)
        
        """
        Step 4: Enter Title as 'v5folder1' and click ok
        """
        main_page_obj.create_new_folder(portal_name)
        
        """
        Step 5: Right click on 'v5folder1' and choose Publish
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Publish')
        for _ in range(90):
            try:
                portal_name_obj = homePage_obj.get_domain_folder_item(portal_name)
                status = portal_name_obj.find_element_by_css_selector('.folder-item-published').is_displayed()
                if status:
                    break
                else:
                    time.sleep(1)
            except:
                continue
        
        """
        Step 6: Right click on 'v5folder1' and choose Properties -> Advanced
        """
        
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Properties')
        util_obj.synchronize_with_visble_text(".properties-page-label", portal_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_property_tab_value('Advanced')
        
        """
        Step 7: Click on ' Allow personal pages' check box
        Verify ' Allow personal pages' check box has been selected
        """
        main_page_obj.edit_property_dialog_value('Allow personal pages', 'checkbox', 'check', tab_name='Advanced')
        allow_pages_obj = util_obj.validate_and_get_webdriver_object(".properties-advanced-create-content", "pages_button")
        allow_pages_attribute = allow_pages_obj.get_attribute('class')
        util_obj.asin('checked', allow_pages_attribute, "Step 7.1: Verify pages is checked")
        
        """
        Step 8: Click save
        """
        main_page_obj.select_property_dialog_save_cancel_button('Save')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_name, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9: Sign Out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()