'''
Created on Sep 14, 2018

@author: Magesh

Testcase Name : Verify to Interact with Analytical Dashboard - Line Chart
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275871&group_by=cases:section_id&group_id=170571&group_order=asc
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C2275871_TestClass(BaseTestCase):

    def test_C2275871(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C2275871"
        fex_name='Analytical_Dashboard'
        expected_label_list1=["1.1B"]
        expected_label_list2=["Revenue"]
        expected_label_list3=["Sales by Product Category"]
        expected_label_list4=["82.6M"]
        wait_time=140
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        element_css1="#MAINTABLE_wbody1 path[class^='riser']"
        element_css3="#MAINTABLE_wbody3 text[class^='xaxis'][class*='labels']"
        element_css4="#MAINTABLE_wbody3 path[class^='riser']"
        element_css5="#MAINTABLE_wbody3 text[class^='xaxis'][class*='labels']"
        element_css7="#MAINTABLE_wbody3 text[class^='xaxis'][class*='labels']"
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
         
        """
        Step 03: Verify the following output
        """
        "---1. ring pie chart---"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, label_css="text[class^='totalLabel']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, label_css="text[class^='pieLabel!g']", msg="Step 03:02:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 03:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 03:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 03:05:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 03:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_x_axis_title_list=['Revenue']
        expected_y_axis_title_list=['Product Analysis']
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 03:07:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 03:08:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 03:09:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:10:Verify y_axis title at runtime")
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 03:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 03:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 03:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 03:14:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 03:15:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 03:16:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 03:19:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 03:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_x_axis_title_list=['Model']
        expected_y_axis_title_list=['Quantity Sold by Product']
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 03:21:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 03:22:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 03:23:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:24:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 03:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_wbody4_f', msg="Step 03:26:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 03:27: Verify legends")
        
        """
        Step 04: Go to "Reveneue vs COGS by Month" > Lasso 8 points > Click filter chart
        """
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody3 [class*='marker!s0!g3!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sx=coord['x']-10
        sy=coord['y']-20
        time.sleep(Global_variables.mediumwait)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody3 [class*='marker!s1!g6!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        tx=coord['x']+10
        ty=coord['y']+20
        time.sleep(Global_variables.mediumwait)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_lasso_tooltip('Filter Chart')
        
        """
        Step 05: Verify the Result
        """
        expected_x_axis_labels=['4', '5', '6', '7']
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.wait_for_number_of_element(element_css3, expected_number=4, time_out=wait_time)
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 05:01:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 05:02:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 05:03:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 05.04:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 05.05:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 05.06:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 05.07: Verify legends")
        
        """
        Step 06: Click "Run menu icon" at the bottom and Click "Show data"
        """
        parent_css="#MAINTABLE_menuContainer3"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css)
        
        """
        Verify the output
        """
        file_name=TestCase_ID+'_Ds01.xlsx'
#         visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 06.1:')
        
        """
        Step 07: Click "Show data" again to return back to Chart and Click Run menu to dismiss
        """
        parent_css="#MAINTABLE_menuContainer3"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, parent_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer3", toggle_button_click='yes')
        
        """
        Step 08: Hover over on point 5 > Click Drilldown to Sale Day (Blue line)
        """
        visual_obj.wait_for_number_of_element(element_css4, expected_number=2, time_out=wait_time)
        riser_css='marker!s1!g1!mmarker!'
        parent_css='MAINTABLE_wbody3'
        menu_path='Drill down to Sale Day'
        visual_obj.select_tooltip(riser_css, menu_path, parent_css, use_marker_enable=True, move_to_tooltip=True)
        
        """
        Step 09: Verify the following output is displayed
        """
        visual_obj.wait_for_number_of_element(element_css5, expected_number=31, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list4, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='totalLabel']", msg="Step 09:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='pieLabel!g']", msg="Step 09.2:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 09.3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 09.4:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 09.5:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 09.6: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        expected_y_axis_labels=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500', '5,000']
        expected_x_axis_title_list=['Revenue']
        expected_y_axis_title_list=['Product Analysis']
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '519.3K', '261.6K', '4K']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 09.7:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 09.8:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 09.9:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09.10:Verify y_axis title at runtime")
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 154, msg="Step 09.11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 09.12:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 09.13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        expected_y_axis_labels=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M']
        expected_x_axis_title_list=['Sale Day']
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        expected_legends=['Revenue', 'Cost of Goods']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 09.14:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 09.15:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 09.16:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09.17:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 09.18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 09.19:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 09.20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['B00D7MOHDO', 'BCG34HRE4KN', 'DS1155/37', 'DMP-692', 'Sennheiser SET830S', 'DS3205/37', 'JVC GCFM2BUS', 'LG MDD72', 'Niles Audio RCAHT2']
        expected_y_axis_labels=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500', '5,000']
        expected_x_axis_title_list=['Model']
        expected_y_axis_title_list=['Quantity Sold by Product']
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        expected_legends=['Revenue', '0M', '0.3M', '0.6M', '0.9M', '1.2M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 09.21:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody4', msg="Step 09.22:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 09.23:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 09.24:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 153, msg="Step 09.25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g14!mbar!']", 'dark_moderate_cyan', parent_css='#MAINTABLE_wbody4_f', msg="Step 09.26:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 09.27: Verify legends")
        
        """
        Step 10: Resize the browser window and verify it does not throws any error message
        """
        driver.set_window_size(945, 1020)
        visual_obj.wait_for_number_of_element(element_css7, expected_number=31, time_out=wait_time)
        
        "---1. ring pie chart---"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_pie_label_in_single_group(expected_label_list4, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='totalLabel']", msg="Step 10:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, parent_css='#MAINTABLE_wbody1 svg > g', label_css="text[class^='pieLabel!g']", msg="Step 10.2:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_wbody1', label_css="[class^='title'] span", msg="Step 10.3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_wbody1', 1, 7, msg="Step 10.4:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', msg="Step 10.5:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 10.6: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        expected_y_axis_labels=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500', '5,000']
        expected_x_axis_title_list=['Revenue']
        expected_y_axis_title_list=['Product Analysis']
        parent_css_with_tag_name="#MAINTABLE_wbody2"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '519.3K', '261.6K', '4K']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 10.7:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody2', msg="Step 10.8:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody2', msg="Step 10.9:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 10.10:Verify y_axis title at runtime")
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 154, msg="Step 10.11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_wbody2_f', msg="Step 10.12:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 10.13: Verify legends")
        
        "---3. Line chart---"
        expected_y_axis_labels=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M']
        expected_x_axis_title_list=['Sale Day']
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        parent_css_with_tag_name="#MAINTABLE_wbody3 path"
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody3', msg="Step 10.15:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody3', msg="Step 10.16:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 10.17:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 10.18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_wbody3_f', attribute='stroke', msg="Step 10.19:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody3", msg="Step 10.20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_title_list=['Model']
        expected_y_axis_title_list=['Quantity Sold by Product']
        parent_css_with_tag_name="#MAINTABLE_wbody4 rect"
        expected_legends=['Revenue', '0M', '0.3M', '0.6M', '0.9M', '1.2M']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody4', msg="Step 10.23:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 10.24:Verify y_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 153, msg="Step 10.25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g14!mbar!']", 'dark_moderate_cyan', parent_css='#MAINTABLE_wbody4_f', msg="Step 10.26:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody4", msg="Step 10.27: Verify legends")
        
        """
        Step 11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()