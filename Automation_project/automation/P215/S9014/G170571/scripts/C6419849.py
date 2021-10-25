'''
Created on Sep 17, 2018

@author: Magesh

Testcase Name : Verify to Interact with Analytical Dashboard - Bubble Chart
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419849
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C6419849_TestClass(BaseTestCase):

    def test_C6419849(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419849"
        fex_name='Analytical_Dashboard'
        expected_label_list1=["1.1B"]
        expected_label_list2=["Revenue"]
        expected_label_list3=["Sales by Product Category"]
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        element_css1="#MAINTABLE_wbody1 svg.rootPanel>g.chartPanel >g>g>g>path[class^='riser']"
        element_css2="#MAINTABLE_wbody2  svg g circle[class^='riser']"
        element_css3="#MAINTABLE_wbody2 circle[class*='riser']"
        element_css4="#MAINTABLE_wbody3 svg > g text[class^='xaxis'][class*='labels']"
        element_css5="#MAINTABLE_wbody2  svg g circle[class^='riser']"
        table_css='#MAINTABLE_wbody5 .arPivot table > tbody > tr'
        
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
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 03:02:Verify x_axis label in runtime")
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
        Step 04: Go to "Product Analysis", lasso 58 points > Click Exclude from chart.
        """
        time.sleep(Global_variables.longwait)
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody2 [class*='riser!s3!g4!mmarker!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody2 [class*='riser!s5!g12!mmarker!']")
        source_element_location='top_left'
        target_element_location='bottom_right'
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-30, source_yoffset=-30, target_xoffset=50, target_yoffset=30, source_element_location=source_element_location, target_element_location=target_element_location)
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        
        """
        Step 05: Verify the Result
        """
        visual_obj.wait_for_number_of_element(element_css3, expected_number=99, time_out=wait_time)
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 03:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 03:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 03:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 100, msg="Step 03:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 03:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '3.4M', '1.7M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 03:13: Verify legends")
        
        """
        Step 06: Click "Run menu icon" at the bottom and Click "Show data"
        """
        parent_css="#MAINTABLE_menuContainer2"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css)
        
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds01.xlsx'
#         visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 06.1:')
        
        """
        Step 07: Click "Show data" again to return back to Chart 
        """
        parent_css="#MAINTABLE_menuContainer2"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        
        """
        Step 08: Click Remove filter (from Run menu icon)
        """
        parent_css="#MAINTABLE_menuContainer2"
        menu_option_button_name='remove_filter'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        
        """
        Verify the original chart is restored
        """
        visual_obj.wait_for_number_of_element(element_css1, expected_number=7, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css2, expected_number=157, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, label_css="text[class^='totalLabel']", msg="Step 08:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 08:02:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 08:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 08:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 08:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 08:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 08:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 08:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 08:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 08:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 08:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 08:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 08:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 08:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 08:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 08:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 08:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 08:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 08:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 08:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 08:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 08:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 08:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_wbody4_f', msg="Step 08:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 08:27: Verify legends")
        
        """
        Step 09: Resize the browser window and verify it does not throws any error message
        """
        driver.set_window_size(945, 1020)
        visual_obj.wait_for_number_of_element(element_css4, expected_number=12, time_out=wait_time)
        visual_obj.wait_for_number_of_element(element_css5, expected_number=157, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, label_css="text[class^='totalLabel']", msg="Step 09:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 09:02:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 09:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 09:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 09:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 09:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 09:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 09:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 09:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 09:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 09:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 09:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 09:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 09:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 09:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 09:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 09:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 09:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 09:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 09:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 09:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 09:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_wbody4_f', msg="Step 09:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 09:27: Verify legends")
        
        """
        Step 10: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()