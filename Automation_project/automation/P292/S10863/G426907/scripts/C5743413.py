"""-------------------------------------------------------------------------------------------
Created on July 17, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267162&group_by=cases:section_id&group_id=426907&group_order=asc
Test Case Title =  Delete Container Menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main

class C5743413_TestClass(BaseTestCase):

    def test_C5743413(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_obj=main(self.driver)
    
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
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(content_css, "Content", main_page.home_page_medium_timesleep)
        
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
            STEP 5 : Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906")
        pd_design.collapse_content_folder("P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        pd_design.wait_for_number_of_element("div[class^='pd-toolbar-filter']", 1, 30)
 
        """
            STEP 6 : Right mouse click anywhere on the container to pull up the context menu.
        """
        container_obj = utils.validate_and_get_webdriver_object("div[class*='pd-container-title-bar']", "Container css")
        core_utils.left_click(container_obj)
        core_utils.right_click(container_obj)
        pd_design.wait_for_visible_text(".pop-effect-menu", "Style")
        
        """
            Step 06.01 : Verify context menus and its icons appears as below
        """
        main_obj.verify_context_menu_item(['Refresh', 'Edit title', 'Settings', 'Style', 'Delete container'], "Step 06.01 : Verify context menus and its icons appears as below")
        utils.verify_picture_using_sikuli("C5743413_step6.png", "Step 06.01 : Verify context menus and its icons appears as below")

        """
            STEP 7 : Click on the delete option in the context menu
        """
        main_obj.select_context_menu_item("Delete container")
        utils.synchronize_until_element_disappear("div[data-ibx-type='pdContainer']", 20)

        """
            Step 07.01 : Verify Category sales panel has been deleted
        """
        pd_design.verify_number_of_panels(0, "Step 07.01 : Verify Category sales panel has been deleted")

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