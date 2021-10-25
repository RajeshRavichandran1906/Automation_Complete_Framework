'''
Created on Sep 17, 2018

@author: Magesh

Testcase Name : Verify to Interact with Analytical Dashboard - Pie Chart
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419852
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C6419852_TestClass(BaseTestCase):

    def test_C6419852(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419852"
        fex_name='Analytical_Dashboard'
        expected_label_list1=["1.1B"]
        expected_label_list2=["Revenue"]
        expected_label_list3=["Sales by Product Category"]
        expected_label_list4=["78.4M"]
        expected_label_list5=["75.0M"]
        parent_css='MAINTABLE_wbody1'
        riser_css1='riser!s5!g0!mwedge!'
        menu_path1='Drill down to Product Subcategory'
        riser_css2='riser!s1!g0!mwedge!'
        menu_path2='Filter Chart'
        menu_option_button_name_show='show_report_css'
        menu_option_button_name_reset='reset'
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        element_css1="#MAINTABLE_wbody1 path[class^='riser']"
        element_css2="#MAINTABLE_wbody2  svg g circle[class^='riser']"
        element_css3="#MAINTABLE_wbody1 path[class^='riser']"
        element_css4="#MAINTABLE_wbody2  svg g circle[class^='riser']"
        table_css='#MAINTABLE_wbody5 .arPivot table > tbody > tr'
        parentmenuContainer_css="#MAINTABLE_menuContainer1"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Visualizations&BIP_item=Analytical_Dashboard.fex
        """
        visual_obj.run_visualization_using_api(fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(element_css1, expected_number=7, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css2, expected_number=157, time_out=wait_time)
         
        """
        Step 03: Verify the following output
        """
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, label_css="text[class^='totalLabel']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 03:02:Verify pie label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 03:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 03:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 03:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 03:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 03:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 03:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 03:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 03:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 03:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 03:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 03:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 03:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 03:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 03:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 03:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_wbody4_f', msg="Step 03:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 03:27: Verify legends")
        
        """
        Step 04: Go to "Sales by product Category" 
        Step 05: Hover over on any slices where "Product Category: Televisions".
        Step 06: Click "Drill down to Product Subcategory"
        """
        visual_obj.select_tooltip(riser_css1, menu_path1, parent_css, element_location='middle', move_to_tooltip=True)
        
        """
        Step 07: Verify the following output is displayed
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=3, time_out=wait_time)
        visual_obj.verify_pie_label_in_single_group(expected_label_list4, label_css="text[class^='totalLabel']", msg="Step 07:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 07:02:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 07:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 3, msg="Step 07:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 07:05:Verify chart color")
        expected_legends=['Product Subcategory', 'CRT TV', 'Flat Panel TV', 'Portable TV']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 07:06: Verify legends")
        
        """
        Step 08: Click "Run menu icon" at the bottom and Click "Show data"
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_show, parentmenuContainer_css)
        
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds01.xlsx'
#         visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 08.1:')
        
        """
        Step 09: Click "Show data" again to return back to Chart and Click Run menu to dismiss
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_show, parentmenuContainer_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer1", toggle_button_click='yes')
        
        """
        Step 10: Hover over on any slices where "Flat panel TV" > Click Filter Chart
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=3, time_out=wait_time)
        visual_obj.select_tooltip(riser_css2, menu_path2, parent_css, element_location='middle_left', xoffset=10, move_to_tooltip=True)
        
        """
        Step 11: Verify the following output is displayed
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=1, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css4, expected_number=7, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list5, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='totalLabel']", msg="Step 11:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='pieLabel!g']", msg="Step 11.2:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 11.3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 1, msg="Step 11.4:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 11.5:Verify chart color")
        expected_legends=['Product Subcategory', 'Flat Panel TV']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 11.6: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 11.7:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 11.8:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 11.9:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 11.10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 8, msg="Step 11.11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 11.12:Verify chart color")
        expected_legends=['Gross Profit', '3.4M', '1.3M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 11.13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 11.14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 11.15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 11.16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 11.17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 11.18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 11.19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 11.20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['Sony KDL32EX400', 'LG 19LE5300 19', 'LG 32LE5300 32', 'Panasonic TCP46G25', 'Sony KDL46HX800', 'Panasonic 58TV25BNDL', 'Sony KDL60EX500']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 11.21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 11.22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 11.23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 11.24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 11.25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g4!mbar!']", 'elf_green', parent_css='#MAINTABLE_wbody4_f', msg="Step 11.26:Verify chart color")
        expected_legends=['Revenue', '6.7M', '8.7M', '10.8M', '12.8M', '14.9M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 11.27: Verify legends")
        
        """
        Step 12: Click Run menu icon > Click "Restore Original"
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_reset, parentmenuContainer_css)
        time.sleep(Global_variables.mediumwait)
        
        """
        Step 13: Verify the original chart is restored
        """
        visual_obj.wait_for_number_of_element(element_css1, expected_number=7, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css2, expected_number=157, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, label_css="text[class^='totalLabel']", msg="Step 13:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 13:02:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 13:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 13:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 13:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 13:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 13:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 13:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 13:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 13:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 13:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 13:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 13:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 13:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 13:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 13:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 13:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 13:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 13:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 13:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 13:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 13:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 13:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 13:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 13:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_wbody4_f', msg="Step 13:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 13:27: Verify legends")
        
        
        """
        Step 14: Resize the browser window and verify it does not throws any error message
        """
        driver.set_window_size(945, 1020)
        visual_obj.wait_for_number_of_element(element_css4, expected_number=157, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, label_css="text[class^='totalLabel']", msg="Step 14:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 14:02:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 14:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 14:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 14:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 14:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 14:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 14:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 14:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 14:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 14:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 14:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 14:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 14:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 14:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 14:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 14:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 14:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 14:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 14:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 14:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 14:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 14:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 14:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 14:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_wbody4_f', msg="Step 14:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 14:27: Verify legends")
        
        """
        Step 15: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()