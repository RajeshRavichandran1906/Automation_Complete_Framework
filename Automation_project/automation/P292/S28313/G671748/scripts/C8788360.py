'''
Created on March 12, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788360
Testcase Name : Verify action Bar Reporting Object option for Admin User
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart
from common.locators.dialog_locators import OpenMasterFileDialog

class C8788360_TestClass(BaseTestCase):

    def test_C8788360(self):
        
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        expected_tree_items=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        content_box_css = ".content-box"
        reporting_object_css="#roTree .bi-tree-view-table tr"
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(repository_css, 'Workspaces', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Workspaces')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, 'Data', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Data' category button
        """
        main_page_obj.select_action_bar_tab('Data')
        util_obj.synchronize_with_visble_text(content_box_css, 'Reporting Object', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on 'Reporting Object' action bar under 'Data' category
                Verify the Master File Dialog is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Reporting Object')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(OpenMasterFileDialog.PARENT_CSS, main_page_obj.home_page_medium_timesleep)
        util_obj.verify_object_visible(OpenMasterFileDialog.PARENT_CSS, True, "Step 5.1: Verify open master file dialog is displayed")
        
        """
        Step 6: Select 'wf_retail_lite.mas' > open
                Verify Reporting Object tool opens
        """
        util_obj.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        util_obj.synchronize_with_visble_text(reporting_object_css, 'Reporting Object', main_page_obj.home_page_medium_timesleep)
        reporting_tree_object = util_obj.validate_and_get_webdriver_objects(reporting_object_css, 'Reporting object tree items')
        actual_tree_items = [item.text.replace('\n','') for item in reporting_tree_object if item.text.strip()!='' and item.is_displayed()]
        util_obj.asequal(expected_tree_items, actual_tree_items, "Step 6:Verify reporting object tree items")
        
        """
        Step 7: Click on RO Globe > Exit > No
        """
        chart_obj.select_ia_exit_from_application_btn()
        chart_obj.click_any_bibutton_in_dialog(btn_name='No')
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out
        """
        core_utilobj.switch_to_previous_window(window_close=False)
        main_page_obj.signout_from_username_dropdown_menu()
        

if __name__ == "__main__":
    unittest.main()