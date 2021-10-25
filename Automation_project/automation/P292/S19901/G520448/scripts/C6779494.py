'''
Created on November 7, 2018

@author: varun
Testcase Name : Create portal with logo
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6779494
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C6779494_TestClass(BaseTestCase):
    
    def test_C6779494(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        domains_css = "div[title=\"Domains\"] .ibx-label-text"
        dialog_box_css=".pop-modal .ibx-dialog-main-box"
        logo_css = ".pvd-banner-logo"
        
        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        util_obj.synchronize_with_visble_text(domains_css, 'Domains', Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('P292_S19901')
        main_page_obj.click_repository_folder('G520448')
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', Global_variables.mediumwait)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'v5-logo-test' in create portal dialog.
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', Global_variables.mediumwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value='v5-logo-test',verify_value=None)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(verify_value='v5-logo-test', step_number='4.1')
        portal_obj.url_textbox_in_new_or_edit_portal_dialog(verify_value='portal/P292_S19901/G520448/v5-logo-test',  step_number='4.2')
        
        """
        Step 5: Click on Browse button
        Step 6: Choose 'cat.jpg' and click on select button.
        """
        portal_obj.logo_browse_button_in_new_or_edit_portal_dialog(verify_value='Browse', current_mode='enable', select_logo_name='Cat', step_number='5')
        
        """
        Step 7: Click on Theme dropdown;
        Select 'midnight' theme
        """
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Midnight', step_number='7')
        
        """
        Step 8: Click Create
        Verify 'New Portal' dialog is closed;
        Portal title appears in Italic;
        Portal is unpublished.
        """
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True, step_number='8')
        util_obj.synchronize_until_element_disappear(dialog_box_css, Global_variables.shortwait)
        portal_obj.verify_portal_dialog_open_or_close('close', 'Step 8.1: verify dialog box closed')
        main_page_obj.verify_repository_folder_font_style('v5-logo-test', 'italic', 'Step 8.2: Verify italics in folder')
        main_page_obj.verify_repository_folder_publish_or_unpublish('v5-logo-test', 'unpublish', 'Step 8.3: verify folder is unpublished')
        
        """
        Step 9: Right click on 'v5-logo-test' and select Run
        Verify cat image appears as logo as shown below.
        """
        main_page_obj.right_click_folder_item_and_select_menu('v5-logo-test', 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.verify_picture_using_sikuli('cat_logo.png', 'Step 9.1: Verify cat logo')
        current_windows = len(self.driver.window_handles)
        
        """
        Step 10: Click on logo
        Verify it doesn't bring up information builders website
        """
        logo_element = util_obj.validate_and_get_webdriver_object(logo_css, 'logo-element')
        core_util_obj.left_click(logo_element)
        new_windows = len(self.driver.window_handles)
        util_obj.asequal(current_windows,new_windows,'Step 10.1: Verify new windows doesnt open')
        
        """
        Step 11: Close portal run mode
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 12: Signout WF.
        """
        util_obj.synchronize_with_visble_text(domains_css, 'Domains',Global_variables.mediumwait)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()