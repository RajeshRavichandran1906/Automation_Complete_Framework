"""-------------------------------------------------------------------------------------------
Created on July 09, 2019
@author: Prabhakaran

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459324
Test Case Title =  Create,Edit and Run Shortcut
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.lib.webfocus.resource_dialog import Resource_Dialog
from common.pages.wf_mainpage import Wf_Mainpage as wf_page
from selenium.webdriver import ActionChains
from common.lib.javascript import JavaScript
import time

class C6459324_TestClass(BaseTestCase):

    def test_C6459324(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        main_page_run = Run(self.driver)
        resource_dialog = Resource_Dialog(self.driver)
        wf_Mp = wf_page(self.driver)
         
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
            STEP 4 : Click on Shortcut action tile from under Other category
        """
        main_page.select_action_bar_tab("Other")
        main_page.select_action_bar_tabs_option("Shortcut")
        utils.synchronize_with_visble_text("div[class*='dialog-cancel-button']", "Cancel", 20)

        """
            STEP 04.01 : Verify New Shortcut dialog opens as below
        """
        shortcut_dialog_obj = utils.validate_and_get_webdriver_object(".create-new-shortcut", "Shortcut dialog")
        actual_result = shortcut_dialog_obj.is_displayed()
        msg = "Step 04.01 : Verify New Shortcut dialog opens as below"
        utils.asequal(True, actual_result, msg)

        """
            STEP 5 : Leave Type as Repository File by default and then Click browse button on Target path.
        """
        browse_button_obj = utils.validate_and_get_webdriver_object("#sdbtnBrowse", "Browse button")
        core_utils.left_click(browse_button_obj)
        utils.synchronize_with_visble_text(".open-dialog-resources", "Cancel", 30)

        """
            STEP 05.01 : Verify the breadcrumb appears as Domains > P292_S11397 > G490183
        """
        main_page.verify_crumb_box("Domains->P292_S11397->G490183", "Step 05.01")

        """
            STEP 6 : Choose 'Explorer Widget page' > Click Select button.
        """
        resource_dialog.select_crumb_item("Domains")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("P292_S11397->G490183", "Explorer Widget page")
        pd_design.resource_dialog().click_button("Select")
        utils.synchronize_with_visble_text(".ibx-dialog-ok-button", "OK", 30)
        
        """
            STEP 06.01 : Verify that the Target Path is displayed and greyed out as below
        """
        target_path_obj = utils.validate_and_get_webdriver_object("#sdtxtTargetPath", "Target path")
        actual_result = target_path_obj.get_attribute("class")
        msg = "Step 06.01 : Verify that the Target Path is displayed and greyed out as below"
        utils.asin("ibx-widget-disabled", actual_result, msg)
        
        actual_result1 = target_path_obj.value_of_css_property("opacity")
        msg = "Step 06.02 : Verify that the Target Path is displayed and greyed out as below"
        utils.asequal("0.5", actual_result1, msg)

        """
            STEP 7 : Enter Title as 'Content - Shortcut' > Click OK.
        """
        main_page.enter_new_folder_title_in_popup_dialog("Content - Shortcut")
        ok_button_obj = utils.validate_and_get_webdriver_object(".ibx-dialog-ok-button", "Ok button css")
        core_utils.left_click(ok_button_obj)

        """
            STEP 07.01 : Verify that the 'Content - Shortcut' is created and listed under G490183 folder
        """
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.verify_items_in_grid_view(["Content - Shortcut"], "asin", "Step 07.01 : Verify that the 'Content - Shortcut' is created and listed under G490183 folder")      

        """
            STEP 8 : Double click on 'Content - Shortcut'
        """
        pd_design.run_page_designer_by_double_click("Content - Shortcut")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        """
            STEP 08.01 : Verify 'Explorer Widget page' runs inside 'Explorer Widget page' as below
        """
        main_page.verify_items_in_grid_view(["Content - Shortcut"], "asin", "Step 08.01 : Verify 'Explorer Widget page' runs inside 'Explorer Widget page' as below")      
        
        """
            STEP 9 : Right click on 'Content - Shortcut'> Edit.
        """
        content_obj = wf_Mp.get_domain_folder_item("Content - Shortcut")
        JavaScript(self.driver).scrollIntoView(content_obj)
        ActionChains(self.driver).context_click(content_obj).perform()
        menu_obj = self.driver.find_element_by_xpath("//div[contains(@class, 'pop-top')]//div[normalize-space()='Edit'][@class='ibx-label-text']")
        ActionChains(self.driver).move_to_element(menu_obj).click().perform()
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(".pd-page-title", "Page", 30)

        """
            STEP 09.01 : Verify page designer opens in new tab
        """
        time.sleep(15)
        pd_design.switch_to_container_frame("Panel 1", 1)
        main_page.verify_items_in_grid_view(["Content - Shortcut"], "asin", "Step 09.01 : Verify page designer opens in new tab")      
        pd_design.switch_to_default_page()

        """
            STEP 10 : Close designer
        """
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        time.sleep(10)
        
        """
            STEP 11 : Close the 'Explorer widget' page run window.
        """
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)

        """
            STEP 11.01 : Verify Home page is displayed and 'Content- Shortcut' is listed under G490183 folder
        """
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.verify_items_in_grid_view(["Content - Shortcut"], "asin", "Step 11.01 : Verify Home page is displayed and 'Content- Shortcut' is listed under G490183 folder")      
        
        """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 