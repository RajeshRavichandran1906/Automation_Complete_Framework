'''
Created on October 27, 2018

@author: Raghunath
Testcase Name : Test Edit menu
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261543
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility

class C8261543_TestClass(BaseTestCase):
    
    def test_C8261543(self):
        """
        Test_case variables
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        util_obj = utillity.UtillityMethods(self.driver) 
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        breadcrumb_path="Domains->{0}_{1}->{2}".format(project_id, suite_id, group_id)
    
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Workspaces')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        
        """
        Step 4: Right click on 'Portal for Context Menu for Testing' > Click Edit from the Resource tree
                Verify that 'Edit Portal' dialog opens with the following options:
                1.Title as 'Portal for Context Menu Testing'
                2.Name as 'Portal_for_Context_Menu_Testing
                3.Alias as empty
                4. Banner toggle button is on
                5.Show portal title in banner checkbox is checked
                6.Logo is disabled with the text Not Selected and Browse button is on the right of the logo
                7.First Navigation is selected and others are rest
                8.Show top navigation in banner with a checkbox is disabled
                9.Theme as Default with dropdown control
                10.URL as 'http://machinename:port/alias/P292_S19901/G513445/Po...' is disabled
                11. Save button is disabled and the Cancel button is enabled
        """
        main_page_obj.select_repository_folder_context_menu('Portal for Context Menu Testing','Edit')
        util_obj.synchronize_with_visble_text(".ibx-dialog-cancel-button", "Cancel", 30)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='Portal for Context Menu Testing', current_mode='enable', step_number='Step 4.1')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='Portal_for_Context_Menu_Testing', current_mode='enable', label_text='Name', step_number='Step 4.2')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', current_mode='enable', label_text='Alias',step_number='Step 4.3')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', label_text='Banner', step_number='4.4')
        portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', label_text='Show portal title in banner', step_number='4.5')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected',step_number='4.5')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse',button_location=True, step_number='4.6')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable',step_number='4.7')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='4.8')
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='4.9')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable', label_text='Show top navigation in banner',step_number='4.10')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='100%', label_text='Maximum width', step_number='4.11')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='4.12')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/{0}_{1}/{2}/Portal_for_Context_Menu_Testing'.format(project_id, suite_id, group_id),label_text='URL', step_number='4.13')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable',step_number='4.14')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel',current_mode='enable',step_number='4.15')   
        portal_obj.close_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()   