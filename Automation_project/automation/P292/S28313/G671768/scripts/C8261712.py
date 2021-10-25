'''
Created on October 31, 2018

@author: varun
Testcase Name : Create portal with my pages and alias
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261712
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261712_TestClass(BaseTestCase):
    
    def test_C8261712(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
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
        Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', 15)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'v5-mypages-test2' in create portal dialog.
        Name text box is filled automatically as 'v5-mypages-test2';
        Verify URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-mypages-test2
        """
        PORTAL_TITLE='v5-mypages-test2'
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.longwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=PORTAL_TITLE, verify_value=PORTAL_TITLE, step_number='4.1')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/'+PORTAL_TITLE, readonly_mode=True, label_text='URL', step_number='4.2')
        
        """
        Step 5: Enter alias as '123'
        Verify URL: http://machine_name:port/alias/portal/123
        """
        ALIAS_VALUE='1234'
        URL_VALUE='portal/1234'
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value=ALIAS_VALUE, verify_value=ALIAS_VALUE, current_mode='enable', label_text='Alias', focused=True, step_number='5')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value=URL_VALUE, readonly_mode=True, label_text='URL', step_number='5.1')
        
        """
        Step 6: Click on 'Create My Pages menu' check box
        """
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox="check")
        
        """
        Step 7: Click Create
        Verify 'Create Portal' dialog is closed;
        'v5-mypages-test2' portal folder is created under P292_S19901 domain > G520448 folder in content tree;
        Portal is unpublished, title appears in Italic in content tree;
        verify portal icon in content area.
        """
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        portal_obj.verify_portal_dialog_open_or_close("close", "Step 7. Verify dialog closed")
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.wait_for_page_loads(20, pause_time=10)
        folder_name_list=['v5-mypages-test2']
        main_page_obj.expand_repository_folders_and_verify(folder_name_path, folder_name_list, 'Step 7.1: Verify repository folders')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(PORTAL_TITLE, 'unpublish', 'Step 7.2: Verify folder published')
        main_page_obj.verify_folder_icon_in_content_area(PORTAL_TITLE, 'portal', '7.3')
        
        """
        Step 8: Double click on 'v5-mypages-test2' portal from content area. 
        Verify 'My Pages' folder appears.
        """
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, click_option='double_click')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.folders_css, 'Folders', Global_variables.mediumwait)
        
        folder_name_list=['My Pages']
        main_page_obj.verify_folders_in_grid_view(folder_name_list, 'asin', 'Step 8.1: Verify content folders')
        
        """
        Step 9: Right click on 'v5-mypages-test2' portal from content tree and click on Run.
        Verify portal run mode appears as below;
        Verify URL : http://machine_name:port/alias/portal/123
        """
        main_page_obj.select_repository_folder_context_menu(PORTAL_TITLE, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.verify_current_url('portal/1234', 'Step 9: Verify URL in the new page')
        
        """
        Step 10: Close portal
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 11: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()