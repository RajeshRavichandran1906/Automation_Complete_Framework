'''
Created on November 7, 2018

@author: varun
Testcase Name : Edit portal with logo
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261719
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C8261719_TestClass(BaseTestCase):
    
    def test_C8261719(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        edit_portal_text = "Edit Portal"
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        domains_css = ".toolbar"
        dialog_box_css=".pop-modal .ibx-dialog-main-box"
        workspace = "Workspaces"
        
        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.click_repository_folder(workspace)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-logo-test' portal and select Edit
        Verify dialog title appears as 'Edit Portal';
        Verify title and name appears as 'v5-logo-test';
        Banner switch is on;
        Alias is empty;
        Logo text box shows IBFS:/WFC/Repository/domain_name/Cat.jpg;
        Navigation stays with initial selection;
        Theme should be 'Midnight';
        URL field shows : https://machine_name:port/alias/domain_name/v5-logo-test
        """
        util_obj.synchronize_with_visble_text(domains_css, workspace, Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('P292_S19901')
        main_page_obj.click_repository_folder('G520448')
        time.sleep(30)
        main_page_obj.right_click_folder_item_and_select_menu('v5-logo-test', 'Edit')
        util_obj.synchronize_with_visble_text(edit_portal_css, edit_portal_text, Global_variables.mediumwait)
        observed_edit_portal_title=util_obj.validate_and_get_webdriver_object(edit_portal_css, "Edit-portal-title").text.strip()
        util_obj.asequal(observed_edit_portal_title,edit_portal_text,'Step 3.1" Verify dialog box title')
        portal_obj.title_textbox_in_new_or_edit_portal_dialog( verify_value='v5-logo-test', step_number='3.2')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='v5-logo-test', step_number='3.3')
        portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog( verify_toggle='check', step_number='3.4')
        portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value='',  step_number='3.5')
        portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_value='IBFS:/WFC/Repository/P292_S19901/G520448/Cat.jpg', step_number='3.6')
        portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='3.7')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog( verify_theme='Midnight', step_number='3.8')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/v5-logo-test', step_number='3.9')
        
        """
        Step 4: Change title as 'v5_logo!test*'
        Verify title is changed and name shows 'v5_logo!test_'.
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value='v5_logo!test*')
        portal_obj.name_textbox_in_new_or_edit_portal_dialog( verify_value='v5_logo!test_', step_number='4.1')
        
        """
        Step 5: Click on browse button next to Logo and select babydeer.jpg 
        Verify user can modify logos and Save button is enabled when new logo is selected.
        """
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog( current_mode='enable',  step_number='5.1')
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse', current_mode='enable',select_logo_name='babydeer', step_number='5')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='enable', step_number='5.2')
        
        """
        Step 6: Click on Save button
        Edit portal dialog closes.
        """
        portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(dialog_box_css, Global_variables.shortwait)
        portal_obj.verify_portal_dialog_open_or_close('close', 'Step 6.1: Verify Portal dialog box close')
        
        """
        Step 7: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()