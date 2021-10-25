'''
Created on April 1, 2019

@author: varun
Testcase Name : Check property default
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261735
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import designer_portal
from common.lib.global_variables import Global_variables

class C8261735_TestClass(BaseTestCase):
    
    def test_C8261735(self):
        """
        Test case objects
        """
        global_obj = Global_variables()
        portal_obj = designer_portal.Portal(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
        """
        Test case CSS
        """
        domains_css = ".toolbar"
        portal_dialog_css = ".create-pvd-dialog .ibx-title-bar-caption .ibx-label-text"
        workspace = "Workspaces"
        
        """
        Step 1: Login WF as domain advanced user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G671769' folder;
        Select Designer tag and click on Portal tile in action bar.
        Verify the create portal dialog appears with maximum width set to 100% by default and is active as below
        """
        util_obj.synchronize_with_visble_text(domains_css, workspace, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='100%',step_number='3.1')
        
        """
        Step 4: Click inside 'Maximum width' text box
        Verify that in CR it is editable
        Verify that in IE11 the 100% is cleared out
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='')
        if (global_obj.browser_name != 'ie'):
            portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(current_mode='enable',step_number='4.1')
        else:
            portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='', step_number='4.1')
            
        """
        Step 5: Click anywhere outside of the text box
        Verify that it reverts back to 100% and nothing has changed in appearance
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(click_on_label=True)
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='100%',step_number='5.1')
        
        """
        Step 6: Choose 'Three level' navigation
        Verify the Maximum width is still 100%
        """
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='100%',step_number='6.1')
        
        """
        Step 7: Click inside 'Maximum width' text box
        Verify that in CR it is editable
        Verify that in IE11 the 100% is cleared out
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='')
        if (global_obj.browser_name != 'ie'):
            portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(current_mode='enable',step_number='7.1')
        else:
            portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='', step_number='7.1')
            
        """
        Step 8: Click anywhere outside of the text box
        Verify that it reverts back to 100% and nothing has changed in appearance
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(click_on_label=True)
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='100%',step_number='8.1')
        
        """
        Step 9: Choose 'Two level Top 'navigation
        Verify the Maximum width is still 100%
        """
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='100%',step_number='9.1')
        
        """
        Step 10: Click inside 'Maximum width' text box
        Verify that in CR it is editable
        Verify that in IE11 the 100% is cleared out
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='')
        if (global_obj.browser_name != 'ie'):
            portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(current_mode='enable',step_number='10.1')
        else:
            portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='', step_number='10.1')
        
        """
        Step 11: Click anywhere outside of the box
        Verify that it reverts back to 100% and nothing has changed in appearance
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(click_on_label=True)
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_placeholder_value='100%',step_number='11.1')
        
        """
        Step 12: Click inside 'Maximum width' text box
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='')
        
        """
        Step 13: Enter 75 then click anywhere outside the box
        Verify the maximum width value automatically picks up px (75px) and the % disappeared.
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(click_on_label=True)
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='75px', step_number='13.1')
        
        """
        Step 14: Click Cancel
        """
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 15: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
            
        