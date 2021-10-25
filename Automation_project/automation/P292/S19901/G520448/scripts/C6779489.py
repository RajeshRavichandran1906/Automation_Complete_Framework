'''
Created on October 31, 2018

@author: varun
Testcase Name : Edit portal portal with my pages and alias
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6779489
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.wftools.designer_portal import Banner
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6779489_TestClass(BaseTestCase):
    
    def test_C6779489(self):
        
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        banner_obj=Banner(self.driver)
        
        """
        CSS
        """
        DESIGNER_CSS=".ibx-tab-button:nth-child(3) .ibx-label-text"
        PORTALS_CSS = "div[title='Portals'] .ibx-label-text"
        PORTAL_TITLE='v5-mypages-test2'
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_path=project_id+'_'+suite_id
        
        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-mypages-test2' portal and select Edit
        
        Edit portal dialog appears;
        Verify below.
        Title and name appears as 'v5-mypages-test2';
        Alias is not empty, retains '123'
        Banner switch is on;
        Show portal title in banner box is checked;
        Logo stays Not selected;
        Two-level navigation is selected;
        Theme should be 'Default';
        URL: http://machine_name:port/alias//portal/123;
        Save button is highlighted and disabled by default;
        Cancel button is enabled.
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.click_repository_folder(group_id)
        util_obj.synchronize_with_visble_text(DESIGNER_CSS, 'Designer', Global_variables.mediumwait)
        
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Edit")
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Save', Global_variables.mediumwait)
        alias_value='123'
        alias_path='portal/'+alias_value
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value=PORTAL_TITLE, step_number='3.1')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value=PORTAL_TITLE, step_number='3.2')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value=alias_value, step_number='4.3')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', step_number='3.4')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', step_number='3.5')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='', verify_placeholder_value='Not Selected', current_mode='disable', step_number='3.6')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(button_location=True, step_number='3.7')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='3.8')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='3.9')
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='uncheck', step_number='3.10')
        portal_obj.show_top_navigation_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='uncheck', current_mode='disable', step_number='3.11')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Default', step_number='3.12')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='{0}'.format(alias_path), readonly_mode=True, step_number='3.13')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', color_name='curious_blue', step_number='3.14')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', current_mode='enable', color_name='black', step_number='3.15')
        
        """
        Step 4: Click on Theme dropdown and select 'Light' theme.
        Verify Save button is highlighted and enabled.
        """
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Light')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='enable', color_name='curious_blue', step_number='4.1')
        
        """
        Step 5: Remove alias
        Verify URL is changed as :http://machine_name:port/alias/portal/P292_S19901/G520448/v5-mypages-test2
        """
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value='')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/{0}/{1}/{2}'.format(folder_path, group_id,PORTAL_TITLE), readonly_mode=True, step_number='5')
        
        """
        Step 6: Enter alias again as '123'
        """
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value='123')
        
        """
        Step 7: Click Save
        """
        portal_obj.close_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 8: Click on Portals node from side bar
        """
        util_obj.synchronize_with_visble_text(DESIGNER_CSS, 'Designer', Global_variables.mediumwait*5)
        main_page_obj.select_portals_from_sidebar()
        
        """
        Step 9: Right click on 'v5-mypages-test2' portal and select Run
        Verify portal run mode appears as below;
        Verify URL: http://machine_name:port/alias/portal/123
        """
        util_obj.synchronize_with_visble_text(PORTALS_CSS, 'Portals', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.verify_current_url(alias_path, 'Step 9.1: URL verification in new window')
        banner_obj.verify_portal_top_banner_title(PORTAL_TITLE, 'Step 9:2;Verify top banner title{0} shows in arun time'.format(PORTAL_TITLE))
        core_util_obj.switch_to_previous_window()
        
        """
        Step 10: Signout WF. 
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()     
        