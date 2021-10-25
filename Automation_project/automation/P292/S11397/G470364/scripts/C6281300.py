"""-------------------------------------------------------------------------------------------
Created on July 3, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6281300
Test Case Title =  Check with Page Margin
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

class C6281300_TestClass(BaseTestCase):

    def test_C6281300(self):
        
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
        
        def verify_container_margin(step_num):
            container_obj = utils.validate_and_get_webdriver_objects(".pd-page-canvas .grid-stack-item-content", "Container CSS")
            actual_padding = []
            for container in container_obj :
                padding_left = container.value_of_css_property('padding-left')
                padding_right = container.value_of_css_property('padding-right')
                padding_top = container.value_of_css_property('padding-top')
                padding_bottom = container.value_of_css_property('padding-bottom')
                margin = padding_left if padding_left == padding_right == padding_top == padding_bottom else ''
                actual_padding.append(margin)
            Expected_list = ['1px', '1px', '1px', '1px', '1px', '1px', '1px', '1px', '1px', '1px', '1px', '1px', '1px']
            msg = "Step {0} : Verify that the space between panels has been changed as below for both the sections.".format(step_num)
            utils.asequal(Expected_list, actual_padding, msg)
        
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
            STEP 4 : Click open properties pane -> Style tab
        """
        pd_design.click_property()
        pd_design.select_property_tab("style")
        time.sleep(5)

        """
            STEP 04.01 : Verify the default value is 20px under Page style
        """
        margin_obj = utils.validate_and_get_webdriver_object(".page-styles input[placeholder='20px']", "Margin css")
        actual_value = margin_obj.get_attribute("placeholder").strip()
        msg = "STEP 04.01 : Verify the default value is 20px under Page style"
        utils.asequal("20px", actual_value, msg)
        
        """
            STEP 5 : Change the Margin to 2px
        """
        margin_texbox_obj = utils.validate_and_get_webdriver_object(".page-styles input[placeholder='20px']", 'margin_css')
        margin_texbox_obj.click()
        margin_texbox_obj.send_keys("2px")
        time.sleep(5)
        pyautogui.press('enter')

        """
            STEP 05.01 : Verify that the space between panels has been changed as below for both the sections.
            but the row height is still the same for both sections as below
        """
        verify_container_margin("05.01")
        par_section_obj = pd_designer._get_page_section_object(1)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        height_section1 = section_obj.size['height']
        msg = "Step 05.02 : row height is still the same for both sections as below"
        utils.asequal(480, height_section1, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        height_section2 = section_obj.size['height']
        msg = "Step 05.03 : row height is still the same for both sections as below"
        utils.asequal(1320, height_section2, msg)
        
        """
            STEP 6 : Click on Section1 and click on settings tab
        """
        pd_design.select_page_section(1, location='bottom_left', xoffset=5, yoffset=-5)
        pd_design.select_property_tab("Settings")

        """
            STEP 06.01 : Verify the Row height is 30px
        """
        rowheight_textbox_obj = utils.validate_and_get_webdriver_object("input[placeholder='60px']", "row height")
        actual_value = rowheight_textbox_obj.get_attribute("value").strip()
        msg = "Step 06.01 : Verify the Row height is 30px"
        utils.asequal("30px", actual_value, msg)

        """
            STEP 7 : Click on Section2
        """
        pd_design.select_page_section(2)

        """
            STEP 07.01 : Verify the Row height is 60px
        """
        rowheight_textbox_obj = utils.validate_and_get_webdriver_object("input[placeholder='60px']", "row height")
        actual_value = rowheight_textbox_obj.get_attribute("placeholder").strip()
        msg = "Step 07.01 : Verify the Row height is 60px"
        utils.asequal("60px", actual_value, msg)
        
        """
            STEP 8 : Click the preview button
        """
        pd_design.click_preview()

        """
            STEP 08.01 : Verify that the space between panels has been changed as below for both the sections but the row height is still the same for both sections.
        """
        verify_container_margin("08.01")
        par_section_obj = pd_designer._get_page_section_object(1)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        height_section1 = section_obj.size['height']
        msg = "Step 08.02 : row height is still the same for both sections as below"
        utils.asequal(480, height_section1, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        height_section2 = section_obj.size['height']
        msg = "Step 08.03 : row height is still the same for both sections as below"
        utils.asequal(1320, height_section2, msg)

        """
            STEP 9 : Close Preview.
        """
        pd_run.go_back_to_design_from_preview()
 
        """
            Click save as and enter "C6281300_1" and close designer
        """
        pd_design.save_as_page_from_application_menu("C6281300_1")
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)

        """
            STEP 11 : Right click on 'C6281300_1' and select Run
        """
        main_page.right_click_folder_item_and_select_menu("C6281300_1", "Run")
        time.sleep(10)
        main_page_run.switch_to_frame()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")

        """
            STEP 11.01 : Verify that the space between panels has been changed as below for both the sections but the row height is still the same for both sections.
        """
        verify_container_margin("11.01")
        par_section_obj = pd_designer._get_page_section_object(1)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        height_section1 = section_obj.size['height']
        msg = "Step 11.02 row height is still the same for both sections as below"
        utils.asequal(480, height_section1, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        height_section2 = section_obj.size['height']
        msg = "Step 11.03 row height is still the same for both sections as below"
        utils.asequal(1320, height_section2, msg)
        
        """
            STEP 12 : Close page
        """
        main_page_run.switch_to_default_content()
        main_page_run.close()

        """
            STEP 13 : Signout WF
        """
        main_page.signout_from_username_dropdown_menu()
    
if __name__ == '__main__':
    unittest.main() 