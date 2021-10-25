'''
Created on October 30, 2018

@author: Robert
Testcase Name : Edit portal with Two-level top navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779503
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.pages import portal_designer
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C6779503_TestClass(BaseTestCase):
    
    def test_C6779503(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portal_designer_obj=portal_designer.Portal_Designer(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-navigation-test3' portal and select Edit
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        main_page_obj.select_repository_folder_context_menu('v5-navigation-test3','Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1',60)
        
        
        """
        Verify dialog title appears as 'Edit Portal';
        Verify title and name appears as 'v5-navigation-test3';
        Banner switch is on;
        Alias is empty;
        Logo is Not Selected;
        Navigation is Two-level top;
        Theme should be 'Default';
        'Show top navigation in banner' box is checked;
        URL field shows : https://machinename:port/alias/domain_name/v5-navigation-test3
        Save button is disabled
        """
        portal_designer_obj.verify_portal_dialog('Edit Portal','label_text', 'Edit Portal','Step 3: verify edit label')
        portal_designer_obj.verify_portal_dialog('Title', 'text_box', 'v5-navigation-test3', 'Step 3: verify title label')
        portal_designer_obj.verify_portal_dialog('Name', 'text_box', 'v5-navigation-test3', 'Step 3.1: verify Name label')
        portal_designer_obj.verify_portal_dialog('Banner', 'toggle_button', 'check', 'Step 3.3: verify Banner toggle button')
        portal_designer_obj.verify_portal_dialog('Alias', 'text_box', '', 'Step 3.2: verify Alias label')
        portal_designer_obj.verify_portal_dialog('Logo', 'text_box', '', 'Step 3.6: Logo Verification',placeholder='Not Selected')
        portal_designer_obj.verify_portal_dialog('Navigation', 'radio_button','check', 'Step 3.7: Navigation Verification', navigation_type='Two-level-top')
        portal_designer_obj.verify_portal_dialog('Theme', 'drop_down', 'Default', 'Step 3.9: verify Theme drop_down')
        portal_designer_obj.verify_portal_dialog('Show top navigation in banner', 'checkbox', 'check', 'Step 3.10. Verify Show top navigation in banner is enabled')
        portal_designer_obj.verify_portal_dialog('URL','text_box','portal/P292_S19901/G520448/v5-navigation-test3','Step 3.11 verify url')
        portal_designer_obj.verify_portal_dialog_content_enable_disable('Save', 'button', 'disable', 'Step 3.12. Verify Save button disabled', navigation_type='Three-level')
        
        """
        Step 4. Select Two-level side navigation
        """
        '''awaiting code from aftab'''
        portal_designer_obj.create_or_edit_portal('Navigation', 'radio_button', 'check', navigation_type='Two-level-side')
        
        """
        Step 5. Click on save button
        Step 5.1. Edit portal dialog closes.
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button = True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        designer_portal_obj.verify_portal_dialog_open_or_close("close", "Step 5.1. Edit portal dialog closes.")
        
        """
        Step 6. Right click on 'v5-navigation-test3' portal and select Edit
        """
        main_page_obj.select_repository_folder_context_menu('v5-navigation-test3','Edit')
        
        """
        Step 6.1.. Verify Navigation is 'Two-level side'
        """
        portal_designer_obj.verify_portal_dialog('Navigation', 'radio_button','check', 'Step 6.1: Navigation Verification', navigation_type='Two-level-side')
        
        """
        Step 7. Click on Cancel button.
        """
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button = True)
        
        """
        Step 8: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()