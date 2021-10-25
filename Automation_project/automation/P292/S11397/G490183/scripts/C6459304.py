"""-------------------------------------------------------------------------------------------
Created on June 26, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22062768
Test Case Title =  Verify to create a new folder
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
import time

class C6459304_TestClass(BaseTestCase):

    def test_C6459304(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        main_page_run = Run(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        
        """
            STEP 3 : Expand 'P292_S11397' domain -> 'G490183' folder;
            Double click on 'Explorer Widget page'
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        """
            STEP 4 : Click on 'Folder' action bar
        """
        main_page.select_action_bar_tab("Common")
        main_page.select_action_bar_tabs_option("Folder")
        
        """
            STEP 04.01 : Verify that 'New Folder' dialog opens as below with the cursor being in Title text box by default;
            OK button is disabled;
            Cancel button is enabled;
            X icon is available
        """
        main_page.verify_new_folder_title_value("", "04.01")
        main_page.verify_button_enable_or_disable_on_popup_dialog("OK", "step 04.02 : OK button is disabled", enable=False)
        main_page.verify_button_enable_or_disable_on_popup_dialog("Cancel", "step 04.03 : Cancel button is enabled", enable=True)
        utils.verify_object_visible("div[class^='ibx-title-bar-close-button']", True, "step 04.04  : X icon is available")
        
        """
            STEP 5 : Enter Title as 'Explorer Test'
        """
        main_page.enter_new_folder_title_in_popup_dialog("Explorer Test")
        
        """
            STEP 05.01 : Verify the name field takes in 'Explore_Test' by default and OK button is enabled.
        """
        main_page.verify_new_folder_name_in_popup_dialog("Explorer_Test", "STEP 05.01 : Verify the name field takes in 'Explore_Test' by default")
        main_page.verify_button_enable_or_disable_on_popup_dialog("OK", "step 04.02 : OK button is enabled", enable=True)
        
        """
            STEP 6 : Click on OK button
        """
        main_page.click_button_on_popup_dialog("OK")
        utils.synchronize_with_visble_text("div[class^='folder-div ibx-widget']", "Explorer", 30)
        
        """
            STEP 06.01 : Verify 'Explorer Test' folder is created and listed under 'P292_S11397' domain -> 'G490183' folder
        """
        main_page.verify_folders_in_grid_view(["Explorer Test"], "asin", "STEP 06.01 : Verify 'Explorer Test' folder is created and listed under 'P292_S11397' domain -> 'G490183' folder")
        
        """
            STEP 7 : Right click on 'Explorer Test' folder and make publish.
        """
        main_page.right_click_folder_item_and_select_menu("Explorer Test", "Publish")
        time.sleep(15)
        
        """
            STEP 07.01 : Verify the folder is published
        """
        main_page.verify_content_area_folder_publish_or_unpublish("Explorer Test", "publish", "STEP 07.01 : Verify the folder is published")
        
        """
            STEP 8 : Close Explorer widget page
        """
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
            STEP 9 : Refresh home page
        """
        self.driver.refresh()
        utils.synchronize_with_visble_text("div[class^='folder-div ibx-widget ibx-flexbox ']", "Explorer", 30)

        """
            STEP 09.01 : Verify 'Explorer Test' folder is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        main_page.verify_folders_in_grid_view(["Explorer Test"], "asin", "STEP 08.01 : Verify 'Explorer Test' folder is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page")
        
        """
            STEP 10 : Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main() 