'''
Created on October 27, 2018

@author: Raghunath
Testcase Name : Test Edit menu
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6670294
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity
from common.lib.global_variables import Global_variables
import time


class C6670294_TestClass(BaseTestCase):
    
    def test_C6670294(self):
        """
        Test_case variables
        """
        
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver) 
        breadcrumb_path="Domains->P292_S19901->G513445"
        Crumb_css=".crumb-box"
        
    
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(Crumb_css, 1, Global_variables.mediumwait * 10)
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        time.sleep(10)
#         util_obj.synchronize_with_visble_text(files_box_css, "Default sort", Global_variables.mediumwait * 10)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        
        """
        Step 4: Right click on 'Portal for Context Menu ...' > Click Properties from the Resource Tree
        Verify that Properties dialog opens with the three tabs are 'General' (Selected by default), 'Advanced' and 'Server.
        Verify all the options under 'General' tab as per in the screenshot
        """
        main_page_obj.select_repository_folder_context_menu('Portal for Context Menu Testing','Edit')

        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='Portal for Context Menu Testing', current_mode='enable', step_number='Step 4.1')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='Portal_for_Context_Menu_Testing', current_mode='enable', label_text='Name', step_number='Step 4.2')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', current_mode='enable', label_text='Alias',step_number='Step 4.3')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', label_text='Banner', step_number='4.4')
        portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', label_text='Show portal title in banner', step_number='4.5')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected',step_number='4.5')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse',button_location=True, step_number='4.6')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable',step_number='4.7')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable', label_text='Show top navigation in banner',step_number='4.8')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Default', label_text='Theme', step_number='4.9')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing',label_text='URL', step_number='4.10')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable',step_number='4.11')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel',current_mode='enable',step_number='4.12')   
        """
        Step 5: Click Cancel to close the 'Edit Portal' dialog box
        """
        portal_obj.close_button_inside_new_or_edit_portal_dialog(select_button=True)
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()   