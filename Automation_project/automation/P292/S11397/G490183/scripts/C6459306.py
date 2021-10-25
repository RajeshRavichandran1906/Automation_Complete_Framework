'''
Created on Jun 26, 2019

@author: Aftab

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/6459306
TestCase Name : Create, Edit and Run chart
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.chart import Chart

class C6459306_TestClass(BaseTestCase):

    def test_C6459306(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        main_page_run = Run(self.driver)
        pd_design = Design(self.driver)
        chart_obj= Chart(self.driver)
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        querypane_css = "#queryBoxColumn"
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
        1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
         
        """
        2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
             
        """
        3 : Expand 'P292_S11397' domain -> 'G490183' folder
            Double click on 'Explorer Widget page'
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
         
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
         
        """
        4 : Click on chart action tile from under InfoAssist category;
        """
        main_page.select_action_bar_tab("InfoAssist")
        main_page.select_action_bar_tabs_option("Chart")      
         
        """
        5 : Select car.mas under ibisamp folder and Click open
        """
        core_utils.switch_to_new_window()
        utils.synchronize_until_element_is_visible("#paneIbfsExplorer_exTree",45)
        utils.select_masterfile_in_open_dialog('ibisamp', 'car')
        
        """
        6 : Double click on 'CAR' from Dimensions and 'SALES' from Measures.
        """
        chart_obj.double_click_on_datetree_item('CAR', 1)
        chart_obj.wait_for_visible_text(querypane_css,'CAR')
        chart_obj.double_click_on_datetree_item('SALES', 1)
        chart_obj.wait_for_visible_text(querypane_css,'SALES')
        
        """
        6.01 : Verify Live Preview appears as below
        """
        chart_obj.verify_x_axis_title_in_preview(["CAR"],'#pfjTableChart_1', msg="step 6.01")
        chart_obj.verify_y_axis_title_in_preview(["SALES"], '#pfjTableChart_1',msg="step 6.02")
        chart_obj.verify_x_axis_label_in_preview(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'],'#pfjTableChart_1', msg="step 6.03")
        chart_obj.verify_y_axis_label_in_preview(["0", "20K", "40K", "60K", "80K", "100K"],'#pfjTableChart_1', msg="step 6.04")
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 10, msg="step 6.05")
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "bar_blue",'#pfjTableChart_1', msg="step 6.06")
          
        """
        7 : Click Run.
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """
        7.01 : Verify chart runs without any error as below
        """
        chart_obj.verify_x_axis_title_in_run_window(["CAR"],'#jschart_HOLD_0', msg="step 7.01")
        chart_obj.verify_y_axis_title_in_run_window(["SALES"], '#jschart_HOLD_0',msg="step 7.02")
        chart_obj.verify_x_axis_label_in_run_window(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'],'#jschart_HOLD_0', msg="step 7.03")
        chart_obj.verify_y_axis_label_in_run_window(["0", "20K", "40K", "60K", "80K", "100K"],'#jschart_HOLD_0', msg="step 7.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 10, msg="step 7.05")
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "bar_blue",'#jschart_HOLD_0', msg="step 7.06")
        
        """
        8 : Click save;
            Enter title as 'Chart' and Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_item_in_top_toolbar('save')
        chart_obj.save_file_in_save_dialog('Chart')
         
        """
        9 : Close IA
        """
        chart_obj.select_visualization_application_menu_item('exit')
        
        """
        9.01 : Verify 'Chart' is available under 'G490183' folder in content area as below
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.verify_items_in_grid_view(["Chart"], 'asin', "Step 9.01: Verify")
        
        """
        10 : Double click on 'Chart' from content area
        """
        main_page.double_click_on_content_area_items('Chart')
                                               
        """
        10.01 Verify Chart runs from explorer widget page without any error as below
        """
        main_page_run.switch_to_frame()
        chart_obj.verify_x_axis_title_in_run_window(["CAR"],'#jschart_HOLD_0', msg="step 10.01")
        chart_obj.verify_y_axis_title_in_run_window(["SALES"], '#jschart_HOLD_0',msg="step 10.02")
        chart_obj.verify_x_axis_label_in_run_window(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'],'#jschart_HOLD_0', msg="step 10.03")
        chart_obj.verify_y_axis_label_in_run_window(["0", "20K", "40K", "60K", "80K", "100K"],'#jschart_HOLD_0', msg="step 10.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 10, msg="step 10.05")
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "bar_blue",'#jschart_HOLD_0', msg="step 10.06")
        
        """
        11 : Close chart
        """
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()
        
        """
        12 : Right click on 'chart' and select Edit
        """
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.right_click_folder_item_and_select_menu("Chart", 'Edit')
        core_utils.switch_to_new_window()
        chart_obj.wait_for_visible_text('#pfjTableChart_1', "BMW")
        
        """
        12.01 : Verify chart opens in a new tab with the live preview canvas as below
        """
        chart_obj.verify_x_axis_title_in_preview(["CAR"],'#pfjTableChart_1', msg="step 12.01")
        chart_obj.verify_y_axis_title_in_preview(["SALES"], '#pfjTableChart_1',msg="step 12.02")
        chart_obj.verify_x_axis_label_in_preview(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'],'#pfjTableChart_1', msg="step 12.03")
        chart_obj.verify_y_axis_label_in_preview(["0", "20K", "40K", "60K", "80K", "100K"],'#pfjTableChart_1', msg="step 12.04")
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 10, msg="step 12.05")
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "bar_blue",'#pfjTableChart_1', msg="step 12.06")
         
        """
        13 : Click IA application main menu and click on Exit
        """
        chart_obj.select_ia_exit_from_application_btn()
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
                 
        """
        14 : Close the 'Explorer widget' page run window.
        """
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
        14.01 : Verify 'Chart' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        self.driver.refresh()
        utils.synchronize_with_visble_text("#files-box-area", "Chart", 30)
        
        main_page.verify_items_in_grid_view(["Chart"], "asin", "Step 14.01 : Verify 'Chart' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page")
        
        """
        15 : Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main() 