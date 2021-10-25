'''
Created on October 26, 2018

@author: varun
Testcase Name : Test Properties menu
Testcase ID : lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261563
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators

class C8261563_TestClass(BaseTestCase):
    
    def test_C8261563(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        admin_user_name = core_util_obj.parseinitfile('mrid')
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        portal_name = '2680958774'
        portal_title = 'Portal for Context Menu Testing'
        path = 'IBFS:/WFC/UserInfo/{0}/Favorites/{1}'.format(admin_user_name, portal_name)
        target_path = 'IBFS:/WFC/Repository/{0}_{1}/{2}/Portal_for_Context_Menu_Testing'.format(project_id, suite_id, group_id)
        attribute_type_text_value = 'text_value'
        
        '''
        Variable css
        '''
        properties_title_css = ".properties-page-label .ibx-label-text"
        
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Favorites View from the sidebar
        """
        main_page_obj.select_favorites_from_sidebar()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_title, 190)
        
        """
        Step 4: Right click on 'Portal for Context Menu T...' > Click Properties
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, 'Properties')
        util_obj.synchronize_with_visble_text(properties_title_css, portal_title, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_property_dialog_value('Title', attribute_type_text_value, 'Portal for Context Menu Testing','Step 4.1: Title verification')
        main_page_obj.verify_property_dialog_value('Name', attribute_type_text_value, portal_name,'Step 4.2: Name verification')
        main_page_obj.verify_property_dialog_value('Summary', 'text_area', '','Step 4.3: Summary verification')
        main_page_obj.verify_property_dialog_value('Path', attribute_type_text_value, path,'Step 4.4: Path verification')
        main_page_obj.verify_property_dialog_value('Target Path', attribute_type_text_value, target_path,'Step 4.5: Target Path verification')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Created', admin_user_name, 'Step 4.6: Verify Created')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Modified', admin_user_name, 'Step 4.7: Verify Modified')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Accessed', admin_user_name, 'Step 4.8: Verify Accessed')
        main_page_obj.verify_property_dialog_value('Tool', 'text', '','Step 4.9: Tool verification')
        main_page_obj.verify_property_dialog_value('Owner', 'text', admin_user_name,'Step 4.10: Owner verification')
        main_page_obj.verify_property_dialog_value('Size', 'text', '-','Step 4.11: Size verification')
        
        """
        Step 5: Click the advanced tab 
        Verify that all the options appear under Advanced tab as same in the below screenshot
        """
        main_page_obj.select_property_tab_value("Advanced")
        time.sleep(3)
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Explorer/Portal Properties', '5.1: Explorer label verification')
        main_page_obj.verify_property_dialog_value('Sort order', attribute_type_text_value, '','Step 5.2: Sort Order verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 5.3: Verify View All - is enabled.",tab_name='Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Search Properties', '5.4: Explorer label verification')
        main_page_obj.verify_property_dialog_value('Tags', attribute_type_text_value, '','Step 5.5: Tags verification',tab_name='Advanced')
        main_page_obj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', 'Step 5.6: verify Save button disable.')
        
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