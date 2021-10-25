"""-------------------------------------------------------------------------------------------
Created on July 17, 2019
@author: Vishnu_priya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743403
Test Case Title =  Check Combine menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main
import keyboard as virtual_keyboard
import time


class C5743403_TestClass(BaseTestCase):

    def test_C5743403(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
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
        
        def multi_select_filter_panel():
            virtual_keyboard.press('ctrl')
            pd_design.select_filter_control_panel(6)
            virtual_keyboard.release('ctrl')
            
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
        STEP 5: Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906")
        pd_design.collapse_content_folder("P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        utils.synchronize_until_element_is_visible("div[title='Quick filter']",main_obj.chart_long_timesleep)
        
        """
        STEP 6: Click on quick filter icon
        """
        pd_design.click_quick_filter()
        utils.synchronize_until_element_is_visible('[data-ibx-type="pdFilterPanel"]',main_page.home_page_long_timesleep)
        
        """
        STEP 7:Multi select the 'From' and 'To' Date filter controls. ( HOLD DOWN the CTRL button on the keyboard to multi select both options)
        """
        pd_design.select_filter_control_panel(5)
        time.sleep(5)
        multi_select_filter_panel()
        time.sleep(5)
        
        """
        STEP 8:Right mouse click on 'To' control 
        """
        """
        Step 08:01 Verify the context menu appears as below
        """
        pd_design.select_filter_control_panel(6,click_type='right',click_on_location='middle')
        main_obj.verify_context_menu_item(['Edit label', 'Combine', 'Settings', 'Style', 'Delete control'],"Step:08:01 Verify the context menu appears as below")
         
        """
        STEP 09:Choose the 'Combine' option in the context menu.
        
        Verify both controls has been combined into one cell as below
        """
        main_obj.select_context_menu_item('Combine')
        filter_grid_elem=utils.validate_and_get_webdriver_objects("div[class*='pd-filter-cell']","filter_grid_object")
        To_grid_text=filter_grid_elem[5].text
        utils.asequal('',To_grid_text,"Step:09 Verify both controls has been combined into one cell as below")
        
        """
        STEP 10:Right click on the combined control (From)
        Verify split doesn't appear in the context menu;
        Verify only below context menus appears with its icons
        """
        pd_design.select_filter_control_panel(5,click_type='right')
        main_obj.verify_context_menu_item(['Split'],"Step:08:01 Verify the context menu appears as below",comparision_type='asnotin')
        utils.verify_picture_using_sikuli("C5743403_step10.png", msg="Step 10:01")
        
        """
        STEP 11: Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
 
        """
        STEP 12 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()