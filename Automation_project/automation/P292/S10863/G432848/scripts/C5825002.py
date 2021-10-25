'''
Created on May 09, 2019

@author: Niranjan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5825002
TestCase Name = Verify search for users/groups functionality
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods

class C5825002_TestClass(BaseTestCase):

    def test_C5825002(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        dropdown_css = ".Share-with-menu-btn"
        search_box_css = ".share-with-txt-search .ibx-sm-selectable"
        share_with_css = ".item-user-group .sw-item-desc"
        share_user_name_css = '.item-user-group .sw-item-name'
        cancel_btn_css = ".ibx-dialog-cancel-button"
        workspaces = "Workspaces"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = workspaces+'->P292_S10863_G193429'
        fex_name = 'report1'
        expected_share_user_groups = ['1TestV3 Advanced Users', 'P292_S10660 Advanced Users', 'Retail Samples Advanced User', 'V5 Domain Testing Advanced User 1'] 
        expected_share_user_groups_name = ['1TestV3/AdvancedUsers', 'P292_S10660/AdvancedUsers', 'Retail_Samples/AdvancedUsers', 'qa\\wfpenadv1(wfpenadv1@domain.com)'] 
        
        """
        Step 01:01: Sign in to WebFOCUS as Developer user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 02:01: Expand the domain from the tree and click on 'P292_S10863_G193429'
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'My Content', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03:01: Click on My Content folder > Right click on report1 > Share with...
        """
        main_page_obj.expand_repository_folder(repository_folder+'->'+'My Content')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Share with...')
        util_obj.synchronize_with_visble_text(pop_top_css, 'Share with Others', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04:01: Click on drop-down in the search box > Users/Groups (By default selected) in the drop-down list
        """
        dropdown = util_obj.validate_and_get_webdriver_object(dropdown_css, 'dropdown')
        core_util_obj.python_left_click(dropdown)
        
        """
        Step 05:01: Enter 'adv' in the 'Enter users/groups' search box. 
        Verify users and groups with the name contains 'adv' appears as same in the screenshot:
        """
        search_box = util_obj.validate_and_get_webdriver_object(search_box_css, 'search box')
        core_util_obj.python_left_click(search_box)
        search_box.send_keys("adv")
        util_obj.synchronize_with_visble_text(pop_top_css, 'Advanced', main_page_obj.home_page_medium_timesleep)
        share_users_groups = util_obj.validate_and_get_webdriver_objects(share_with_css, 'share user')
        actual_share_users_groups =[share_user.text for share_user in share_users_groups]
        util_obj.verify_list_values(expected_share_user_groups, actual_share_users_groups, 'Step 05.1: Verified users and groups contains \'adv\' appears as same in the screenshot:', assert_type='asin')
        share_user_groups_names = util_obj.validate_and_get_webdriver_objects(share_user_name_css, 'share user names')
        actual_share_user_groups_names =[share_user_groups_name.text for share_user_groups_name in share_user_groups_names]
        util_obj.verify_list_values(expected_share_user_groups_name, actual_share_user_groups_names, 'Step 05.2: Verified users and groups with the name contains \'adv\' appears as same in the screenshot:', assert_type='asin')
        
        """
        Step 06:01: Click Cancel button to close the Share with Others window.
        """   
        cancel_btn = util_obj.validate_and_get_webdriver_object(cancel_btn_css, 'cancel btn')
        core_util_obj.python_left_click(cancel_btn)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 07:01: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()