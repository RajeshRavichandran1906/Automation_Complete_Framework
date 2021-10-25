'''
Created on October 26, 2018

@author: varun
Testcase Name : Test Properties menu
Testcase ID : lnxtestrail.ibi.com/testrail/index.php?/cases/view/6670301
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators import wf_mainpage_locators
from common.lib import base

class C6670301_TestClass(BaseTestCase):
    
    def test_C6670301(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        domain_css = "div[data-ibx-type=\"breadCrumbTrail\"] div[data-ibx-type=\"ibxButtonSimple\"] .ibx-label-text"
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Favorites View from the sidebar
        """
        util_obj.synchronize_with_visble_text(domain_css, 'Domains', Global_variables.mediumwait)
        main_page_obj.select_favorites_from_sidebar()
        
        """
        Step 4: Right click on 'Portal for Context Menu T...' > Click Properties
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Properties')
        main_page_obj.verify_property_dialog_value('Title', 'text_value', 'Portal for Context Menu Testing','Step 4.1: Title verification')
        main_page_obj.verify_property_dialog_value('Name', 'text_value', '2680958774','Step 4.2: Name verification')
        main_page_obj.verify_property_dialog_value('Summary', 'text_area', '','Step 4.3: Summary verification')
        main_page_obj.verify_property_dialog_value('Path', 'text_value', 'IBFS:/WFC/UserInfo/autoadmuser18/Favorites/2680958774','Step 4.4: Path verification')
        main_page_obj.verify_property_dialog_value('Target Path', 'text_value', 'IBFS:/WFC/Repository/P292_S19901/G513445/Portal_for_Context_Menu_Testing','Step 4.5: Target Path verification')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Created', 'admin', 'Step 4.6: Verify Created')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Modified', 'admin', 'Step 4.7: Verify Modified')
        main_page_obj.verify_created_modified_accessed_time_stamp_format('Accessed', 'admin', 'Step 4.8: Verify Accessed')
        main_page_obj.verify_property_dialog_value('Tool', 'text', '','Step 4.9: Tool verification')
        main_page_obj.verify_property_dialog_value('Owner', 'text', 'autoadmuser18','Step 4.10: Owner verification')
        main_page_obj.verify_property_dialog_value('Size', 'text', '-','Step 4.11: Size verification')
        
        """
        Step 5: Click the advanced tab 
        Verify that all the options appear under Advanced tab as same in the below screenshot
        """
        util_obj.synchronize_with_number_of_element(tab_css, 2, Global_variables.mediumwait)
        main_page_obj.select_property_tab_value("Advanced")
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