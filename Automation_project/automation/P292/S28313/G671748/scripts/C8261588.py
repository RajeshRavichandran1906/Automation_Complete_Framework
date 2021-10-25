'''
Created on December 12, 2018

@author: varun
Testcase Name : Verify Home page is the default when first launch WebFocus
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261588
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261588_TestClass(BaseTestCase):
    
    def test_C8261588(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """
        Test case CSS
        """
        properties_tab_css = ".properties-general-pane-tab" 
        property_title_css = ".properties-page-label .ibx-label-text"
        properties_close_button_css = ".properties-page-close-button"
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        
        """
        Test case variables
        """
        property_tab_list = ['General','Advanced','Server']
        property_title = 'Retail Samples'
        action_bar_text = 'Action Bar'
        domains_repository = 'Domains'
        domains_actionbar_list = ['Workspace','Folder']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(domains_repository)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Right click on 'Retail Samples' domain from repository tree > Click on 'Properties'
        Verify that Properties dialog box opens with the following options:
        1.Title as 'Retail Samples' at the top of the dialog with the X button at the right corner of the dialog box.
        2.Three tabs are available (General, Advanced and Server tabs).
        3.By default 'General' tab is selected.
        4.By default Save button is disabled and Cancel button is enabled.
        """
        main_page_obj.select_repository_folder_context_menu('Retail Samples', 'Properties')
        util_obj.synchronize_with_number_of_element(properties_tab_css, 1, base_obj.home_page_medium_timesleep)
        util_obj.synchronize_with_visble_text(property_title_css, property_title, base_obj.chart_medium_timesleep)
        property_title_element = util_obj.validate_and_get_webdriver_object(property_title_css, "property-title").text.strip()
        util_obj.asequal(property_title,property_title_element,'Step 03.01: Verify the Title is Retail Samples')
        util_obj.verify_object_visible(properties_close_button_css, True, "Step 03.02: Verify Close button is visible")
        main_page_obj.verify_property_dialog_tab_list(property_tab_list, "Step 03.03: Verify 3 tabs are available")
        main_page_obj.verify_selected_tab_in_property_dialog('General', 'Step 03.04: Verify General tab is selected')
        main_page_obj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable' , 'Step 03.05: Verify Save button is disabled')
        
        """
        Step 4: Click on "Domain" node from the repository tree
        Verify that Properties dialog box gets closed and Domain and Folder only appear in the action bar.
        """
        main_page_obj.expand_repository_folder(domains_repository)
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_medium_timesleep)
        util_obj.verify_object_visible(properties_tab_css, False, "Step 04.01: Verify Property Dialog tab is closed")
        main_page_obj.verify_action_bar_tab_all_options(domains_actionbar_list, "Step 04.02: Verify Domain and Folder are Present")
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()