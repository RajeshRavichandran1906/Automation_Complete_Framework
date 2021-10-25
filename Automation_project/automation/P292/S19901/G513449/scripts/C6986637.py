'''
Created on November 1, 2018

@author: varun
Testcase Name : Test Edit menu
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986637
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity
from common.locators.portal_designer import Vfive_Designer
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6986637_TestClass(BaseTestCase):
    
    def test_C6986637(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        crumbbox_css = ".crumb-box .ibx-label-text"
        project_id = util_obj.parseinitfile('project_id')
        suite_id = util_obj.parseinitfile('suite_id')
        group_id = util_obj.parseinitfile('group_id')
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Portal View from the sidebar
        """
        main_page_obj.select_portals_from_sidebar()
        util_obj.synchronize_with_visble_text(crumbbox_css, 'Portals', 90)
        
        """
        Step 4: Right click on 'Portal for Context Menu T...' > Click Edit
                Verify that 'Edit Portal' dialog box opens with the following options:
                1.Title as 'Portal for Context Menu Testing'
                2.Name as 'Portal_for_Context_Menu_Testing
                3.Alias as empty
                4.Banner toggle button is on
                5.Show portal title in banner checkbox is checked
                6.Logo is disabled with the text Not Selected and Browse button is on the right of the logo
                7.First Navigation is selected and others are rest
                8.Show top navigation in banner with a checkbox is disabled
                9.Theme as Default with dropdown control
                10.URL as 'http://machinename:port/alias/P292_S19901/G513445/Po...' is read only
                11.Save button is disabled and Cancel button is enabled
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Edit')
        util_obj.synchronize_with_number_of_element(Vfive_Designer.title_textbox_input_css, 1, 45)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='Portal for Context Menu Testing', step_number='4.1')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='Portal_for_Context_Menu_Testing', step_number='4.2')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', step_number='4.3')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', step_number='4.4')
        portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', step_number='4.5')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected', current_mode='disable', step_number='4.6')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(button_location=True, step_number='4.7')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='4.8')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='4.9')
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='4.10')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable', step_number='4.11')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Default', step_number='4.12')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/{0}_{1}/{2}/Portal_for_Context_Menu_Testing'.format(project_id, suite_id, group_id), readonly_mode=True, step_number='4.13')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', color_name='curious_blue', step_number='4.14')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable', color_name='black', step_number='4.15')
        
        """
        Step 5: Click Cancel to close the 'Edit Portal' dialog box
        """
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        