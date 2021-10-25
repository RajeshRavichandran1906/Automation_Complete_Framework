'''
Created on March 21, 2019

@author: AA14564
Testcase Name : Open dialog: IBFS error clicking on breadcrumb for shared user folder
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261621
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.webfocus.resource_dialog import Resource_Dialog

class C8261621_TestClass(BaseTestCase):
    
    def test_C8261621(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        wf_locators_obj = WfMainPageLocators()
        res_dialog_obj = Resource_Dialog(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        user_name = core_util_obj.parseinitfile('mrid')
        
        """
        Test case CSS
        """
#         case_id = 'c8261621'
        repository_css = "div[class='ibfs-tree']"
        pop_top_css = ".pop-top"
        
        """
        Test case variables
        """
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
         
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        main_page_obj.expand_repository_folder('Workspaces')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
         
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(wf_locators_obj.content_area_css, 'My Content', main_page_obj.home_page_medium_timesleep)
         
        """
        Step 4: Right Click on 'My Content' folder in content area > select Share
        """
        main_page_obj.right_click_folder_item_and_select_menu('My Content', context_menu_item_path='Share')
         
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
         
        """
        Step 6: Sign into WebFOCUS Home Page as Dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 7: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Workspaces')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(wf_locators_obj.content_area_css, 'Other', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9: Click on 'Other' category button and Click on 'Shortcut' action bar
                Verify New Shortcut dialog box opens
        """
        main_page_obj.select_action_bar_tab('Other')
        util_obj.synchronize_with_visble_text(wf_locators_obj.content_area_css, 'Shortcut', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Shortcut')
        util_obj.synchronize_with_visble_text(pop_top_css, 'Browse', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Click on Browse
                 Verify Select dialog box opens
        """
        main_page_obj.click_button_on_popup_dialog('Browse')
        
        """
        Step 11: Double click on 'Shared Content'
        """
        resource_item_css='{0} #files-box-area'.format(res_dialog_obj.resource_dialog_css)
        util_obj.synchronize_with_visble_text(resource_item_css, 'Shared Content', main_page_obj.home_page_long_timesleep)
        res_dialog_obj.select_resource_from_gridview('Shared Content', selection_type='double')
        
        """
        Step 12: Double click on 'Administrator' and click on Administrator breadcrumb within Select dialog box
                 Verify that no error message is displayed
        """
        util_obj.synchronize_with_visble_text(resource_item_css, user_name, main_page_obj.home_page_long_timesleep)
        res_dialog_obj.select_resource_from_gridview(user_name, selection_type='double')
        crumb_item_css='{0} .sd-tab-page.tpg-selected .sd-toolbar'.format(res_dialog_obj.resource_dialog_css)
        util_obj.synchronize_with_visble_text(crumb_item_css, user_name, main_page_obj.home_page_long_timesleep)
        res_dialog_obj.select_crumb_item(user_name, selection_type='double')
        time.sleep(19)
        elements = util_obj.validate_and_get_webdriver_object('[class="ibx-root ibx-loaded ibx-visible"]  .open-dialog-resources', 'Browse Select dialog box')
        list_items = elements.text.split('\n')
        expected_item = ['Select', 'Workspaces', 'Retail Samples', 'Shared Content', 'autoadmuser02', 'search', 'Title', 'Name', 'Select', 'Cancel']
        util_obj.asequal(list_items, expected_item, 'Step 12.01: Verify that no error message is displayed')
        
        """
        Step 13: Click on Cancel > Cancel
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        util_obj.synchronize_with_visble_text(pop_top_css, 'Cancel', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out 
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()