"""-------------------------------------------------------------------------------------------
Created on July 4, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22062745
Test Case Title =  Check with Max Width
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design,Run as R
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.page_designer_design import PageDesignerDesign
import pyautogui
import time

class C6281307_TestClass(BaseTestCase):

    def test_C6281307(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        pd_run = R(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_page_run = Run(self.driver)
        pd_designer = PageDesignerDesign(self.driver)
        
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
        utils.synchronize_with_visble_text(content_css, "Content", 60)
 
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
 
        """
            STEP 3 : Expand 'P292_S11397' domain -> 'G470364' folder;
            Right click on 'C6281300' and select Edit
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.right_click_folder_item_and_select_menu("C6281300", "Edit")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")

        """
            STEP 4 : Click open properties pane -> Settings tab
        """
        pd_design.click_property()
        pd_design.select_property_tab("style")

        """
            STEP 5 : Change the Maximum width to 50%
        """
        pd_design.select_property_tab_style_option("Page Style", "text_box", "Maximum width", "50%")
        pyautogui.press('enter')

        """
            STEP 6 : Click on preview button
        """
        pd_design.click_preview()
        
        """
            Step 06.01 : Verify that the width changed but the sections row height remains the same as below
        """
        par_section_obj = pd_designer._get_page_section_object(1)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        page_obj = utils.validate_and_get_webdriver_object(".pd-page-canvas", "page")
        expected_width = section_obj.location['x']
        section_end_x = expected_width + section_obj.size['width']
        actual_width = page_obj.size['width'] - section_end_x
        msg = "Step 06.01 : Verify that the width changed"
        utils.asequal(expected_width, actual_width, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        page_obj = utils.validate_and_get_webdriver_object(".pd-page-canvas", "page")
        expected_width = section_obj.location['x']
        section_end_x = expected_width + section_obj.size['width']
        actual_width = page_obj.size['width'] - section_end_x
        msg = "Step 06.02 : Verify that the width changed"
        utils.asequal(expected_width, actual_width, msg)
        
        height_section1 = section_obj.size['height']
        msg = "Step 06.03 : Verify that the sections row height remains the same as below"
        utils.asequal(1636, height_section1, msg)
        
        """
            STEP 7 : Save and close page designer
        """
        pd_run.go_back_to_design_from_preview()
        pd_design.click_toolbar_save()
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
 
        """
            STEP 8 : Right click on 'C6281300' and select Run
        """
        main_page.right_click_folder_item_and_select_menu("C6281300", "Run")
        
        time.sleep(10)
        main_page_run.switch_to_frame()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 08.01 : Verify that the width changed but the sections row height remains the same as below
        """
        par_section_obj = pd_designer._get_page_section_object(1)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        page_obj = utils.validate_and_get_webdriver_object(".pd-page-canvas", "page")
        expected_width = section_obj.location['x']
        section_end_x = expected_width + section_obj.size['width']
        actual_width = page_obj.size['width'] - section_end_x
        msg = "Step 08.01 : Verify that the width changed"
        utils.asequal(expected_width, actual_width, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        page_obj = utils.validate_and_get_webdriver_object(".pd-page-canvas", "page")
        expected_width = section_obj.location['x']
        section_end_x = expected_width + section_obj.size['width']
        actual_width = page_obj.size['width'] - section_end_x
        msg = "Step 08.02 : Verify that the width changed"
        utils.asequal(expected_width, actual_width, msg)
                
        height_section1 = section_obj.size['height']
        msg = "Step 08.03 : Verify that the sections row height remains the same as below"
        utils.asequal(1636, height_section1, msg)

        """
            STEP 9 : Close page
        """
        main_page_run.switch_to_default_content()
        main_page_run.close()

        """
            STEP 10 : Signout WF
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 