'''
Created on October 30, 2018

@author: Robert
Testcase Name : Edit portal with Two-level top navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261727
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import utillity,core_utility

class C8261727_TestClass(BaseTestCase):
    
    def test_C8261727(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"
        
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-navigation-test3' portal and select Edit
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        main_page_obj.select_repository_folder_context_menu('v5-navigation-test3','Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1',main_page_obj.home_page_short_timesleep)
        
        
        """
        Verify dialog title appears as 'Edit Portal';
        Verify title and name appears as 'v5-navigation-test3';
        Banner switch is on;
        Alias is empty;
        Logo is Not Selected;
        Navigation is Two-level top;
        Maximum width is not set, left default (100%);
        Theme should be 'Designer 2018';
        'Show top navigation in banner' box is checked;
        URL field shows : https://machinename:port/alias/domain_name/v5-navigation-test3
        Save button is disabled
        """
        designer_portal_obj.verify_caption_in_new_or_edit_portal_dialog('Edit Portal','3')
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='v5-navigation-test3', current_mode='enable',label_text='Title',step_number='3.1')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='v5-navigation-test3',current_mode='enable',label_text='Name',step_number='3.2')
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle="check", current_mode='enable',label_text='Banner',step_number='3.3')
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', current_mode='enable', label_text='Alias',step_number='3.4')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected', current_mode='disable', label_text='Logo',step_number='3.5')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck',step_number='3.6')
        designer_portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='3.7')
        designer_portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable', step_number='3.8')
        designer_portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='',verify_placeholder_value="100%", current_mode='enable', label_text='Maximum width',step_number='3.9')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', current_mode='enable', label_text='Theme',step_number='3.10')
        designer_portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check',current_mode='enable',label_text='Show top navigation in banner', step_number='3.11')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/v5-navigation-test3',label_text='URL',step_number='3.12')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(current_mode='disable', step_number='3.13')
        
        """
        Step 4. Select Two-level side navigation
        """
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        
        """
        Step 5. Click on save button
        Step 5.1. Edit portal dialog closes.
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button = True)
        util_obj.synchronize_until_element_disappear(".pop-top", main_page_obj.home_page_short_timesleep)
        designer_portal_obj.verify_portal_dialog_open_or_close("close", "Step 5.1. Edit portal dialog closes.")
        
        """
        Step 6. Right click on 'v5-navigation-test3' portal and select Edit
        Verify Navigation is 'Two-level side'
        """
        main_page_obj.select_repository_folder_context_menu('v5-navigation-test3','Edit')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='6')
        
        """
        Step 7. Click on Cancel button.
        """
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button = True)
        
        """
        Step 8: Signout WF.
        """
if __name__ == '__main__':
    unittest.main()