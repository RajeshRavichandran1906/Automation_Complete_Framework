"""-------------------------------------------------------------------------------------------
Created on July 17, 2019
@author: Vpriya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743390
Test Case Title =  Add content into sections As New Slide
-----------------------------------------------------------------------------------------------"""
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C5743390_TestClass(BaseTestCase):

    def test_C5743390(self):
        
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
            STEP 5 : Drag Red from Retail Samples -> Portal -> Test widgets onto the canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906->P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Red", 1,"Retail Samples->Portal->Test Widgets")
        pd_design.wait_for_number_of_element("div[data-ibx-type='pdContent']",1,main_page.chart_long_timesleep)
    
        """
            STEP 6 : Drag Green over Red
        """ 
        pd_design.collapse_content_folder("Test Widgets->Portal->Retail Samples")
        pd_design.drag_content_item_to_blank_canvas("Green", 1,"Retail Samples->Portal->Test Widgets")
        utils.synchronize_until_element_is_visible("div[data-ibx-name='vbMain']", main_page.chart_long_timesleep)      
        
        """
            STEP 06.01 : Verify Add Content dialog appears as below
        """
        pd_design.verify_add_content_panel_dialog(['Replace content', 'Add content as new tab', 'Cancel'],"Step 06:01 Verify Add Content dialog appears")
        
        """
            STEP 7 : Click on 'Add content as New Tab' drop down and Choose 'Add content as New slide' option'
        """
        pd_design.select_options_from_add_content_dropdown('Add content as new slide')
        
        """
            STEP 07.01 :Verify Carousel container has been created as below
        """
        utils.synchronize_with_number_of_element(".ibx-csl-page-marker[title*='Go to slide 1 of 2']", 1, main_page.chart_long_timesleep)
        utils.verify_object_visible(".ibx-csl-page-marker[title*='Go to slide 1 of 2']",True,"Step 07:01: Verify Carousel container has been created")
        
        """
            STEP 08: Hover over the current slide navigation circle
        """
        """
            STEP 08:01 Verify tooltip appears as 'Go to slide 2 of 2'
        """
        slide_2_elem=utils.validate_and_get_webdriver_object(".ibx-csl-page-marker[title*='Go to slide 2 of 2']","Slide_one_object")
        slide_2_title=utils.get_element_attribute(slide_2_elem,'title')
        utils.asequal(slide_2_title,'Go to slide 2 of 2',"Step 08.01: Verify tooltip appears as 'Go to slide 2 of 2'")
        
        """
            STEP 9:Hover over first slide navigation circle
        """
        """
            STEP 09:01 Verify tooltip appears as 'Go to slide 1 of 2'
        """
        slide_1_elem=utils.validate_and_get_webdriver_object(".ibx-csl-page-marker[title*='Go to slide 1 of 2']","Slide_one_object")
        slide_1_title=utils.get_element_attribute(slide_1_elem,'title')
        utils.asequal(slide_1_title,'Go to slide 1 of 2',"Step 09.01: Verify tooltip appears as 'Go to slide 1 of 2'")
        
        """
            STEP 10:Click on first navigation circle
        """
        """
            STEP 10:01 Verify Red widget slide appears as below
        """
        core_utils.python_left_click(slide_1_elem)
        time.sleep(2)
        pd_design.switch_to_container_frame("Red")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        utils.asequal(color_attribute,'background-color: red;',"Step 10.01: Verify red widget slide appears")
        pd_design.switch_to_default_page()

        """
            Step 11: Click on second navigation circle
        """
        """
           STEP 11:01  Verify green widget slide appears as below
        """
        slide_2_elem=utils.validate_and_get_webdriver_object(".ibx-csl-page-marker[title*='Go to slide 2 of 2']","Slide_one_object")
        core_utils.python_left_click(slide_2_elem)
        time.sleep(2)
        pd_design.switch_to_container_frame("Red",frame_index=2)
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        utils.asequal(color_attribute,'background-color: green;',"Step 11.01: Verify green widget slide appears")

        """
            STEP 12 : Close page without saving
        """
        pd_design.switch_to_default_page()
        pd_design.close_page_designer_without_save_page()
 
        """
            STEP 13 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 