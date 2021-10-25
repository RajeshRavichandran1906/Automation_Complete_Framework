"""-------------------------------------------------------------------------------------------
Created on June 27, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22062771
Test Case Title =  Create, Edit and Run Visualization
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.wftools.visualization import Visualization
from common.wftools.chart import Chart

class C6459307_TestClass(BaseTestCase):

    def test_C6459307(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        main_page_run = Run(self.driver)
        visual = Visualization(self.driver)
        chart = Chart(self.driver)
        
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
        qwerty_tree_css = "#queryTreeWindow"
        
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
            STEP 4 : Click on Visualization action tile from under InfoAssist category;
        """
        main_page.select_action_bar_tab("InfoAssist")
        main_page.select_action_bar_tabs_option("Visualization")
        core_utils.switch_to_new_window()

        """
            STEP 5 : Select car.mas under ibisamp folder and Click open
        """
        utils.select_masterfile_in_open_dialog("ibisamp", "car")
        utils.synchronize_with_visble_text("#pfjTableChart_1", "Drop", 60)
 
        """
            STEP 6 : Double click on 'CAR' from Dimensions and 'SALES' from Measures.
        """
        visual.double_click_on_datetree_item("CAR", 1)
        visual.wait_for_visible_text(qwerty_tree_css, "CAR")
        
        visual.double_click_on_datetree_item("SALES", 1)
        visual.wait_for_visible_text(qwerty_tree_css, "SALES")

        """
            STEP 06.01 : Verify Live Preview appears as below
        """
        visual.verify_x_axis_title(["CAR"], msg="step 06.01")
        visual.verify_y_axis_title(["SALES"], msg="step 06.02")
        visual.verify_x_axis_label(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 06.03")
        visual.verify_y_axis_label(["0", "20K", "40K", "60K", "80K", "100K"], msg="step 06.04")
        visual.verify_number_of_risers("#ar_TableChart_1 rect", 1, 10, msg="step 06.05")
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", "bar_blue", msg="step 06.06")

        """
            STEP 7 : Click Run.
        """
        visual.run_visualization_from_toptoolbar()

        """
            STEP 07.01 : Verify chart runs without any error as below
        """
        core_utils.switch_to_new_window()
        visual.verify_x_axis_title(["CAR"], msg="step 07.01")
        visual.verify_y_axis_title(["SALES"], msg="step 07.02")
        visual.verify_x_axis_label(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 07.03")
        visual.verify_y_axis_label(["0", "20K", "40K", "60K", "80K", "100K"], msg="step 07.04")
        visual.verify_number_of_risers("#MAINTABLE_wbody1 rect", 1, 10, msg="step 07.05")
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", "bar_blue", msg="step 07.06")
        
        """
            STEP 8 : Close run window
        """
        core_utils.switch_to_previous_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1", "CAR")

        """
            STEP 9 : Click save;
            Enter title as 'Visual' and Click Save
        """
        chart.select_ia_toolbar_item("toolbar_save")
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        
        chart.save_file_in_save_dialog("Visual")

        """
            STEP 10 : Close IA
            Verify 'Visual' is available under 'G490183' folder in content area as below
        """
        chart.select_ia_exit_from_application_btn()
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        
        """
            STEP 10.01 : Verify 'Visual' is available under 'G490183' folder in content area as below
        """
        main_page.verify_items_in_grid_view(["Visual"], "asin", "STEP 10.01 : Verify 'Visual' is available under 'G490183' folder in content area as below")
        
        """
            STEP 11 : Double click on Visual' from content area
        """
        pd_design.run_page_designer_by_double_click("Visual")
        main_page_run.switch_to_frame()

        """
            STEP 11.01 : Verify 'Visual' runs from explorer widget page without any error as below
        """
        visual.verify_x_axis_title(["CAR"], msg="step 11.01")
        visual.verify_y_axis_title(["SALES"], msg="step 11.02")
        visual.verify_x_axis_label(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 11.03")
        visual.verify_y_axis_label(["0", "20K", "40K", "60K", "80K", "100K"], msg="step 11.04")
        visual.verify_number_of_risers("#MAINTABLE_wbody1 rect", 1, 10, msg="step 11.05")
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", "bar_blue", msg="step 11.06")
        
        """
            STEP 12 : Close visualization
        """
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()

        """
            STEP 13 : Right click on 'Visual' and select Edit
        """
        main_page.right_click_folder_item_and_select_menu("Visual", "Edit")
        core_utils.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1", "CAR")
        
        """
            STEP 13.01 : Verify visualization opens in a new tab with the live preview canvas as below
        """
        visual.verify_x_axis_title(["CAR"], msg="step 13.01")
        visual.verify_y_axis_title(["SALES"], msg="step 13.02")
        visual.verify_x_axis_label(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 13.03")
        visual.verify_y_axis_label(["0", "20K", "40K", "60K", "80K", "100K"], msg="step 13.04")
        visual.verify_number_of_risers("#MAINTABLE_wbody1 rect", 1, 10, msg="step 13.05")
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", "bar_blue", msg="step 13.06")

        """
            STEP 14 : Click IA application main menu and click on Exit
        """
        chart.select_ia_exit_from_application_btn()
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")

        """
            STEP 15 : Close the 'Explorer widget' page run window.
        """
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)

        """
            STEP 15.01 : Verify 'Visual' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        self.driver.refresh()
        utils.synchronize_with_visble_text("#files-box-area", "Visual", 30)
        
        main_page.verify_items_in_grid_view(["Visual"], "asin", "Step 15.01 : Verify 'Visual' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page")

        """
            STEP 16 : Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main() 