'''
Created on October 31, 2018

@author: varun
Testcase Name : Create portal without my pages and alias
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261714
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261714_TestClass(BaseTestCase):
    
    def test_C8261714(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        PORTAL_TITLE='v5-alias-test1'
        
        """
        CSS
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', 15)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'v5-alias-test1' in create portal dialog.
        Name text box is filled automatically as 'v5-alias-test1';
        Verify URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias-test1
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.mediumwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=PORTAL_TITLE, verify_value=PORTAL_TITLE, step_number='4')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/{0}/{1}/{2}'.format(folder_name, group_id,PORTAL_TITLE), readonly_mode=True, step_number='4.1')
        
        """
        Step 5: Click on Theme dropdown;
        Select 'Midnight' theme
        """
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Midnight')
        
        """
        Step 6: Click Create
        Verify 'Create Portal' dialog is closed;
        'v5-alias-test1' portal folder is created under P292_S19901 domain > G520448 folder in content tree;
        Portal is unpublished, title appears in Italic in content tree;
        verify portal icon in content area.
        """
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        portal_obj.verify_portal_dialog_open_or_close("close", "Step 6.1: Verify dialog closed")
        
        folder_name_list=['v5-alias-test1']
        main_page_obj.expand_repository_folders_and_verify(folder_name_path, folder_name_list, 'Step 6.1: Verify repository folders',comparion_type='asin')
        
        main_page_obj.click_repository_folder(group_id)
        main_page_obj.verify_repository_folder_publish_or_unpublish(PORTAL_TITLE, 'unpublish', 'Step 6.2: Verify unpublished')
        main_page_obj.verify_folder_icon_in_content_area(PORTAL_TITLE, 'portal', '6.4')
        
        """
        Step 7: Double click on 'v5-alias-test1' portal from content area.
        Verify 'My Content' folder does not appear.
        """
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, click_option="double_click")
        main_page_obj.verify_folders_in_grid_view(['My Content'],'asnotin', 'Step 7: Verify My Content doesnt appear')
        
        """
        Step 8: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()