"""-------------------------------------------------------------------------------------------
Created on June 27, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22062773
Test Case Title =  Create, Edit and Run Page
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Run as R
from common.wftools.chart import Chart

class C6459309_TestClass(BaseTestCase):

    def test_C6459309(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        pd_design_run = R(self.driver)
        main_page_run = Run(self.driver)
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
        explorer_css = "div.files-box-files"
        
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
            STEP 4 : Click on Page action tile from under Designer category;
            Choose Blank template
        """
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        chart.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
        
        pd_design.select_page_designer_template("Blank")
        chart.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 5 : From Container tab, Drag and drop panel container into the page canvas
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Panel", 1)
 
        """
            STEP  6 : From Content tab, Drag and drop 'Chart1' into the panel
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G490183")
        pd_design.drag_content_item_to_container("Chart1", "Panel 1", 1, content_folder_path="G490183")
        
        """
            STEP 06.01 : Verify chart is placed in the container as below
        """
        pd_design.switch_to_container_frame("Chart1")
        chart.verify_x_axis_label_in_run_window(['ALFA R...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASER...', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 06.01")
        chart.verify_x_axis_title_in_run_window(['CAR'], msg="step 06.02")
        chart.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K'], msg="step 06.03")
        chart.verify_y_axis_title_in_run_window(['SALES'], msg="step 06.04")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 10, msg="step 06.05")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar!", "bar_blue", "step 06.06 : Verify chart colour is blue")
        pd_design.switch_to_default_page()
        
        """
            STEP 7 : Click on preview button.
        """
        pd_design.click_preview()
        pd_design.switch_to_container_frame("Chart1")

        """
            STEP 07.01 : Verify that the chart runs inside the container in preview mode as below
        """
        chart.verify_x_axis_label_in_run_window(['ALFA R...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASER...', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 07.01")
        chart.verify_x_axis_title_in_run_window(['CAR'], msg="step 07.02")
        chart.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K'], msg="step 07.03")
        chart.verify_y_axis_title_in_run_window(['SALES'], msg="step 07.04")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 10, msg="step 07.05")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar!", "bar_blue", "step 07.06 : Verify chart colour is blue")
        pd_design.switch_to_default_page()
        
        """
            STEP 8 : Click on back button to get back to the design mode
        """
        pd_design_run.go_back_to_design_from_preview()

        """
            STEP 9 : Click on Application menu > Save > Enter title 'PGX' > Click Save.
        """
        pd_design.save_as_page_from_application_menu("PGX")

        """
            STEP 10 : Close Page Designer from application menu
        """
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")

        """
            STEP 10.01 : Verify that the 'PGX' is created and listed under 'G490183' folder
        """
        main_page.verify_items_in_grid_view(["PGX"], "asin", "STEP 10.01 : Verify that the 'PGX' is created and listed under 'G490183' folder")
        
        """
            STEP 11 : Double click on 'PGX'
        """
        pd_design.run_page_designer_by_double_click("PGX")
        main_page_run.switch_to_frame()

        """
            STEP 11.01 : Verify the page runs fine from inside explorer widget page as below
        """
        pd_design.switch_to_container_frame("Chart1")
        chart.verify_x_axis_label_in_run_window(['ALFA R...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASER...', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 11.01")
        chart.verify_x_axis_title_in_run_window(['CAR'], msg="step 11.02")
        chart.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K'], msg="step 11.03")
        chart.verify_y_axis_title_in_run_window(['SALES'], msg="step 11.04")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 10, msg="step 11.05")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar!", "bar_blue", "step 11.06 : Verify chart colour is blue")
        pd_design.switch_to_default_page()
        
        """
            STEP 12 : Close PGX page run window
        """
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()
        
        """
            STEP 13 : Right click on 'PGX' and select Edit
        """
        main_page.right_click_folder_item_and_select_menu("PGX", "Edit")
        core_utils.switch_to_new_window()
        
        """
            STEP 13.01 : Verify that the PGX designer page opens in a new tab as below
        """
        pd_design.switch_to_container_frame("Chart1")
        chart.verify_x_axis_label_in_run_window(['ALFA R...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASER...', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 13.01")
        chart.verify_x_axis_title_in_run_window(['CAR'], msg="step 13.02")
        chart.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K'], msg="step 13.03")
        chart.verify_y_axis_title_in_run_window(['SALES'], msg="step 13.04")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 10, msg="step 13.05")
        pd_design.switch_to_default_page()

        """
            STEP 14 : Close designer
        """
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")

        """
            STEP 15 : Click X button to close the 'Explorer widget' page run mode
        """
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)

        """
            STEP 15.01 : Verify PGX' page is listed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        self.driver.refresh()
        utils.synchronize_with_visble_text("#files-box-area", "PGX", 30)
        
        main_page.verify_items_in_grid_view(["PGX"], "asin", "Step 15.01 : Verify 'Visual' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page")
        
        """
            STEP 16 : Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  