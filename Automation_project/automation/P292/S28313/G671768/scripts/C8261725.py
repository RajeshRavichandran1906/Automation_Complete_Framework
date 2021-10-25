'''
Created on November 2, 2018

@author: Vpriya
Testcase Name : Edit portal with Two-level side navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261725
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage, designer_portal
from common.pages import portal_designer
from common.lib import utillity, core_utility

class C8261725_TestClass(BaseTestCase):
    
    def test_C8261725(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portal_designer_obj=portal_designer.Portal_Designer(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        medium_wait=40
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"
        
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
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-navigation-test1' portal and select Edit
        Edit portal dialog appears;
        Verify below.
        Verify title and name appears as 'v5-navigation-test1';;
        Banner switch is on;
        Alias is empty
        Logo is Not Selected;
        Navigation is Two-level side;;
        Theme should be 'Light';
        URL field shows : https://machinename:port/alias/domain_name/v5-navigation-test1;
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        main_page_obj.right_click_folder_item_and_select_menu('v5-navigation-test1','Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1', medium_wait)
        portal_designer_obj.verify_portal_dialog('Edit Portal','label_text', 'Edit Portal','Step 3: verify edit label')
        portal_designer_obj.verify_portal_dialog('Title', 'text_box', 'v5-navigation-test1', 'Step 3.1: verify title label')
        portal_designer_obj.verify_portal_dialog('Name', 'text_box', 'v5-navigation-test1', 'Step 3.2: verify Name label')
        portal_designer_obj.verify_portal_dialog('Banner', 'toggle_button', 'check', 'Step 3.3: verify Banner toggle button')
        portal_designer_obj.verify_portal_dialog('Alias', 'text_box', '', 'Step 3.4: verify Alias is empty')
        portal_designer_obj.verify_portal_dialog('Logo', 'text_box', '', 'Step 3.5: Logo Verification',placeholder='Not Selected')
        portal_designer_obj.verify_portal_dialog('Navigation', 'radio_button','check', 'Step 3.6: Navigation Verification')
        portal_designer_obj.verify_portal_dialog('Theme', 'drop_down', 'Light','Step 3.7: verify Theme drop_down')
        portal_designer_obj.verify_portal_dialog('URL','text_box','portal/P292_S19901/G520448/v5-navigation-test1','Step 3.8 verify url')
        
        """
        Step 4. Click cancel
        Edit portal dialog closes.
        """
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button = True)
        designer_portal_obj.verify_portal_dialog_open_or_close("close","Step 4:Verify dialog node is close")
        
        """
        Step 5: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        