'''
Created on Sep 21, 2018

@author: Magesh

Testcase Name : Verify to restore successful with Executive Dashboard
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419859
'''

import unittest
import time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C6419859_TestClass(BaseTestCase):

    def test_C6419859(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        folder_name="Retail_Samples/Visualizations"
        edit_fex_folder_after_save="SmokeTest/~rsadv"
        fex_name='Executive_Dashboard'
        save_fex_name='Executive_Dashboard1'
        expected_guage1_label_list1=["130.8M"]
        expected_guage1_label_list2=["Revenue"]
        expected_guage2_label_list1=["37.1M"]
        expected_guage2_label_list2=["Gross Profit"]
        expected_guage3_label_list1=["439K"]
        expected_guage3_label_list2=["Quantity Sold"]
        wait_time=90
        long_time=300
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        
        run_css1="#MAINTABLE_7 svg g rect[class^='riser']"
        app_btn_css="#applicationButtonBox"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Edit the Visualizations using the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Visualizations/Executive_Dashboard.fex&tool=idis
        """
        visible_text='439K'
        gauge_chart_label_css="#ar_TableChart_3 text[class^='Total']"
        visual_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_visible_text(gauge_chart_label_css, visible_text, time_out=long_time)
        time.sleep(20)#time sleep given asall of the charts are not getting diplayed sometimes.
        
        
        """
        Step 03: Verify the following Query pane,Filter pane and Chart on canvas
        """
        visual_obj.verify_field_listed_under_querytree('Gauge1', 'Gauge2', 1, msg="Step 03.a:")
        visual_obj.verify_field_listed_under_querytree('Gauge2', 'Gauge3', 1, msg="Step 03.b:")
        visual_obj.verify_field_listed_under_querytree('Measure', 'Quantity,Sold', 1, msg="Step 03.c:")
        visual_obj.verify_field_listed_under_querytree('Line1', 'Line2', 1, msg="Step 03.d:")
        visual_obj.verify_field_listed_under_querytree('Line2', 'Line3', 1, msg="Step 03.e:")
        visual_obj.verify_field_listed_under_querytree('Line3', 'Bar Stacked1', 1, msg="Step 03.f:")
        visual_obj.verify_field_listed_under_querytree('Bar Stacked1', 'Bar Stacked2', 1, msg="Step 03.g:")
        visual_obj.verify_field_listed_under_querytree('Bar Stacked2', 'Bar Stacked3', 1, msg="Step 03.h:")
        visual_obj.verify_field_in_filterbox('Sale,Year', 1, msg="Step 03.i:")
        visual_obj.verify_field_in_filterbox('Store Type', 2, msg="Step 03.j:")
        
        "---1. guage chart1---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_1 path[class^='riser!s0!g0!mrange!']", expected_number=1, time_out=long_time)
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#ar_TableChart_1 svg > g', label_css="text[class^='Total']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#ar_TableChart_1', label_css="[class^='title'] span", msg="Step 03:2")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_1', 1, 1, msg="Step 03:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#ar_TableChart_1', msg="Step 03:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_2 path[class^='riser!s0!g0!mrange!']", expected_number=1, time_out=long_time)
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#ar_TableChart_2 svg > g', label_css="text[class^='Total']", msg="Step 03:05:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#ar_TableChart_2', label_css="[class^='title'] span", msg="Step 03:6")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_2', 1, 1, msg="Step 03:07:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#ar_TableChart_2', msg="Step 03:08:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_3 path[class^='riser!s0!g0!mrange!']", expected_number=1, time_out=long_time)
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#ar_TableChart_3 svg > g', label_css="text[class^='Total']", msg="Step 03:09:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#ar_TableChart_3', label_css="[class^='title'] span", msg="Step 03:10")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_3', 1, 1, msg="Step 03:11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#ar_TableChart_3', msg="Step 03:12:Verify chart color")
        
        "---4. Line chart1---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_4 path[class^='riser!s0!g0!mline!']", expected_number=1, time_out=long_time)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_4', msg="Step 03:13:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_4', msg="Step 03:14:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_4', msg="Step 03:15:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_4', msg="Step 03:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#ar_TableChart_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_4 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_4', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_4", msg="Step 03:20: Verify legends")
        
        "---5. Line chart2---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_5 path[class^='riser!s0!g0!mline!']", expected_number=1, time_out=long_time)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_5', msg="Step 03:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_5', msg="Step 03:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_5', msg="Step 03:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_5', msg="Step 03:24:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#ar_TableChart_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:25:Verify line chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:26:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_5', attribute='stroke', msg="Step 03:27:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_5", msg="Step 03:28: Verify legends")
        
        "---6. Line chart3---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_6 path[class^='riser!s0!g0!mline!']", expected_number=1, time_out=long_time)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_6', msg="Step 03:29:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_6', msg="Step 03:30:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_6', msg="Step 03:31:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_6', msg="Step 03:32:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#ar_TableChart_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:33:Verify line chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_6 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:34:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_6', attribute='stroke', msg="Step 03:35:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_6", msg="Step 03:36: Verify legends")
        
        "---7. Bar chart1---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_7 rect[class^='riser!']", expected_number=29, time_out=long_time)
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_7', msg="Step 03:37:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_7', msg="Step 03:38:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Store Name']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_7', msg="Step 03:39:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_7', msg="Step 03:40:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Revenue by Store']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:41:Verify bar chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_7 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 29, msg="Step 03:42:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#ar_TableChart_7', msg="Step 03:43:Verify chart color")
        
        "---8. Bar chart2---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_8 rect[class^='riser!']", expected_number=7, time_out=long_time)
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_8', msg="Step 03:44:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_8', msg="Step 03:45:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_8', msg="Step 03:46:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_8', msg="Step 03:47:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit by Product Category']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:48:Verify bar chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_8 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 03:49:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#ar_TableChart_8', msg="Step 03:50:Verify chart color")
        
        "---9. Bar chart3---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_9 rect[class^='riser!']", expected_number=3, time_out=long_time)
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_9', msg="Step 03:51:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_9', msg="Step 03:52:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Business Region']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_9', msg="Step 03:53:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_9', msg="Step 03:54:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Region']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:55:Verify bar chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_9 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 03:56:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#ar_TableChart_9', msg="Step 03:57:Verify chart color")
        
        """
        Step 04: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
        time.sleep(2*Global_variables.longwait)
        
        """
        Verify the output is displayed in new window
        """
        visual_obj.wait_for_number_of_element(run_css1, expected_number=29, time_out=long_time)
        
        "---1. guage chart1---"
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='Total']", msg="Step 04:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 04:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 1, msg="Step 04:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 04:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#MAINTABLE_2 svg > g', label_css="text[class^='Total']", msg="Step 04.5:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#MAINTABLE_2', label_css="[class^='title'] span", msg="Step 04.6")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_2', 1, 1, msg="Step 04.7:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 04.8:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#MAINTABLE_3 svg > g', label_css="text[class^='Total']", msg="Step 04.9:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#MAINTABLE_3', label_css="[class^='title'] span", msg="Step 04.10")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_3', 1, 1, msg="Step 04.11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_3', msg="Step 04.12:Verify chart color")
        
        "---4. Line chart1---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 04.13:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 04.14:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 04.15:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 04:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 04:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_4 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 04:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 04:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 04:20: Verify legends")
        
        "---5. Line chart2---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 04.21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 04.22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 04.23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 04.24:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 04.25:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 04.26:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 04.27:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 04.28: Verify legends")
        
        "---6. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 04.29:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 04.30:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 04.31:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 04.32:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 04.33:Verify line chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_6 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 04.34:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 04.35:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 04.36: Verify legends")
        
        "---7. Bar chart1---"
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 04.37:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_7', msg="Step 04.38:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Store Name']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 04.39:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 04.40:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Revenue by Store']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 04.41:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_7 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 29, msg="Step 04.42:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 04.43:Verify chart color")
        
        "---8. Bar chart2---"
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_8', msg="Step 04.44:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 04.45:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 04.46:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 04.47:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit by Product Category']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 04.48:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 04.49:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 04.50:Verify chart color")
        
        "---9. Bar chart3---"
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 04.51:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_9', msg="Step 04.52:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Business Region']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 04.53:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 04.54:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Region']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 04.55:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 04.56:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 04.57:Verify chart color")
        
        """
        Step 05: Close the output window
        """
        visual_obj.switch_to_previous_window()
        time.sleep(Global_variables.longwait)
        visual_obj.wait_for_number_of_element(app_btn_css, expected_number=1, time_out=wait_time)
        
        """
        Step 06: Click IA > Save > Select "SmokeTest" folder > Enter title as "Executive Dashboard1" > Click Save
        """
        visual_obj.save_as_from_application_menu_item(save_fex_name)
        
        """
        Step 07: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual_obj.logout_visualization_using_api()
        
        """
        Step 08: Edit the saved Visualization using "rsadv" user with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Executive_Dashboard1.fex&tool=Document
        """
        visual_obj.edit_fex_using_api_url(edit_fex_folder_after_save, fex_name=save_fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_visible_text(gauge_chart_label_css, visible_text, time_out=long_time)
        
        """
        Verify Restore successful
        """
        "---1. guage chart1---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_1 path[class^='riser!s0!g0!mrange!']", expected_number=1, time_out=long_time)
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#ar_TableChart_1 svg > g', label_css="text[class^='Total']", msg="Step 08:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#ar_TableChart_1', label_css="[class^='title'] span", msg="Step 08:2")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_1', 1, 1, msg="Step 08:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#ar_TableChart_1', msg="Step 08:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_2 path[class^='riser!s0!g0!mrange!']", expected_number=1, time_out=long_time)
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#ar_TableChart_2 svg > g', label_css="text[class^='Total']", msg="Step 08:05:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#ar_TableChart_2', label_css="[class^='title'] span", msg="Step 08:6")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_2', 1, 1, msg="Step 08:07:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#ar_TableChart_2', msg="Step 08:08:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_3 path[class^='riser!s0!g0!mrange!']", expected_number=1, time_out=long_time)
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#ar_TableChart_3 svg > g', label_css="text[class^='Total']", msg="Step 08:09:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#ar_TableChart_3', label_css="[class^='title'] span", msg="Step 08:10")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_3', 1, 1, msg="Step 08:11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#ar_TableChart_3', msg="Step 08:12:Verify chart color")
        
        "---4. Line chart1---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_4 path[class^='riser!s0!g0!mline!']", expected_number=1, time_out=long_time)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_4', msg="Step 08:13:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_4', msg="Step 08:14:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_4', msg="Step 08:15:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_4', msg="Step 08:16:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#ar_TableChart_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:17:Verify line chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_4 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 08:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_4', attribute='stroke', msg="Step 08:19:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_4", msg="Step 08:20: Verify legends")
        
        "---5. Line chart2---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_5 path[class^='riser!s0!g0!mline!']", expected_number=1, time_out=long_time)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_5', msg="Step 08:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_5', msg="Step 08:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_5', msg="Step 08:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_5', msg="Step 08:24:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#ar_TableChart_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:25:Verify line chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_5 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 08:26:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_5', attribute='stroke', msg="Step 08:27:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_5", msg="Step 08:28: Verify legends")
        
        "---6. Line chart3---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_6 path[class^='riser!s0!g0!mline!']", expected_number=1, time_out=long_time)
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_6', msg="Step 08:29:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_6', msg="Step 08:30:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_6', msg="Step 08:31:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_6', msg="Step 08:32:Verify y_axis title at runtime")
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#ar_TableChart_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:33:Verify line chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_6 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 08:34:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_6', attribute='stroke', msg="Step 08:35:Verify chart color")
        expected_legends=['Sale Year', '2014', '2015']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_6", msg="Step 08:36: Verify legends")
        
        "---7. Bar chart1---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_7 rect[class^='riser!']", expected_number=29, time_out=long_time)
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_7', msg="Step 08:37:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_7', msg="Step 08:38:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Store Name']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_7', msg="Step 08:39:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_7', msg="Step 08:40:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Revenue by Store']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:41:Verify bar chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_7 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 29, msg="Step 08:42:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#ar_TableChart_7', msg="Step 08:43:Verify chart color")
        
        "---8. Bar chart2---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_8 rect[class^='riser!']", expected_number=7, time_out=long_time)
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_8', msg="Step 08:44:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_8', msg="Step 08:45:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Product Category']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_8', msg="Step 08:46:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_8', msg="Step 08:47:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Gross Profit by Product Category']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:48:Verify bar chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_8 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 08:49:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#ar_TableChart_8', msg="Step 08:50:Verify chart color")
        
        "---9. Bar chart3---"
        visual_obj.wait_for_number_of_element("#ar_TableChart_9 rect[class^='riser!']", expected_number=3, time_out=long_time)
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_9', msg="Step 08:51:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_9', msg="Step 08:52:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Business Region']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_9', msg="Step 08:53:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_9', msg="Step 08:54:Verify y_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Region']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:55:Verify bar chart title at runtime")
        parent_css_with_tag_name="#ar_TableChart_9 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 08:56:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#ar_TableChart_9', msg="Step 08:57:Verify chart color")
        
        """
        Step 09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()