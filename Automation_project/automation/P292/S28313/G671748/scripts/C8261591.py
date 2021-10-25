'''
Created on Dec 12, 2018

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261591
Testcase Name : Verify Admin User can Create new Domain
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.global_variables import Global_variables

class C8261591_TestClass(BaseTestCase):

    def test_C8261591(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        CSS
        """
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        pop_up_css = '.pop-top'
        
        """
        TESTCASE VARIABLE
        """
        Testcase_ID='C6667538'
        
        """
        Step 1:Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
 
        """
        Step 2:Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
 
        """
        Step 3:Click on Domain from the resource tree
        Verify 2 action bar (Domain, Folder) is displayed
        """
        domain_action_bar_options=['Workspace', 'Folder']
        main_page_obj.expand_repository_folder('Workspaces')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(domain_action_bar_options, 'Step 3: Verify domain from resource tree options{0}'.format(domain_action_bar_options))

        """
        Step 4:Click on 'Domain' action bar
        Verify New Domain prompt is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Workspace')
        util_obj.synchronize_with_visble_text(pop_up_css, 'New Workspace', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_popup_dialog_caption('New Workspace', "Step 4:1: Verify New Domain title is displayed")
        main_page_obj.verify_new_domain_type_selected_value('Enterprise workspace', "Step 4:2: Verify New Domain type dropdown value shown as Enterprise domain")
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 4:3: Verify popup dialog is displayed")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('OK', "Step 4.4 : Verify", enable=False)
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog("Cancel", "Step 4.5 : Verify", enable = True)
        
        """
        Step 5:Enter Title 'C6667538'
        Verify the Name will be inherited from the title
        Also verify that 'Create Reporting Server Application' is unchecked
        """
        main_page_obj.enter_new_domain_title_value(Testcase_ID)
        main_page_obj.verify_new_domain_name_value(Testcase_ID, "Step 5: Verify New domain name value is inherited from the title")
        main_page_obj.verify_new_domain_create_reporting_server_application_checkbox("Step 4:2: Verify New Domain Create Reporting Server Application check box is unchecked", check=False)
        
        """
        Step 6:Click on 'Ok' button in new domain prompt
        Verify that the 'C6667538' is displayed in the Resource tree
        """
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 6:Verify folder is displayed in the resource tree")
        
        """
        Step 7:Right Click on the 'C6667538' > Delete > yes in the 'Delete' dialog box
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Delete', folder_path='Workspaces')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')

        """
        Step 8:In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_long_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()