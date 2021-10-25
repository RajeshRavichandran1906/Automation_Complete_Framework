'''
Created on Sep 21, 2018

@author: Magesh

Testcase Name : Verify to Interact with the Executive Dashboard - Line charts
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275872
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.lib import utillity

class C2275872_TestClass(BaseTestCase):

    def test_C2275872(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C2275872"
        fex_name='Executive_Dashboard'
        expected_guage1_label_list1=["130.8M"]
        expected_guage1_label_list2=["Revenue"]
        expected_guage2_label_list1=["37.1M"]
        expected_guage2_label_list2=["Gross Profit"]
        expected_guage3_label_list1=["439K"]
        expected_guage3_label_list2=["Quantity Sold"]
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        element_css1="#MAINTABLE_7 svg>g rect[class^='riser']"
        element_css2="#MAINTABLE_9 svg>g rect[class^='riser']"
        element_css3="#MAINTABLE_4 path[class^='riser']"
        element_css4="#MAINTABLE_5 path[class^='riser']"
        table_css1='#MAINTABLE_wbody10 .arPivot table > tbody > tr'
        table_css2='#MAINTABLE_wbody11 .arPivot table > tbody > tr'
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Visualizations&BIP_item=Executive_Dashboard.fex
        """
        visual_obj.run_visualization_using_api(fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(element_css1, expected_number=29, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css2, expected_number=3, time_out=wait_time)
        
        """
        Step 03: Verify the following Charts are displayed
        """
        "---1. guage chart1---"
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='Total']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 03:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 1, msg="Step 03:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 03:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#MAINTABLE_2 svg > g', label_css="text[class^='Total']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#MAINTABLE_2', label_css="[class^='title'] span", msg="Step 03:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_2', 1, 1, msg="Step 03:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 03:04:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#MAINTABLE_3 svg > g', label_css="text[class^='Total']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#MAINTABLE_3', label_css="[class^='title'] span", msg="Step 03:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_3', 1, 1, msg="Step 03:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_3', msg="Step 03:04:Verify chart color")
        
        "---4. Line chart1---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_4 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 03:20: Verify legends")
        
        "---5. Line chart2---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 03:20: Verify legends")
        
        "---6. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 03:20: Verify legends")
        
        "---7. Bar chart1---"
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 03:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_7', msg="Step 03:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Store Name']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 03:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 03:16:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Revenue by Store']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:24:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_7 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 42, msg="Step 03:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 03:26:Verify chart color")
        
        "---8. Bar chart2---"
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_8', msg="Step 03:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 03:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 03:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 03:16:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit by Product Category']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:24:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 03:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 03:26:Verify chart color")
        
        "---9. Bar chart3---"
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 03:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_9', msg="Step 03:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Business Region']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 03:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 03:16:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Region']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:24:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 03:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 03:26:Verify chart color")
        
        """
        Step 04: Go to "Quantity Sold (TY vs LY) by Month"
        Hover over on point 6 and click exclude from chart
        """
        riser_css='marker!s1!g5!mmarker!'
        parent_css='MAINTABLE_4'
        menu_path='Exclude from Chart'
        visual_obj.select_tooltip(riser_css, menu_path, parent_css, use_marker_enable=True, move_to_tooltip=True)
        
        """
        Step 05: Verify the Result
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=3, time_out=wait_time)
        time.sleep(Global_variables.mediumwait)
        
        "---1. Line chart1---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_4 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 03:20: Verify legends")
        
        "---2. Line chart2---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 03:20: Verify legends")
        
        "---3. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 03:20: Verify legends")
        
        """
        Step 06: Click "Run menu icon" at the bottom and Click "Show data"
        """
        parent_css="#MAINTABLE_menuContainer4"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css)
        
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds01.xlsx'
        visual_obj.create_visualization_tabular_report(file_name, table_css1)
        visual_obj.verify_visualization_tabular_report(file_name, table_css1, msg='Step 06.1:')
        
        """
        Step 07: Click "Show data" again to return back to Chart and click Run menu to dismiss
        """
        parent_css="#MAINTABLE_menuContainer4"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer4", toggle_button_click='yes')
        
        
        """
        Step 08: Go to "Gross Profit (TY vs LY) by Month".
        Hover over on point 9 click "Drill up to Sale Quarter"
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=3, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css4, expected_number=3, time_out=wait_time)
        riser_css='marker!s1!g8!mmarker!'
        parent_css='MAINTABLE_wbody5'
        menu_path='Drill up to Sale Quarter'
        visual_obj.select_tooltip(riser_css, menu_path, parent_css, use_marker_enable=True, move_to_tooltip=True)
        
        """
        Step 09: Verify the Result
        """
        visual_obj.wait_for_number_of_element(element_css4, expected_number=2, time_out=wait_time)
        expected_x_axis_labels=['1', '2', '3', '4']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Quarter']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 03:20: Verify legends")
        
        """
        Step 10: Click "Run menu icon" at the bottom and Click "Show data"
        """
        parent_css="#MAINTABLE_menuContainer5"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css)
        
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds02.xlsx'
        visual_obj.create_visualization_tabular_report(file_name, table_css2)
        visual_obj.verify_visualization_tabular_report(file_name, table_css2, msg='Step 10.1:')
        
        """
        Step 11: Click "Show data" again to return back to Chart and click Run menu to dismiss
        """
        parent_css="#MAINTABLE_menuContainer5"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer5", toggle_button_click='yes')
        
        
        """
        Step 19: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        