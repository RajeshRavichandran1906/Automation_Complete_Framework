'''
Created on January 31, 2019

@author: Varun
Testcase Name : Test Edit menu using Developers
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261548
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.core_utility import CoreUtillityMethods

class C8261548_TestClass(BaseTestCase):
    
    def test_C8261548(self):
        """
        Test case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        util_obj = UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        breadcrumb_path="Domains->{0}_{1}->{2}".format(project_id, suite_id, group_id)
        portal_name = 'Portal for Context Menu Testing'
        
        """
        Test case CSS
        """
        portal_dialog_css = ".ibx-dialog-title-box .ibx-title-bar-caption .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view([portal_name], 'asin', "Step 3: Verify user sees 'Portal for Context Menu Testing' folder.")
        
        """
        Step 4: Right click on 'Portal for Context Menu for Testing' > Click Edit from the Resource tree
                Verify that 'Edit Portal' dialog opens with the following options:
                Verify that 'Edit Portal' dialog box opens with the following options:
                1.Title as 'Portal for Context Menu Testing'
                2.Name as 'Portal_for_Context_Menu_Testing
                3.Alias as empty
                4.Banner toggle button is on
                5.Show portal title in banner checkbox is checked
                6.Logo is disabled with the text Not Selected and Browse button is on the right of the logo
                7.Two level side navigation is selected and others are rest
                8.Show top navigation in banner with a checkbox is disabled
                9. Maximum width text box is available and 100% is set by default
                10.Theme is Designer 2018
                11.URL as 'http://machinename:port/alias/P292_S19901/G513445/Po...' is disabled
                12.Save button is disabled and Cancel button is enabled
        """
        main_page_obj.select_repository_folder_context_menu(portal_name,'Edit')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Edit Portal', main_page_obj.home_page_medium_timesleep)
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, current_mode='enable', step_number='4.1')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='Portal_for_Context_Menu_Testing', current_mode='enable', label_text='Name', step_number='4.2')
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', current_mode='enable', label_text='Alias',step_number='4.3')
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', label_text='Banner', step_number='4.4')
        designer_portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', label_text='Show portal title in banner', step_number='4.5')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected',step_number='4.6')
        designer_portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse',button_location=True, step_number='4.7')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable',step_number='4.8')
        designer_portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='4.9')
        designer_portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='4.10')
        designer_portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable', label_text='Show top navigation in banner',step_number='4.11')
        designer_portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='100%', label_text='Maximum width', step_number='4.12')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='4.13')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/{0}_{1}/{2}/Portal_for_Context_Menu_Testing'.format(project_id, suite_id, group_id),label_text='URL', step_number='4.14')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable',step_number='4.15')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel',current_mode='enable',step_number='4.16')   
        
        """
        Step 5:Click X button to close the Edit Portal dialog.
        """
        designer_portal_obj.close_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 6:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()       
    