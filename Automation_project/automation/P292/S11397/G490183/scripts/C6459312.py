"""-------------------------------------------------------------------------------------------
Created on July 09, 2019
@author: vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459312
Test Case Title =  Create,Edit and Run V4 Portal 
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.pages import vfour_portal_canvas, vfour_portal_ribbon
import time


class C6459312_TestClass(BaseTestCase):

    def test_C6459312(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_run = Run(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
        
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
        
        expected_title="Portal Designer"
        
        def select_column(column_no):
            """
            Desc:- This function is used to slect coloumn default is middle in BIP file so updtaed in script level 
            """
            elem=portal_canvas.get_column_obj(column_no)
            utils.click_on_screen(elem, 'top_middle', click_type=0,y_offset=2)
        
        
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
        Step 4:Click on Collaborative Portal action tile from under Other category;
        Verify New Portal dialog appears as below
        """
        main_page.select_action_bar_tab('Other')
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'Collaborative Portal', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Collaborative Portal')
        
        """
        Step 5:Enter Title 'V4 Portal' and click Create button
        Verify V4 portal design mode opens in a new tab
        """
        main_page.enter_new_folder_title_in_popup_dialog("V4 Portal")
        main_page.click_button_on_popup_dialog("Create")
        core_utils.switch_to_new_window()
        actual_title=self.driver.title
        utils.asequal(actual_title,expected_title,"Step 5.1")

        """
        Step 6:Choose 1 Column in Templates dialog;
        Click Create
        """
        portal_canvas.add_page('1 Column',page_verify=False)
        time.sleep(3)
        utils.synchronize_until_element_is_visible(".selection-marquee",main_page.chart_long_timesleep)

        """
        Step 7:Press F8 to invoking resource tree
        Expand 'P292_S11397' domain -> 'G490183' folder;
        Drag and drop 'Report' into 1 Column.
        """
        portal_ribbon.select_ribbon_item("Insert", 'Insert_WebFOCUSResources')
        utils.synchronize_with_visble_text(".bi-tool-bar.window-caption",' WebFOCUS Resources',main_page.chart_long_timesleep)
        portal_canvas.dragdrop_repository_item_to_canvas(repository_folder+"->Report1","column",1,)
        time.sleep(10)
        
 
        """
        Verify that the content is placed into the 1 Column page as below
        """
        column1 = portal_canvas.get_column_obj(1)
        self.driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        actual_text=self.driver.find_element_by_css_selector("table>tbody>tr>td").text
        expected_text='CAR'
        utils.asequal(actual_text,expected_text,"Step 7:Verify that the content is placed into the 1 Column page as below")

        """
        Step 8:Click Save;
        Click OK button
        """
        """
        step 9:Click on BIP application main menu;
        Select Exit.
        Verify 'V4 Portal' is created and listed under 'G490183' folder
        """
        utils.switch_to_default_content()
        portal_ribbon.select_save_from_toolbar()
        core_utils.switch_to_previous_window()
        time.sleep(2)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page.verify_items_in_grid_view(["V4 Portal"],"asin","Step 9.1 Verify 'Report' is available under 'G490183' folder in content area as below")

        """
        Step 10:Double click on 'V4 Portal'.
        Verify that the V4 Portal runs in a new tab as below
        """
        """
        Step 11:Click close from the menu bar
        """
        pd_design.run_page_designer_by_double_click("V4 Portal")
        core_utils.switch_to_new_window()
        select_column(1)
        column1 = portal_canvas.get_column_obj(1)
        self.driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        actual_text=self.driver.find_element_by_css_selector("table>tbody>tr>td").text
        expected_text='CAR'
        utils.asequal(actual_text,expected_text,"Step 11.1:Verify that the content is placed into the 1 Column page as below")
        core_utils.switch_to_previous_window()
        
        """
        Step 12:Right click on 'V4 Portal' from content area and select Edit
        Verify that the V4 portal opens in design mode
        """
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page.right_click_folder_item_and_select_menu("V4 Portal","Edit")
        core_utils.switch_to_new_window()
        select_column(1)
        column1 = portal_canvas.get_column_obj(1)
        self.driver.switch_to.frame(column1.find_element_by_css_selector("[class*='bi-iframe iframe'][name^='Panel']"))
        actual_text=self.driver.find_element_by_css_selector("table>tbody>tr>td").text
        expected_text='CAR'
        utils.asequal(actual_text,expected_text,"Step 12:Verify that the content is placed into the 1 Column page as below")
        
        """
        Step 13:Click on BIP application main menu;
        Select Exit.
        """
        
        time.sleep(5)
        core_utils.switch_to_previous_window()

 
        """
        Step 14:Close the 'Explorer widget' page run window
        Verify 'V4 Portal' is listed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer",main_page.home_page_medium_timesleep)
        main_page.verify_items_in_grid_view(["V4 Portal"],"asin","Step 14.1 Verify 'Portal Page' is available under 'G490183' folder in content area as below")

        
        """
        Step 15:Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
 

 

 
if __name__ == '__main__':
    unittest.main() 