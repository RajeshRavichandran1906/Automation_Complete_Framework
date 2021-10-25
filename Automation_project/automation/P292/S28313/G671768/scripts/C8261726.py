'''
Created on October 30, 2018

@author: Robert
Testcase Name : Edit portal with Three level navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261726
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage, designer_portal
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C8261726_TestClass(BaseTestCase):
    
    def test_C8261726(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_obj=designer_portal.Portal(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
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
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-navigation-test2' portal and select Edit
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        
        """
        Step 4. Edit 'v5-navigation-test2' portal
        """
        main_page_obj.select_repository_folder_context_menu('v5-navigation-test2','Edit',verification_state='collapse')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Save', main_page_obj.home_page_short_timesleep)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='v5-navigation-test2', step_number='3.1')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='v5-navigation-test2', step_number='3.2')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='', step_number='3.3')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', step_number='3.4')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', step_number='3.5')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected', current_mode='disable', step_number='3.6')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='3.7')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='3.8')
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='3.9')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='enable', step_number='3.10')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='100%', label_text='Maximum width', step_number='3.11')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='3.12')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog('portal/P292_S19901/G520448/v5-navigation-test2', readonly_mode=True, step_number='3.13')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', color_name='curious_blue1', step_number='3.14')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable',step_number='3.15')
        
        """
        Step 5: click on (x)
        Edit portal dialog closes
        """
        portal_obj.close_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 6: Signout WF
        """
        
if __name__ == '__main__':
    unittest.main()    