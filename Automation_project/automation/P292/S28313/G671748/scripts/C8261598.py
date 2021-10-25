'''
Created on December 12, 2018

@author: Vpriya
Testcase Name : Verify action Bar Document option for Dev User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261598
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import core_utility
from common.locators.dialog_locators import OpenMasterFileDialog
from common.wftools import report

class C8261598_TestClass(BaseTestCase):
    
    def test_C8261598(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        report_obj = report.Report(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        cluster_box_css = "#HomeReport .cluster-box-title"
        tool_bar_css = "div[id^='BiTabBar'] div[id$='Button']:not([style*='hidden'])"
        toolbar_css = "[id*='IaToolbar']"
        
        """
        Test case variables
        """
        cluster_text = 'Report'
        expected_tooltab_buttons = ['Home', 'Insert', 'Format', 'Data', 'Slicers', 'Layout', 'View', 'Field']
        folders_text = 'Folders'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the sidebar
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5: Click on 'Document' action bar under 'InfoAssist' category
        Verify the Master File Dialog is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Document')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(OpenMasterFileDialog.PARENT_CSS, base_obj.report_medium_timesleep)
        util_obj.verify_object_visible(OpenMasterFileDialog.PARENT_CSS, True, "Step 5.1: Verify open master file dialog is displayed")
        
        """
        Step 6: Select 'wf_retail_lite.mas' > open
        Verify IA tool will open
        """
        util_obj.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        util_obj.synchronize_with_visble_text(toolbar_css, 'Series', main_page_obj.report_medium_timesleep, condition_type='asnotin')
        util_obj.synchronize_with_visble_text(cluster_box_css, cluster_text,base_obj.chart_medium_timesleep)
        tab_buttons = util_obj.validate_and_get_webdriver_objects(tool_bar_css, 'tab_buttons')
        observed_tab_list = [element.text for element in tab_buttons]
        util_obj.asequal(expected_tooltab_buttons, observed_tab_list, "Step 6.1: Verify IA tool is opened")
        
        """
        Step 7: Click on IA Globe > Exit
        """
        report_obj.select_visualization_application_menu_item('exit')
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()