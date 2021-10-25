"""-------------------------------------------------------------------------------------------
Created on July 10, 2019
@author: Vpriya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743391
Test Case Title =  Add content into sections As New Tab
-----------------------------------------------------------------------------------------------"""
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C5743391_TestClass(BaseTestCase):

    def test_C5743391(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        pd_preview = page_designer.Preview(self.driver)
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
            STEP 5 : Drag 'Grey' from Retail Samples -> Portal -> Test widgets onto the canvas 
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906->P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Gray", 1,"Retail Samples->Portal->Test Widgets")
        pd_design.wait_for_number_of_element("div[data-ibx-type='pdContent']",1,main_page.chart_long_timesleep)
    
        """
            STEP 6 : Drag yellow over Grey
        """ 
        pd_design.collapse_content_folder("Test Widgets->Portal->Retail Samples")
        pd_design.drag_content_item_to_blank_canvas("Yellow", 1,"Retail Samples->Portal->Test Widgets")
        utils.synchronize_until_element_is_visible("div[data-ibx-name='vbMain']", main_page.chart_long_timesleep)      
        
        """
            STEP 06.01 : Verify Add Content dialog appears as below
        """
        pd_design.verify_add_content_panel_dialog(['Replace content', 'Add content as new tab', 'Cancel'],"Step 06:01 Verify Add Content dialog appears")
        
        """
            STEP 7 : Choose 'Add content as new tab'
        """
        pd_design.select_options_add_content_dialog("Add content as new tab")

        """
            STEP 07.01 : Verify new tabbed Container has been created as below
        """
        pd_preview.tab_container("Gray").verify_selected_tab(["Yellow"],"Step 07:01")
        
        """
            STEP 08: Click the Add tab plus sign 15 times (once the tab overflows, use ellipsis + icon to add new tabs)
        """
        for n in range(3):
            if n < 3:
                time.sleep(2)
                pd_preview.tab_container("Gray").click_new_tab_plus_icon()
        
        for n in range(12):
            if n < 12:
                time.sleep(2)
                pd_preview.tab_container("Gray").click_tab_overflow_icon()
                pd_preview.tab_container("Gray").click_new_tab_plus_icon_in_tab_overflow_popup()

        """
            STEP 09: Click on ellipsis
        """
        
        pd_preview.tab_container("Gray").click_tab_overflow_icon()
        
        
        """
            STEP 09:01 Verify Gray, Yellow, Tab 3, Tab 4, Tab 5, Tab 6, Tab 7, Tab 8, Tab 9, Tab 10, Tab 11, Tab 12, Tab 13, Tab 14, Tab 15, Tab 16, Tab 17 appears as below.
        """
        
        pd_preview.tab_container("Gray").verify_tabs_in_tab_overflow_popup(['Gray', 'Yellow', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6', 'Tab 7', 'Tab 8', 'Tab 9', 'Tab 10', 'Tab 11', 'Tab 12', 'Tab 13', 'Tab 14', 'Tab 15', 'Tab 16', 'Tab 17'],"Step 9.01")
        
        
        """
            STEP 10: Click on Yellow
            Verify yellow tab appears as below
        """
        
        pd_preview.tab_container("Gray").click_tab_overflow_icon()
        pd_preview.tab_container("Gray").select_tab_from_tab_overflow_popup("Yellow")
        pd_design.switch_to_container_frame("Gray",1)
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        utils.asequal(color_attribute,'background-color: yellow;',"Step 10.1")
        

        """
            STEP 11 : Close page without saving
        """
        pd_design.switch_to_default_page()
        pd_design.close_page_designer_without_save_page()
 
        """
            STEP 12 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 