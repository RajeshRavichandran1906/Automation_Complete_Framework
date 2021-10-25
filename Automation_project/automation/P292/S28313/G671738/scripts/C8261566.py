'''
Created on January 31, 2019

@author: varun
Testcase Name : Test Properties menu using Developers
Testcase ID : lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261566
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import base
from common.lib.core_utility import CoreUtillityMethods


class C8261566_TestClass(BaseTestCase):
    
    def test_C8261566(self):
        """
        Test_case objects
        """
        core_util_obj = CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """
        Test case CSS
        """
        items_css = 'div[data-ibxp-text="Items "] .ibx-label-text'
        properties_title_css = ".properties-page-label .ibx-label-text"
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        user_name = core_util_obj.parseinitfile('mriddev')
        portal_name = 'Portal for Context Menu Testing'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click Favorite View from the sidebar
        """
        main_page_obj.select_favorites_from_sidebar()
        
        """
        Step 4: Right click on 'Portal for Context Menu ...' > Click Properties
        """
        util_obj.synchronize_with_visble_text(items_css, 'Items', main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu( portal_name, 'Properties')
        util_obj.synchronize_with_visble_text(properties_title_css, portal_name, main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_property_dialog_value('Title', 'text_value', portal_name,'Step 4.1: Title verification')
        main_page_obj.verify_property_dialog_value('Name', 'text_value', '2680958774','Step 4.2: Name verification')
        main_page_obj.verify_property_dialog_value('Summary', 'text_area', '','Step 4.3: Summary verification')
        main_page_obj.verify_property_dialog_value('Path', 'text_value', 'IBFS:/WFC/UserInfo/autodevuser88/Favorites/2680958774','Step 4.4: Path verification')
        main_page_obj.verify_property_dialog_value('Target Path', 'text_value', 'IBFS:/WFC/Repository/{0}_{1}/{2}/Portal_for_Context_Menu_Testing'.format(project_id, suite_id, group_id),'Step 4.5: Target Path verification')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Created', user_name, 'Step 4.6: Verify Created')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Modified', user_name, 'Step 4.7: Verify Modified')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Accessed', user_name, 'Step 4.8: Verify Accessed')
        main_page_obj.verify_property_dialog_value('Tool', 'text', '','Step 4.9: Tool verification')
        main_page_obj.verify_property_dialog_value('Owner', 'text', 'autodevuser88','Step 4.10: Owner verification')
        main_page_obj.verify_property_dialog_value('Size', 'text', '-','Step 4.11: Size verification')
        
        """
        Step 5: Click the advanced tab
        Verify that all the options appear under Advanced tab as same in the below screenshot
        """
        main_page_obj.select_property_tab_value("Advanced")
        time.sleep(3)
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', '5.1: Explorer label verification')
        main_page_obj.verify_property_dialog_value('Sort order', 'text_value', '','Step 5.2: Sort Order verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 5.3: Verify View All - is enabled.",tab_name='Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Search Properties', '5.4: Explorer label verification')
        main_page_obj.verify_property_dialog_value('Tags', 'text_value', '','Step 5.5: Tags verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 5.6: Save button disable verfication')
        
        """
        Step 6: Click Cancel to close the properties dialog box
        """
        main_page_obj.select_property_dialog_save_cancel_button('Cancel')
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        

if __name__ == '__main__':
    unittest.main()