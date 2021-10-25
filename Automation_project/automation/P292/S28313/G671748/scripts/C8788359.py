'''
Created on March 12, 2019

@author: AA14564
Testcase Name : Verify action Bar Document option for Admin User
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788359
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators.dialog_locators import OpenMasterFileDialog
from common.wftools import report

class C8788359_TestClass(BaseTestCase):
    
    def test_C8788359(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        report_obj = report.Report(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        tool_bar_css = "div[id^='BiTabBar'] div[id$='Button']:not([style*='hidden'])"
        repository_css = "div[class='ibfs-tree']"
        document_canvas_css = "#resultArea #theCanvas"
        content_box_css = ".content-box"
        toolbar_css = "[id*='IaToolbar']"
        
        """
        Test case variables
        """
        expected_tooltab_buttons = ['Home', 'Insert', 'Format', 'Data', 'Slicers', 'Layout', 'View', 'Field']
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(repository_css, 'Workspaces', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Workspaces')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(content_box_css, 'InfoAssist', main_page_obj.home_page_medium_timesleep)
        
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
        util_obj.synchronize_until_element_is_visible(OpenMasterFileDialog.PARENT_CSS, main_page_obj.report_medium_timesleep)
        util_obj.verify_object_visible(OpenMasterFileDialog.PARENT_CSS, True, "Step 5.1: Verify open master file dialog is displayed")
        
        """
        Step 6: Select 'wf_retail_lite.mas' > open
        Verify IA tool will open
        """
        util_obj.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        util_obj.synchronize_with_visble_text(toolbar_css, 'Series', main_page_obj.report_medium_timesleep, condition_type='asnotin')
        tab_buttons = util_obj.validate_and_get_webdriver_objects(tool_bar_css, 'tab_buttons')
        observed_tab_list = [element.text for element in tab_buttons]
        util_obj.asequal(expected_tooltab_buttons, observed_tab_list, "Step 6.1: Verify IA tool is opened")
        util_obj.verify_object_visible(document_canvas_css, True, "Step 6.2: Verify IA tool document result canvas is displayed.")
        
        """
        Step 7: Click on IA Globe > Exit
        """
        report_obj.select_visualization_application_menu_item('exit')
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'InfoAssist', main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()