"""-------------------------------------------------------------------------------------------
Created on July 10, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267154
Test Case Title =  Check Delete Section
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C5743405_TestClass(BaseTestCase):

    def test_C5743405(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        
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
            STEP 3 : Expand 'P292_S10863' domain -> 'G426906' folder;
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
 
        """
            STEP 4 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Right mouse click anywhere on the page canvas
        """
        page_canvas_obj = utils.validate_and_get_webdriver_object("div[id^=ibx-aria-id] > div.pd-page-section-grid > div:nth-child(1)", "Page Canvas")
        core_utils.right_click(page_canvas_obj)
        utils.synchronize_with_visble_text("div[class^='section-context-menu ibx-widget']", "Settings", 20)

        """
            STEP 05.01 : Verify Delete section menu is inactive
        """
        delete_section_obj = utils.validate_and_get_webdriver_object("div[class*='ibx-menu-item-disabled']", "Delete button")
        actual_output = delete_section_obj.get_attribute("class")
        msg = "Step 05.01 : Verify Delete section menu is inactive"
        utils.asin("ibx-widget-disabled", actual_output, msg)
        
        actual_result1 = delete_section_obj.value_of_css_property("opacity")
        msg = 'Step 05.02 : Verify Delete section menu is inactive'
        utils.asequal("0.5", actual_result1, msg)
    
        """
            STEP 6 : Choose Insert section below
        """        
        insert_section_css = utils.validate_and_get_webdriver_object("div[data-ibxp-label-options*='ibx-glyph-insert-after']", "insert button")
        core_utils.left_click(insert_section_css)
        
        """
            STEP 06.01 : Verify section has been inserted
        """
        pd_design.verify_number_of_page_sections(2, "Step 06.01 : Verify section has been inserted")
        
        """
            STEP 7 : Right mouse click anywhere on the first section and choose Delete from the context menu
        """
        pd_design.select_page_section_context_menu(1, "Delete section")

        """
            STEP 07.01 : Verify section has been deleted
        """
        pd_design.verify_number_of_page_sections(1, "Step 07.01 : Verify section has been deleted")

        """
            STEP 8 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
 
        """
            STEP 9 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 