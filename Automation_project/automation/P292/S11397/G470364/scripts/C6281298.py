"""-------------------------------------------------------------------------------------------
Created on July 2, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22062741
Test Case Title =  Check Default Setting
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.page_designer_design import PageDesignerDesign
import pyautogui

class C6281298_TestClass(BaseTestCase):

    def test_C6281298(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        pd_designer = PageDesignerDesign(self.driver)
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
        
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        
        """
            STEP 3 : Expand 'P292_S11397' domain;
            Click on 'G470364' folder and click on 'page' action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
        
        """
            STEP 4 : Choose Grid 2-1 template
        """
        pd_design.select_page_designer_template("Grid 2-1")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 5 : Click on the section area in page canvas
        """
        pd_design.select_page_section(1, xoffset = 3, yoffset = 2)

        """
            STEP 6 : From the designer toolbar click open Properties pane;
            STEP 7 : Click on settings tab if not already open
        """
        pd_design.click_property()

        """
            STEP 07.01 : Verify Row height property appears as below and the default value is 60px
        """
        rowheight_textbox_obj = utils.validate_and_get_webdriver_object("input[placeholder='60px']", "row height")
        actual_value = rowheight_textbox_obj.get_attribute("placeholder").strip()
        msg = "STEP 07.01 : Verify Row height property appears as below and the default value is 60px"
        utils.asequal("60px", actual_value, msg)

        """
            STEP 8 : Enter 30px in Row height text box
        """
        par_section_obj = pd_designer._get_page_section_object(1)
        section_obj = utils.validate_and_get_webdriver_object("div[data-ibx-type='pdPageSection']", "section", parent_object=par_section_obj)
        old_height = section_obj.size['height']
        pd_design.select_property_tab_settings_option("Section Settings", "text_box", "Row height", "30px")
        pyautogui.press('enter')
        
        """
            STEP 08.01 : Verify the section has been shrunken as below
        """
        new_height = ((section_obj.size['height'])*2)
        msg = "STEP 08.01 : Verify the section has been shrunken as below"
        utils.asequal(new_height, old_height, msg)

        """
            STEP 9 : Clear 30px in Row height text box and hit enter
        """
        pd_design.select_property_tab_settings_option("Section Settings", "text_box", "Row height", "")
        pyautogui.press('enter')

        """
            STEP 09.01 : Verify the page goes back to the default height as below
        """
        new_height = section_obj.size['height']
        msg = "STEP 09.01 : Verify the page goes back to the default height as below"
        utils.asequal(new_height, old_height, msg)

        """
            STEP 10 : Click Save;
            Enter title as 'Row height testing' and click save.
        """
        pd_design.save_page_from_toolbar("Row height testing")
        
        """
            STEP 11 : Close page designer
        """
        pd_design.close_page_designer_from_application_menu()
        
        """
            STEP 12 : Signout WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main() 