"""-------------------------------------------------------------------------------------------
Created on July 18, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267157&group_by=cases:section_id&group_id=426907&group_order=asc
Test Case Title =  Edit Container title
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main
import pyautogui
import time

class C5743408_TestClass(BaseTestCase):

    def test_C5743408(self):
        
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
            STEP 5 : Drag and drop Panel container to the page canvas
        """ 
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Panel", 1)
 
        """
            STEP 6 : Right mouse click anywhere on the container
        """
        container_obj = utils.validate_and_get_webdriver_object(".pd-container-title-bar", "Container css")
        core_utils.left_click(container_obj)
        core_utils.right_click(container_obj)
        pd_design.wait_for_visible_text(".ibx-popup", "Style")
        
        """
            Step 06.01 : Verify context menus and its icons appears as below
        """
        main_obj.verify_context_menu_item(['Refresh', 'Edit title', 'Settings', 'Style', 'Delete container'], "Step 06.01 : Verify context menus and its icons appears as below")
        
        """
            STEP 7 : Click on 'Edit title'
        """
        main_obj.select_context_menu_item("Edit title")
        
        """
            Step 07.01 : Verify title will be highlighted in blue color
        """
        utils.verify_picture_using_sikuli("C5743408_step7.png", "Step 07.01 : Verify title will be highlighted in blue color")
        
        """
            STEP 8 : Enter 'Panel 1- changed' and click any where outside the panel in page canvas
        """
        time.sleep(5)
        pyautogui.typewrite("Panel 1- changed", 0.25)
        Page_click_obj = utils.validate_and_get_webdriver_object("div[id^='ibx-aria-id'] > div.pd-page-section-grid > div:nth-child(4)", "Page Click css")
        core_utils.python_move_to_element(Page_click_obj)
        core_utils.python_left_click(Page_click_obj)
        
        """
            Step 08.01 : Verify title is now changed as 'Panel 1- changed'
        """
        pd_design.verify_containers_title(['Panel 1- changed'], "Step 08.01 : Verify title is now changed as 'Panel 1- changed'")
        
        """
            STEP 9 : Double click on 'Panel 1- changed' title
        """
        panel_css = utils.validate_and_get_webdriver_object(".pd-container-title ", "Panel css")
        core_utils.python_doubble_click(panel_css)
        time.sleep(5)
        
        """
            Step 09.01 : Verify title will be highlighted in blue color
        """
        utils.verify_picture_using_sikuli("C5743408_step9.png", "Step 09.01 : Verify title will be highlighted in blue color")

        """
            STEP 10 : Enter 'Panel 1- restored' and click any where outside the panel in page canvas
        """
        time.sleep(5)
        pyautogui.typewrite("Panel 1- restored", 0.25)
        Page_click_obj = utils.validate_and_get_webdriver_object("div[id^='ibx-aria-id'] > div.pd-page-section-grid > div:nth-child(4)", "Page Click css")
        core_utils.python_move_to_element(Page_click_obj)
        core_utils.python_left_click(Page_click_obj)
        
        """
            Step 10.01 : Verify title is now changed as 'Panel 1- restored'
        """
        pd_design.verify_containers_title(["Panel 1- restored"], "Step 10.01 : Verify title is now changed as 'Panel 1- restored'")
        
        """
            STEP 11 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        
        """
            STEP 12 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()