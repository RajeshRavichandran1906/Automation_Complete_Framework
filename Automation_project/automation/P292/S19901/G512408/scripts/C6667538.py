'''
Created on Dec 12, 2018

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667538&group_by=cases:section_id&group_id=512408&group_order=asc
Testcase Name : Verify Admin User can Create new Domain
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.global_variables import Global_variables

class C6667538_TestClass(BaseTestCase):

    def test_C6667538(self):
        
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
        content_files_css=".content-box.ibx-widget .files-box"
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        
        """
        TESTCASE VARIABLE
        """
        Testcase_ID='C6667538'
        
        """
        Step 1:Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_ICON_CSS, 1, 190)
 
        """
        Step 2:Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
 
        """
        Step 3:Click on Domain from the resource tree
        Verify 2 action bar (Domain, Folder) is displayed
        """
        domain_action_bar_options=['Domain', 'Folder']
        main_page_obj.select_option_from_crumb_box('Domains')
        main_page_obj.verify_action_bar_tab_all_options(domain_action_bar_options, 'Step 3: Verify domain from resource tree options{0}'.format(domain_action_bar_options))

        """
        Step 4:Click on 'Domain' action bar
        Verify New Domain prompt is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Domain')
        main_page_obj.verify_popup_dialog_caption('New Domain', "Step 4:1: Verify New Domain title is displayed")
        main_page_obj.verify_new_domain_type_selected_value('Enterprise domain', "Step 4:2: Verify New Domain type dropdown value shown as Enterprise domain")
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 4:3: Verify popup dialog is displayed")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('OK', "Step 1: Verify", enable=False)
        main_page_obj.verify_button_color_on_popup_dialog('OK', 'curious_blue', "Step 2: Verify color")
        
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
        util_obj.synchronize_with_visble_text(content_files_css, Testcase_ID, 15)
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 6:Verify folder is displayed in the resource tree")
        
        """
        Step 7:Right Click on the 'C6667538' > Delete > yes in the 'Delete' dialog box
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Delete', folder_path='Domains')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', 15)
        main_page_obj.click_button_on_popup_dialog('OK')

        """
        Step 8:In the banner link, click on the top right username > Click Sign Out
        """
        
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()