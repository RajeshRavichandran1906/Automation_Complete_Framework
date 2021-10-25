'''
Created on December 26, 2018

@author: KK14897
Testcase Name : Edit portal without my pages,with alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261717
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage, designer_portal
from common.lib import utillity,core_utility
from common.wftools.designer_portal import Banner

class C8261717_TestClass(BaseTestCase):
    
    def test_C8261717(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        banner_obj=Banner(self.driver)
        Crumb_css=".crumb-box"
        Long_wait=90
        medium_wait=40
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        portal_name='v5-alias-test2'
        workspaces = "Workspaces"
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(Crumb_css, '1', Long_wait)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-alias-test2' portal and select Edit
        Edit portal dialog appears;
        Verify below.
        Title and name appears as 'v5-alias-test2';
        Alias is not empty, shows 'abc123ABC+_)*&^%$#@!'
        Banner switch is on;
        Show portal title in banner box is checked;
        Logo stays Not selected;
        Two-level navigation is selected;
        Theme should be 'Midnight';
        URL: http://machinename:port/alias/portal/abc123ABC_@!
        Save button is highlighted and disabled by default;
        Cancel button is enabled.
        """
        main_page_obj.expand_repository_folder(workspaces+'->{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1', medium_wait)
        designer_portal_obj.verify_caption_in_new_or_edit_portal_dialog("Edit Portal", '4')
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number='4.1')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value=portal_name, step_number='4.2')
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(verify_value="abc123ABC_@!",step_number="4.3")
        designer_portal_obj.banner_toggle_button_in_new_or_edit_portal_dialog(verify_toggle='check', current_mode='enable', step_number='4.4')
        designer_portal_obj.show_portal_title_in_banner_checkbox_inside_new_or_edit_portal_dialog(verify_checkbox='check', current_mode='enable', step_number='4.5')
        designer_portal_obj.logo_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='Not Selected', step_number='4.6')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', current_mode='enable', step_number='4.7')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Midnight', current_mode='enable', step_number='4.8')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/abc123ABC_@!', step_number='4.9')
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(verify_button='Save', current_mode='disable', step_number='4.10')
        designer_portal_obj.cancel_button_inside_new_or_edit_portal_dialog(verify_button='Cancel', step_number='4.11')
        
        """
        Step 4.Remove Alias
        Verify URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias-test2
        """
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value="", step_number="4.1")
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/v5-alias-test2', step_number='4.2')
        
        """
        Step 5. Click on Save.
        Edit portal dialog closes.
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True, step_number="5.1")
        designer_portal_obj.verify_portal_dialog_open_or_close("close","Step 4:Verify dialog node is close")
        
        """
        Step 6:Right click on 'v5-alias-test2' portal from content tree and select Run.
        Verify URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias-test2
        Verify portal run mode appears as below
        """
    
        main_page_obj.right_click_folder_item_and_select_menu('v5-alias-test2', 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.verify_current_url('portal/P292_S19901/G520448/v5-alias-test2', 'Step 9.1: URL verification in new window')
        banner_obj.verify_portal_top_banner_title(portal_name, 'Step 9:2;Verify top banner title{0} shows in arun time'.format(portal_name))
        util_obj.verify_picture_using_sikuli("info_build_logo.png","Step 9.5: Verify the Infobuilders icon logo")
        
        """
        Step 7: Close portal.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 8: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()