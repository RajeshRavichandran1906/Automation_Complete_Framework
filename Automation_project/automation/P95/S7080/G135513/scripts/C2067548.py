'''
Created on January 11, 2019
@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2067548
TestCase Name = Active Dashboard has several Filtering problems using a CheckBox (ACT-432)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.wftools.chart import Chart
from common.wftools import document
from common.wftools import visualization
import time
import pyautogui

class C2067548_TestClass(BaseTestCase):

    def test_C2067548(self):
        
        """
        TESTCASE Object's
        """
        visual_obj = visualization.Visualization(self.driver)
        document_obj = document.Document(self.driver)
        chart_obj = Chart(self.driver)
        active_chart_obj = Active_Chart(self.driver)
        active_report_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        util_obj = UtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        PARENT_CSS = "#MAINTABLE_wbody1_f"
        page_load_css= PARENT_CSS + " text[class*='xaxisOrdinal-labels!g2!mgroupLabel']"
        coffee_css = "rect[class='riser!s0!g0!mbar!']"
        
        """
        Test case variables
        """
        test_case_id = 'C2067548'
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        """
        Step 1: Run the existing fex using the below API link
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P95/S7063/&BIP_item=act-432.fex
        Expect to see the following Dashboard with an Active Report, a Check Box Filter, a Bar Chart and PIE Chart. 
        Each object should contain data for three Categories, Coffee, Food and Gifts.
        """
        active_report_obj.run_active_report_using_api('act-432.fex', column_css=page_load_css, synchronize_visible_element_text='Gifts', repository_path=folder_path)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 1')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 1.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 1.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Food','Gifts'], parent_css=PARENT_CSS, msg='Step 1.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 1.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css=PARENT_CSS, msg='Step 1.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 1.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 1.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.create_active_report_dataset(test_case_id + '_step_1.xlsx')
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_1.xlsx', 'Step 1.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 1.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 6, msg="Step 1.10")
        active_chart_obj.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css="#MAINTABLE_wbody2", legend_length=3, msg="Step:1.11")
        active_chart_obj.verify_x_axis_label_in_run_window(['37%', '38%', '25%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 1.12")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 1.13', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step:1.14", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 1.15')
        document_obj.verify_prompts('check_box', '#checkboxPROMPT_1', ['[All]', 'Coffee', 'Food', 'Gifts'], 'Step 1.16: Verify the checkbox')
        
        """
        Step 2: In the Check Box, select Coffee.
        Expect to see the following Dashboard, with Coffee the only Category displayed on all three Objects.
        """
        document_obj.select_prompt('check_box', '#checkboxPROMPT_1', ['Coffee'])
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 2, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 2')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 2.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 2.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee'], parent_css=PARENT_CSS, msg='Step 2.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 2.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 2, parent_css=PARENT_CSS, msg='Step 2.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 2.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 2.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_2.xlsx', 'Step 2.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 2.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 2, msg="Step 2.10")
        active_chart_obj.verify_x_axis_label_in_run_window(['100%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 2.11")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 2.12', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 2.13", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 2.14')
        
        """
        Step 3: In the Check Box, select Gifts.
        Expect to see the following Dashboard, with Coffee and Gifts the two Categories displayed on all three Objects.
        """
        document_obj.select_prompt('check_box', '#checkboxPROMPT_1', ['Gifts'])
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 3, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 3')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 3.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 3.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Gifts'], parent_css=PARENT_CSS, msg='Step 3.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.3M', '0.6M', '0.9M', '1.2M','1.5M'], parent_css=PARENT_CSS, msg='Step 3.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 4, parent_css=PARENT_CSS, msg='Step 3.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 3.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 3.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_3.xlsx', 'Step 3.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 3.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 4, msg="Step 3.10")
        active_chart_obj.verify_x_axis_label_in_run_window(['60%', '40%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 3.11")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 3.12', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 3.13", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 3.14')
        
        """
        Step 4: On the Bar Chart, left-click and Exclude the first Bar, for Coffee.
        Expect to see the following Dashboard, with Gifts the only Category displayed on all three Objects.
        Also expect to see the Check Box unchanged, still showing Coffee and Gifts checked.
        Expect to see the Filter icon appear at the top of the Bar Chart.
        """
        source_element = util_obj.validate_and_get_webdriver_object(coffee_css, 'coffee-css')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-15, source_yoffset=-19, target_xoffset=19, target_yoffset=19)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 2, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 4')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 4.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 4.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Gifts'], parent_css=PARENT_CSS, msg='Step 4.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.2M', '0.4M', '0.6M', '0.8M', '1M', '1.2M'], parent_css=PARENT_CSS, msg='Step 4.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 2, parent_css=PARENT_CSS, msg='Step 4.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 4.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 4.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_4.xlsx', 'Step 4.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 4.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 2, msg="Step 4.10")
        active_chart_obj.verify_x_axis_label_in_run_window(['100%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 4.11")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 4.12', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 4.13", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 4.14')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['Coffee', 'Gifts'], 'Step 4.15: Verify the selected checkbox')
        util_obj.verify_object_visible("#MAINTABLE_wmenu1 div[title=\"Remove Filter\"] img", True, 'Step 4.16: Verify the filter')
        
        """
        Step 5: Click the Filter icon at the top of the Bar Chart.
        Expect to see the following Dashboard, with Gifts and Coffee the two Categories displayed on all three Objects.
        Also expect to see the Filter icon removed from the Bar Chart.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_1', 8)
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 3, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 5')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 5.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 5.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Gifts'], parent_css=PARENT_CSS, msg='Step 5.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.3M', '0.6M', '0.9M', '1.2M','1.5M'], parent_css=PARENT_CSS, msg='Step 5.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 4, parent_css=PARENT_CSS, msg='Step 5.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 5.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 5.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_3.xlsx', 'Step 5.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 5.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 4, msg="Step 5.10")
        active_chart_obj.verify_x_axis_label_in_run_window(['60%', '40%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 5.11")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 5.12', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 5.13", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 5.14')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['Coffee', 'Gifts'], 'Step 5.15: Verify the selected checkbox')
        util_obj.verify_object_visible("#MAINTABLE_wmenu1 div[title=\"Remove Filter\"] img", False, 'Step 5.16: Verify the filter not present')
        
        """
        Step 6: In the Check Box, select All.
        Expect to see the original Dashboard with an Active Report, a Check Box Filter, a Bar Chart and PIE Chart. 
        Each object should contain data for three Categories, Coffee, Food and Gifts.
        """
        document_obj.select_prompt('check_box', '#checkboxPROMPT_1', ['[All]'])
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 4, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 6')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 6.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 6.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Food','Gifts'], parent_css=PARENT_CSS, msg='Step 6.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 6.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css=PARENT_CSS, msg='Step 6.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 6.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 6.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_1.xlsx', 'Step 6.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 6.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 6, msg="Step 6.10")
        active_chart_obj.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css="#MAINTABLE_wbody2", legend_length=3, msg="Step 6.11")
        active_chart_obj.verify_x_axis_label_in_run_window(['37%', '38%', '25%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 6.12")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 6.13', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 6.14", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 6.15')
        document_obj.verify_prompts('check_box', '#checkboxPROMPT_1', ['[All]', 'Coffee', 'Food', 'Gifts'], 'Step 6.16: Verify the checkbox')
        
        """
        Step 7: On the PIE chart, left-click and Exclude the slice for Food.
        Expect to see the following Dashboard, with Coffee and Gifts the two Categories displayed on all three Objects.
        Also expect to see the Check Box unchanged, showing All.
        Expect to see the Filter icon appear at the top of the PIE Chart.
        """
        source_element = util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody2 path[class='riser!s1!g0!mwedge!']", 'foods-css')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-20, target_xoffset=-5, target_yoffset=5)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 3, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 7')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 7.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 7.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Gifts'], parent_css=PARENT_CSS, msg='Step 7.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M'], parent_css=PARENT_CSS, msg='Step 7.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 4, parent_css=PARENT_CSS, msg='Step 7.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 7.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 7.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_7.xlsx', 'Step 7.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 7.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 4, msg="Step 7.10")
        active_chart_obj.verify_legends_in_run_window(['Coffee', 'Gifts'], parent_css="#MAINTABLE_wbody2", legend_length=3, msg="Step 7.11")
        active_chart_obj.verify_x_axis_label_in_run_window(['60%', '40%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 7.12")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 7.13', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 7.14", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 7.15')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['[All]'], 'Step 7.16: Verify the selected checkbox')
        util_obj.verify_object_visible("#MAINTABLE_wmenu1 div[title=\"Remove Filter\"] img", True, 'Step 7.17: Verify the filter')
        
        """
        Step 8: On the Bar Chart, left-click and Exclude Gifts.
        Expect to see the following Dashboard, with Coffee the only Category displayed on all three Objects.
        Also expect to see Filter icons at the top of both the Bar and PIE charts.
        """
        source_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g1!mbar!']", 'gifts-css')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-20, target_xoffset=-5, target_yoffset=5)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 2, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 8')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 8.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 8.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee'], parent_css=PARENT_CSS, msg='Step 8.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 8.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 2, parent_css=PARENT_CSS, msg='Step 8.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 8.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 8.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_8.xlsx', 'Step 8.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 8.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 2, msg="Step 8.10")
        active_chart_obj.verify_x_axis_label_in_run_window(['100%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 8.11")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 8.12', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 8.13", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 8.14')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['[All]'], 'Step 8.15: Verify the selected checkbox')
        util_obj.verify_object_visible("#MAINTABLE_wmenu1 div[title=\"Remove Filter\"] img", True, 'Step 8.16: Verify the filter on bar')
        util_obj.verify_object_visible("#MAINTABLE_wmenu2 div[title=\"Remove Filter\"] img", True, 'Step 8.17: Verify the filter on pie')
        
        """
        Step 9: Click the Filter icon at the top of the PIE Chart.
        Expect to see the following Dashboard, with Gifts and Coffee the two Categories displayed on all three Objects.
        Also expect to see the Filter icon removed from the PIE chart.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_2', 8)
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 4, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 9')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 9.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 9.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Food','Gifts'], parent_css=PARENT_CSS, msg='Step 9.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 9.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css=PARENT_CSS, msg='Step 9.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 9.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 9.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_1.xlsx', 'Step 9.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 9.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 6, msg="Step 9.10")
        active_chart_obj.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css="#MAINTABLE_wbody2", legend_length=3, msg="Step 9.11")
        active_chart_obj.verify_x_axis_label_in_run_window(['37%', '38%', '25%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 9.12")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 9.13', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 9.14", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 9.15')
        document_obj.verify_prompts('check_box', '#checkboxPROMPT_1', ['[All]', 'Coffee', 'Food', 'Gifts'], 'Step 9.16: Verify the checkbox')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['[All]'], 'Step 9.17: Verify the selected checkbox')
        
        """
        Step 10: From the drop down for Category on the report, select Filter/Equals.
        Select the value Food.
        Expect to see only the report change, showing just Food rows.
        """
        active_report_obj.select_menu_items('ITableData0', 0, 'Filter', 'Equals')
        util_obj.synchronize_with_number_of_element('#wall1 .arFilter', 1 , chart_obj.report_short_timesleep)
        active_report_obj.create_filter(1, 'Equals', value1="Food")
        active_report_obj.filter_button_click('Filter')
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 4, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 10')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 10.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 10.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Food','Gifts'], parent_css=PARENT_CSS, msg='Step 10.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 10.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css=PARENT_CSS, msg='Step 10.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 10.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 10.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_10.xlsx', 'Step 10.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 10.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 6, msg="Step 10.10")
        active_chart_obj.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css="#MAINTABLE_wbody2", legend_length=3, msg="Step 10.11")
        active_chart_obj.verify_x_axis_label_in_run_window(['37%', '38%', '25%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 10.12")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 10.13', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 10.14", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 10.15')
        document_obj.verify_prompts('check_box', '#checkboxPROMPT_1', ['[All]', 'Coffee', 'Food', 'Gifts'], 'Step 10.16: Verify the checkbox')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['[All]'], 'Step 10.17: Verify the selected checkbox')
        
        """
        Step 11: From the drop down for Category on the report, 
        select Restore Original.
        Expect to see the original Dashboard with an Active Report, a Check Box Filter, a Bar Chart and PIE Chart. 
        Each object should contain data for three Categories, Coffee, Food and Gifts.
        """
        source_element = util_obj.validate_and_get_webdriver_object('#wall1 .arWindowBarTitle', 'filter-panel-css')
        sourcevalue = core_util_obj.get_web_element_coordinate(source_element)
        pyautogui.mouseDown(sourcevalue['x'], sourcevalue['y'], duration=1)
        pyautogui.moveTo(x=1000, y=33, duration=1)
        pyautogui.mouseUp(duration=1)
        
        active_report_obj.select_menu_items('ITableData0', 0, 'Restore Original')
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody1 text[class^='xaxis']", 4, chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(['Category'], parent_css=PARENT_CSS, msg='Step 11')
        active_chart_obj.verify_y_axis_title_in_run_window(['Unit Sales'], parent_css=PARENT_CSS,msg='Step 11.1')
        active_chart_obj.verify_chart_title('Unit Sales by Category', msg='Step 11.2', parent_css='#MAINTABLE_wbody1_ft')
        active_chart_obj.verify_x_axis_label_in_run_window(['Coffee','Food','Gifts'], parent_css=PARENT_CSS, msg='Step 11.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.4M', '0.8M', '1.2M', '1.6M'], parent_css=PARENT_CSS, msg='Step 11.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css=PARENT_CSS, msg='Step 11.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(coffee_css, 'cerulean_blue', parent_css=PARENT_CSS,  msg='Step 11.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], 'Step 11.7', parent_css="#MAINTABLE_wmenu1")
        active_report_obj.verify_active_report_dataset(test_case_id + '_step_1.xlsx', 'Step 11.8', table_css='#ITableData0')
        active_chart_obj.verify_pie_label_in_single_group_in_run_window(['Unit Sales'], parent_css='#MAINTABLE_wbody2', msg="Step 11.9")
        active_chart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody2', 1, 6, msg="Step 11.10")
        active_chart_obj.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css="#MAINTABLE_wbody2", legend_length=3, msg="Step 11.11")
        active_chart_obj.verify_x_axis_label_in_run_window(['37%', '38%', '25%'], parent_css="#MAINTABLE_wbody2", xyz_axis_label_css="[class*='dataLabels!']",msg="step 11.12")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 11.13', parent_css='#MAINTABLE_wmenu2')
        active_chart_obj.verify_chart_title('Unit Sales by Category',msg="Step 11.14", parent_css="#MAINTABLE_wbody2")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css="#MAINTABLE_wbody2",  msg='Step 11.15')
        document_obj.verify_prompts('check_box', '#checkboxPROMPT_1', ['[All]', 'Coffee', 'Food', 'Gifts'], 'Step 11.16: Verify the checkbox')
        document_obj.verify_selected_value_in_active_dashboard_prompts('check_box', '#checkboxPROMPT_1', ['[All]'], 'Step 11.17: Verify the selected checkbox')
        
        """
        Step 12: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()