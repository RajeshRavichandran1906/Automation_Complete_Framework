'''
Created on October 30, 2018

@author: Robert
Testcase Name : Edit portal with Three level navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779502
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage, designer_portal
from common.pages import portal_designer
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C6779502_TestClass(BaseTestCase):
    
    def test_C6779502(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portal_designer_obj=portal_designer.Portal_Designer(self.driver)
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
        main_page_obj.select_option_from_crumb_box("Domains")
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
        portal_designer_obj.verify_portal_dialog('Edit Portal','label_text', 'Edit Portal','Step 4: verify edit label')
        portal_designer_obj.verify_portal_dialog('Title', 'text_box', 'v5-navigation-test2', 'Step 4: verify title label')
        portal_designer_obj.verify_portal_dialog('Name', 'text_box', 'v5-navigation-test2', 'Step 4.1: verify Name label')
        portal_designer_obj.verify_portal_dialog('Banner', 'toggle_button', 'check', 'Step 4.3: verify Banner toggle button')
        portal_designer_obj.verify_portal_dialog('Alias', 'text_box', '', 'Step 4.2: verify Alias label')
        portal_designer_obj.verify_portal_dialog('Logo', 'text_box', '', 'Step 4.6: Logo Verification',placeholder='Not Selected')
        portal_designer_obj.verify_portal_dialog('Navigation', 'radio_button','check', 'Step 4.7: Navigation Verification', navigation_type='Three-level' )
        portal_designer_obj.verify_portal_dialog('Theme', 'drop_down', 'Default', 'Step 4.9: verify Theme drop_down')
        portal_designer_obj.verify_portal_dialog('URL','text_box','portal/P292_S19901/G520448/v5-navigation-test2','Step 4.10 verify url')
        portal_designer_obj.verify_portal_dialog_content_enable_disable('Save', 'button', 'disable', 'Step 4.11. Verify Save button disabled', navigation_type='Three-level')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button = True)
        
        """
        Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()    