'''
Created on October 31, 2018

@author: Vpriya
Testcase Name : Edit portal without my pages and alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779491
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C6779491_TestClass(BaseTestCase):
    
    def test_C6779491(self):
        
        """
        CLASS OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_path=folder_name+'->'+group_id
        portal_name='v5-alias-test1'
        
        """
        Step 1: Login WF new home page as domain developer
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
        Right click on 'v5-alias-test1' portal and select Edit
        Edit portal dialog appears;
        Verify below.
        Title and name appears as 'v5-alias-test1';
        Banner switch is on;
        Show portal title in banner box is checked;
        Logo stays Not selected;
        Two-level navigation is selected;
        Theme should be 'Midnight';
        URL: http:machine_name:port/alias/portal/P292_S19901/G520448/v5-alias-test1;
        Save button is highlighted and disabled by default;
        Cancel button is enabled.
        """
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Edit')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Save', Global_variables.mediumwait*7)
        
        designer_portal_obj.verify_caption_in_new_or_edit_portal_dialog('Edit Portal', step_number='Step 3.')
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name,  step_number='Step 3.')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number='Step 3.')
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', step_number='Step 3.')
        designer_portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', step_number='Step 3.')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', step_number='Step 3.')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable', step_number='Step 3.')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Midnight', current_mode='enable', step_number='Step 3.')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/{0}/{1}/{2}'.format(folder_name,group_id,portal_name), step_number='Step 3.')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', step_number='Step 3.')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 4. Click cancel
        Edit portal dialog closes.
        """
        
        designer_portal_obj.verify_portal_dialog_open_or_close("close","Step 4:Verify dialog node is close")
        
        """
        Step 5: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        