'''
Created on May 10, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5825021
TestCase Name = Verify a group can be added to existing user
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods


class C5825021_TestClass(BaseTestCase):

    def test_C5825021(self):
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
        user_css = ".pop-top [data-ibx-name*='User']"
        search_box_css = ".share-with-txt-search .ibx-sm-selectable"
        share_user_css = ".item-user-group .sw-item-desc"
        share_user_name_css = '.item-user-group .sw-item-name'
        share_data_css = ".item-user-group"
        close_icon = ".pop-top .sw-close-button"
        ok_btn_css = ".ibx-dialog-ok-button"
        sharing_data_css = ".share-with-item"
        workspaces = "Workspaces"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = workspaces + '->P292_S10863_G193429'
        fex_name = 'report1'
        expected_font = ['font-weight:bold;']
        expected_sharing_data = ['autoadvuser04 autoadvuser04(auto@devmail.com)']
        
        """
        Step 1: Sign in to WebFOCUS as Developer user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from the sidebar
        """ 
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand the domain from the tree and click on 'P292_S10863_G193429'
        """  
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'My Content', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on My Content folder from the resource tree > Right click on report1 > Select Share with...
        """
        main_page_obj.expand_repository_folder(repository_folder+'->'+'My Content')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Share with...')
        util_obj.synchronize_with_visble_text(pop_top_css, 'Share with Others', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on drop-down in the search box > Choose Users in the drop-down list.
        """
        dropdown = util_obj.validate_and_get_webdriver_object(dropdown_css, 'dropdown')
        core_util_obj.python_left_click(dropdown)
        user = util_obj.validate_and_get_webdriver_object(user_css, 'user')
        core_util_obj.python_left_click(user)
        
        """
        Step 6: Enter Domain advanced user name in the 'Enter users' search box > Click on Domain advanced user.
        Verify under 'Shared with' it shows the domain advanced user name as in bold with x icon and 'Enter users' search box is empty
        """
        search_box = util_obj.validate_and_get_webdriver_object(search_box_css, 'search box')
        core_util_obj.python_left_click(search_box)
        search_box.send_keys("autoadvuser04")
        util_obj.synchronize_with_visble_text(pop_top_css, 'mail', main_page_obj.home_page_medium_timesleep)
        share_data = util_obj.validate_and_get_webdriver_object(share_data_css, 'share data')
        core_util_obj.python_left_click(share_data)
        util_obj.synchronize_with_visble_text(pop_top_css, 'mail', main_page_obj.home_page_medium_timesleep)
        sharing_data = util_obj.validate_and_get_webdriver_object(sharing_data_css, 'shareing data').text
        actual_sharing_data = sharing_data.replace('\n', ' ')
        util_obj.verify_list_values(expected_sharing_data, [actual_sharing_data], 'Step 6.1: Verify under Shared with still it shows users and description')
        user_name = util_obj.validate_and_get_webdriver_object(share_user_css, 'user name')
        actual_font = util_obj.get_element_attribute(user_name, 'style')
        actual_font = actual_font.replace(' ', '')
        util_obj.verify_list_values(expected_font, [actual_font], 'Step 6.2: Verify under Shared with still it shows autoadvuser04 name as in bold')
        user_desc = util_obj.validate_and_get_webdriver_object(share_user_name_css, 'user_desc')
        actual_font = util_obj.get_element_attribute(user_desc, 'style')
        util_obj.verify_list_values([''], [actual_font], 'Step 6.3: Verify autoadvuser04(auto@devmail.com) description as in normal text')
        search_box_text = search_box.text
        util_obj.verify_list_values([''], [search_box_text], 'Step 6.4: Verify Enter users search box is empty')
        util_obj.verify_element_visiblty(element_css=close_icon, msg="Step 6.5: Verify x icon is visible")
        
        """
        Step 7: Click OK
        Verify Share with Others window closed
        """   
        ok_btn = util_obj.validate_and_get_webdriver_object(ok_btn_css, 'ok btn')
        core_util_obj.python_left_click(ok_btn)
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_medium_timesleep)
        util_obj.verify_element_visiblty(element_css=pop_top_css, visible=False, msg='Step 7.1: Verify Share with Others window closed')
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()