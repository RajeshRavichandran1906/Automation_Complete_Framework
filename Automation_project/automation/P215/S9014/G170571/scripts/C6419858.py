'''
Created on Oct 24, 2018

@author: Magesh

Testcase Name : Verify to Interact with the Executive Dashboard - Bar charts
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419858
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.lib import utillity

class C6419858_TestClass(BaseTestCase):

    def test_C6419858(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419858"
        fex_name='Executive_Dashboard'
        expected_guage1_label_list1=["130.8M"]
        expected_guage1_label_list2=["Revenue"]
        expected_guage2_label_list1=["37.1M"]
        expected_guage2_label_list2=["Gross Profit"]
        expected_guage3_label_list1=["439K"]
        expected_guage3_label_list2=["Quantity Sold"]
        expected_guage1_label_list1a=["682K"]
        expected_guage2_label_list1a=["196K"]
        expected_guage3_label_list1a=["1,997"]
        menu_option_button_name_reset='reset'
        source_element_location='top_middle'
        target_element_location='bottom_middle'
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        element_css1="#MAINTABLE_7 svg>g rect[class^='riser']"
        element_css2="#MAINTABLE_9 svg>g rect[class^='riser']"
        element_css3="#MAINTABLE_7 svg > g text[class^='yaxis-labels']"
        element_css4="#MAINTABLE_5 path[class^='riser']"
        element_css5="#MAINTABLE_8 svg>g rect[class^='riser']"
        element_css6="#MAINTABLE_6 path[class^='riser']"
        source_css_locator="#MAINTABLE_8 [class*='riser!s0!g0!mbar!']"
        target_css_locator="#MAINTABLE_8 [class*='riser!s0!g3!mbar!']"
        table_css1='#MAINTABLE_wbody10 .arPivot table > tbody > tr'
        parentmenuContainer_css="#MAINTABLE_menuContainer6"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Visualizations&BIP_item=Executive_Dashboard.fex
        """
        visual_obj.run_visualization_using_api(fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(element_css1, expected_number=29, time_out=wait_time)
        
        """
        Step 03: Verify the following Charts are displayed
        """
        "---1. guage chart1---"
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='Total']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 03:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 1, msg="Step 03:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 03:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#MAINTABLE_2 svg > g', label_css="text[class^='Total']", msg="Step 03:05:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#MAINTABLE_2', label_css="[class^='title'] span", msg="Step 03:6")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_2', 1, 1, msg="Step 03:07:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 03:08:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#MAINTABLE_3 svg > g', label_css="text[class^='Total']", msg="Step 03:09:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#MAINTABLE_3', label_css="[class^='title'] span", msg="Step 03:10")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_3', 1, 1, msg="Step 03:11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_3', msg="Step 03:12:Verify chart color")
        
        "---4. Line chart1---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Quantity Sold']
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_4 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:13:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:14:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:15:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:16:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 03:19:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 03:20: Verify legends")
        
        "---5. Line chart2---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_5 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:21:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 03:22:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:23:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 03:24:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:25:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:26:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 03:27:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 03:28: Verify legends")
        
        "---6. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_6 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 03:29:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 03:30:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 03:31:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 03:32:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:33:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:34:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 03:35:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 03:36: Verify legends")
        
        "---7. Bar chart1---"
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        expected_x_axis_title_list=['Store Name']
        expected_y_axis_title_list=['Revenue']
        expected_y_axis_title_list1=['Revenue by Store']
        parent_css_with_tag_name="#MAINTABLE_7 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 03:37:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_7', msg="Step 03:38:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 03:39:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 03:40:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:41:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 29, msg="Step 03:42:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 03:43:Verify chart color")
        
        "---8. Bar chart2---"
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions']
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y_axis_title_list1=['Gross Profit by Product Category']
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_8', msg="Step 03:44:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 03:45:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 03:46:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 03:47:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:48:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 03:49:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 03:50:Verify chart color")
        
        "---9. Bar chart3---"
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        expected_x_axis_title_list=['Business Region']
        expected_y_axis_title_list=['Quantity Sold']
        expected_y_axis_title_list1=['Quantity Sold by Region']
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 03:51:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_9', msg="Step 03:52:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 03:53:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 03:54:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:55:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 03:56:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 03:57:Verify chart color")
        
        """
        Step 04: Go to "Quantity Sold by Region" 
        Step 05: Hover over "EMEA" and click "Filter Chart"
        """
        parent_css='MAINTABLE_9'
        riser_css1='riser!s0!g0!mbar!'
        menu_path1='Filter Chart'
        visual_obj.select_tooltip(riser_css1, menu_path1, parent_css, element_location='middle', move_to_tooltip=True)
        
        """
        Step 06: Verify the selected value is filtered
        """
        visual_obj.wait_for_number_of_element(element_css2, expected_number=1, time_out=wait_time)
        expected_x_axis_labels=['EMEA']
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        expected_x_axis_title_list=['Business Region']
        expected_y_axis_title_list=['Quantity Sold']
        expected_y_axis_title_list1=['Quantity Sold by Region']
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 06.1:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_9', msg="Step 06.2:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 06.3:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 06.4:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 06.5:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 06.6:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 06.7:Verify chart color")
        
        """
        Step 07: Go to "Gross Profit by Product Category"
        Step 08: Lasso first 4 risers and Click Exclude from chart
        """
        visual_obj.wait_for_number_of_element(element_css5, expected_number=7, time_out=wait_time)
        time.sleep(Global_variables.longwait)
        source_element=utillobj.validate_and_get_webdriver_object(source_css_locator, "Source Lasso bar riser")
        target_element=utillobj.validate_and_get_webdriver_object(target_css_locator, "Target Lasso bar riser")
        visual_obj.create_lasso(source_element, target_element, source_yoffset=-10, source_element_location=source_element_location, target_element_location=target_element_location)
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        
        """
        Step 09: Verify the Result
        """
        visual_obj.wait_for_number_of_element(element_css5, expected_number=3, time_out=wait_time)
        expected_x_axis_labels=['Video Production', 'Computers', 'Televisions']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y_axis_title_list1=['Gross Profit by Product Category']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_8', msg="Step 09.1:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 09.2:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 09.3:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 09.4:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09.5:Verify bar chart title at runtime")
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 09.6:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 09.7:Verify chart color")
        
        
        """
        Step 10: Click "Run menu icon" at the bottom and Click "Show data"
        """
        parent_css="#MAINTABLE_menuContainer8"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css)
        
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds01.xlsx'
#         visual_obj.create_visualization_tabular_report(file_name, table_css1)
        visual_obj.verify_visualization_tabular_report(file_name, table_css1, msg='Step 10.1:')
        
        """
        Step 11: Click "Show data" again to return back to Chart and click Run menu to dismiss
        """
        parent_css="#MAINTABLE_menuContainer8"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer8", toggle_button_click='yes')
        
        """
        Step 12: Go to "Revenue by Store"> Hover over Chart riser "London"
        Step 13: Click "Drill Up to Store Postal Code "
        """
        visual_obj.wait_for_number_of_element(element_css1, expected_number=20, time_out=wait_time)
        parent_css='MAINTABLE_7'
        riser_css1='riser!s0!g1!mbar!'
        menu_path1='Drill up to Store Postal Code'
        visual_obj.select_tooltip(riser_css1, menu_path1, parent_css, element_location='middle', move_to_tooltip=True)
        
        """
        Step 14: Verify the Result
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=5, time_out=wait_time)
        expected_x_axis_labels=['1012', '111 44', 'SW1V', '00176', '10969', '20154', '28002', '2300', '00-203', '1204', '1060']
        expected_y_axis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        expected_x_axis_title_list=['Store Postal Code']
        expected_y_axis_title_list=['Revenue']
        expected_y_axis_title_list1=['Revenue by Store']
        parent_css_with_tag_name="#MAINTABLE_7 rect"
        
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 14.1:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_7', msg="Step 14.2:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 14.3:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 14.4:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 14.5:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 20, msg="Step 14.6:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 14.7:Verify chart color")
        
        """
        Step 15: Go to "Revenue (TY vs LY) by Month".
        Hover over any chart riser (eg: Sale month 5) > Click "Drill down to Sale Day"
        """
        visual_obj.wait_for_number_of_element(element_css6, expected_number=2, time_out=wait_time)
        source_element=utillobj.validate_and_get_webdriver_object('#MAINTABLE_wbody6', "Line chart parent css")
        utillobj.click_on_screen(source_element, 'bottom_middle')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody6 [class*='marker!s1!g4!mmarker!']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        
        time.sleep(Global_variables.mediumwait)
        riser_css='marker!s1!g4!mmarker!'
        parent_css='MAINTABLE_wbody6'
        menu_path='Drill down to->Sale Day'
        visual_obj.select_tooltip(riser_css, menu_path, parent_css,initial_move_xy_dict={'x':900,'y':657}, use_marker_enable=True, move_to_tooltip=True)
        
        """
        Step 16: Verify the following output
        """
        visual_obj.wait_for_number_of_element(element_css1, expected_number=18, time_out=wait_time)
        
        "---1. guage chart1---"
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1a, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='Total']", msg="Step 16:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 16:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 1, msg="Step 16:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 16:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1a, parent_css='#MAINTABLE_2 svg > g', label_css="text[class^='Total']", msg="Step 16.5:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#MAINTABLE_2', label_css="[class^='title'] span", msg="Step 16.6")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_2', 1, 1, msg="Step 16.7:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 16.8:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1a, parent_css='#MAINTABLE_3 svg > g', label_css="text[class^='Total']", msg="Step 16.9:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#MAINTABLE_3', label_css="[class^='title'] span", msg="Step 16.10")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_3', 1, 1, msg="Step 16.11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_3', msg="Step 16.12:Verify chart color")
        
        "---4. Line chart1---"
        expected_x_axis_labels=['5']
        expected_y_axis_labels=['0', '400', '800', '1,200', '1,600', '2,000', '2,400']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Quantity Sold']
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_4 path"
        expected_legends=['Sale Year', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 16.13:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 16.14:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 16.15:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 16.16:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 16:17:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 16:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 16:19:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 16:20: Verify legends")
        
        "---5. Line chart2---"
        expected_x_axis_labels=['5']
        expected_y_axis_labels=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_5 path"
        expected_legends=['Sale Year', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 16.21:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 16.22:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 16.23:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 16.24:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 16.25:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 16.26:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 16.27:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 16.28: Verify legends")
        
        "---6. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K']
        expected_x_axis_title_list=['Sale Day']
        expected_y_axis_title_list=['Revenue']
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_6 path"
        expected_legends=['Sale Year', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 16.29:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 16.30:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 16.31:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 16.32:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 16.33:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 16.34:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 16.35:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 16.36: Verify legends")
        
        "---7. Bar chart1---"
        expected_x_axis_labels=['20154', '28002', '00176']
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_x_axis_title_list=['Store Postal Code']
        expected_y_axis_title_list=['Revenue']
        expected_y_axis_title_list1=['Revenue by Store']
        parent_css_with_tag_name="#MAINTABLE_7 rect"
            
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 16.37:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_7', msg="Step 16.38:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 16.39:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 16.40:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 16.41:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 18, msg="Step 16.42:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 16.43:Verify chart color")
        
        "---8. Bar chart2---"
        expected_x_axis_labels=['Video Production', 'Computers', 'Televisions']
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y_axis_title_list1=['Gross Profit by Product Category']
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_8', msg="Step 16.44:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 16.45:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 16.46:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 16.47:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 16.48:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 16.49:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 16.50:Verify chart color")
        
        "---9. Bar chart3---"
        expected_x_axis_labels=['EMEA']
        expected_y_axis_labels=['0', '400', '800', '1,200', '1,600', '2,000', '2,400']
        expected_x_axis_title_list=['Business Region']
        expected_y_axis_title_list=['Quantity Sold']
        expected_y_axis_title_list1=['Quantity Sold by Region']
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 16.51:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_9', msg="Step 16.52:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 16.53:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 16.54:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 16.55:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 16.56:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 16.57:Verify chart color")
        
        """
        Step 17: Click Run menu icon > Click "Restore Original"
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_reset, parentmenuContainer_css)
        time.sleep(Global_variables.mediumwait)
        
        """
        Verify original dashboard is restored back
        """
        visual_obj.wait_for_number_of_element(element_css1, expected_number=29, time_out=wait_time)
        
        "---1. guage chart1---"
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='Total']", msg="Step 17:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 17:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 1, msg="Step 17:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 17:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#MAINTABLE_2 svg > g', label_css="text[class^='Total']", msg="Step 17:05:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#MAINTABLE_2', label_css="[class^='title'] span", msg="Step 17:6")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_2', 1, 1, msg="Step 17:07:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 17:08:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#MAINTABLE_3 svg > g', label_css="text[class^='Total']", msg="Step 17:09:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#MAINTABLE_3', label_css="[class^='title'] span", msg="Step 17:10")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_3', 1, 1, msg="Step 17:11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_3', msg="Step 17:12:Verify chart color")
        
        "---4. Line chart1---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Quantity Sold']
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_4 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 17:14:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 17:15:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 17:16:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 17:17:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 17:18:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 17:19:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 17.20:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 17.21: Verify legends")
        
        "---5. Line chart2---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_5 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 17:22:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 17.23:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 17.24:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 17.25:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", msg="Step 17.26:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 17.27:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 17.28:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 17.29: Verify legends")
        
        "---6. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        expected_line_chart_title_list=['Revenue (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_6 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 17.30:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 17.31:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 17.32:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 17.33:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", msg="Step 17.34:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 17.35:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 17.36:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 17.37: Verify legends")
        
        "---7. Bar chart1---"
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        expected_x_axis_title_list=['Store Name']
        expected_y_axis_title_list=['Revenue']
        expected_y_axis_title_list1=['Revenue by Store']
        parent_css_with_tag_name="#MAINTABLE_7 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 17.38:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_7', msg="Step 17.39:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 17.40:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 17.41:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 17.42:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 29, msg="Step 17.43:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 17.44:Verify chart color")
        
        "---8. Bar chart2---"
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions']
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y_axis_title_list1=['Gross Profit by Product Category']
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_8', msg="Step 17.45:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 17.46:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 17.47:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 17.48:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 17.49:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 17.50:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 17.51:Verify chart color")
        
        "---9. Bar chart3---"
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        expected_x_axis_title_list=['Business Region']
        expected_y_axis_title_list=['Quantity Sold']
        expected_y_axis_title_list1=['Quantity Sold by Region']
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 17.52:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_9', msg="Step 17.53:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 17.54:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 17.55:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 17.56:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 17.57:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 17.58:Verify chart color")
        
        """
        Step 18: Resize the browser window and verify it does not throws any error message
        """
        driver.set_window_size(945, 1020)
        visual_obj.wait_for_number_of_element(element_css4, expected_number=2, time_out=wait_time)
        
        """
        Verify original dashboard is restored back
        """
        "---1. guage chart1---"
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list1, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='Total']", msg="Step 18:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage1_label_list2, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 18:2")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 1, msg="Step 18:03:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 18:04:Verify chart color")
        
        "---2. guage chart2---"
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list1, parent_css='#MAINTABLE_2 svg > g', label_css="text[class^='Total']", msg="Step 18.5:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage2_label_list2, parent_css='#MAINTABLE_2', label_css="[class^='title'] span", msg="Step 18.6")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_2', 1, 1, msg="Step 18.7:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 18.8:Verify chart color")
        
        "---3. guage chart3---"
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list1, parent_css='#MAINTABLE_3 svg > g', label_css="text[class^='Total']", msg="Step 18.9:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_guage3_label_list2, parent_css='#MAINTABLE_3', label_css="[class^='title'] span", msg="Step 18.10")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_3', 1, 1, msg="Step 18.11:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mrange!']", 'lochmara_1', parent_css='#MAINTABLE_3', msg="Step 18.12:Verify chart color")
        
        "---4. Line chart1---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Quantity Sold']
        expected_line_chart_title_list=['Quantity Sold (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_4 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 18.13:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 18.14:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 18.15:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 18:16:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", x_or_y_axis_title_length=5, msg="Step 18:17:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 18:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_4', attribute='stroke', msg="Step 18:19:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 18:20: Verify legends")
        
        "---5. Line chart2---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_line_chart_title_list=['Gross Profit (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_5 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_5', msg="Step 18.21:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_5', msg="Step 18.22:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 18.23:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_5', msg="Step 18.24:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list, parent_css='#MAINTABLE_5', x_or_y_axis_title_css="[class^='title'] span", x_or_y_axis_title_length=5, msg="Step 18.25:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 18.26:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_5', attribute='stroke', msg="Step 18.27:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_5", msg="Step 18.28: Verify legends")
        
        "---6. Line chart3---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        expected_line_chart_title_list1=['Revenue (TY vs LY) by Month']
        parent_css_with_tag_name="#MAINTABLE_6 path"
        expected_legends=['Sale Year', '2014', '2015']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_6', msg="Step 18.29:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_6', msg="Step 18.30:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 18.31:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_6', msg="Step 18.32:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_line_chart_title_list1, parent_css='#MAINTABLE_6', x_or_y_axis_title_css="[class^='title'] span", x_or_y_axis_title_length=5, msg="Step 18.33:Verify line chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 18.34:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_6', attribute='stroke', msg="Step 18.35:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_6", msg="Step 18.36: Verify legends")
        
        "---7. Bar chart1---"
        expected_x_axis_labels=['New York', 'Amsterdam', 'Madrid', 'Brasilia', 'Toronto', 'Milan', 'Geneva', 'Warsaw', 'Rome', 'Berlin', 'London']
        expected_x_axis_title_list=['Store Name']
        expected_y_axis_title_list=['Revenue']
        expected_y_axis_title_list1=['Revenue by Store']
        parent_css_with_tag_name="#MAINTABLE_7 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_7', msg="Step 18.37:Verify x_axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 18.38:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_7', msg="Step 18.39:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_7', x_or_y_axis_title_css="[class^='title'] span", msg="Step 18.40:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 29, msg="Step 18.41:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_7', msg="Step 18.42:Verify chart color")
        
        "---8. Bar chart2---"
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y_axis_title_list1=['Gross Profit by Product Category']
        parent_css_with_tag_name="#MAINTABLE_8 rect"
        
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_8', msg="Step 18.43:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 18.44:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_8', msg="Step 18.45:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_8', x_or_y_axis_title_css="[class^='title'] span", msg="Step 18.46:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 18.47:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_8', msg="Step 18.48:Verify chart color")
        
        "---9. Bar chart3---"
        expected_x_axis_labels=['EMEA', 'North America', 'South America']
        expected_x_axis_title_list=['Business Region']
        expected_y_axis_title_list=['Quantity Sold']
        expected_y_axis_title_list1=['Quantity Sold by Region']
        parent_css_with_tag_name="#MAINTABLE_9 rect"
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_9', msg="Step 18.49:Verify x_axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 18.50:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_9', msg="Step 18.51:Verify y_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list1, parent_css='#MAINTABLE_9', x_or_y_axis_title_css="[class^='title'] span", msg="Step 18.52:Verify bar chart title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 3, msg="Step 18.53:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'lochmara_1', parent_css='#MAINTABLE_9', msg="Step 18.54:Verify chart color")
        
        """
        Step 19: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()