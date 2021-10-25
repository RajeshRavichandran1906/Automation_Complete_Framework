'''
Created on Sep 19, 2018

@author: Magesh

Testcase Name : Verify to restore successful with Analytical Dashboard
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419856
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C6419856_TestClass(BaseTestCase):

    def test_C6419856(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419856"
        folder_name="Retail_Samples/Visualizations"
        edit_fex_folder_after_save="SmokeTest/~rsadv"
        fex_name='Analytical_Dashboard'
        save_fex_name='Analytical_Dashboard1'
        expected_label_list1=["1.1B"]
        expected_label_list2=["Revenue"]
        expected_label_list3=["Sales by Product Category"]
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        preview_css1="#ar_TableChart_1 path[class^='riser']"
        preview_css2="#ar_TableChart_2 svg g circle[class^='riser']"
        run_css1="#MAINTABLE_1 path[class^='riser']"
        run_css2="#MAINTABLE_2 circle[class^='riser']"
        app_btn_css="#applicationButtonBox"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Edit the Visualizations using the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Visualizations/Analytical_Dashboard.fex&tool=idis
        """
        visual_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=7, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=157, time_out=wait_time)
        
        """
        Verify the following Charts are displayed
        """
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, parent_css='#ar_TableChart_1 svg > g', label_css="text[class^='totalLabel']", msg="Step 02:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, parent_css='#ar_TableChart_1 svg > g', label_css="text[class^='pieLabel!g']", msg="Step 02:02:Verify pie label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#ar_TableChart_1', label_css="[class^='title'] span", msg="Step 02:3")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_1', 1, 7, msg="Step 02:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', parent_css='#ar_TableChart_1', msg="Step 02:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_1", msg="Step 02:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_2', msg="Step 02:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_2', msg="Step 02:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_2', msg="Step 02:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 02:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#ar_TableChart_2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 02:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#ar_TableChart_2', msg="Step 02:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_2", msg="Step 02:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_3', msg="Step 02:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_3', msg="Step 02:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_3', msg="Step 02:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 02:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#ar_TableChart_3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 02:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_3', attribute='stroke', msg="Step 02:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_3", msg="Step 02:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_4', msg="Step 02:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_4', msg="Step 02:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_4', msg="Step 02:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 02:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#ar_TableChart_4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 02:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#ar_TableChart_4', msg="Step 02:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_4", msg="Step 02:27: Verify legends")
        
        """
        Step 03: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
        time.sleep(2*Global_variables.longwait)
        
        """
        Verify the following Charts are displayed
        """
        visual_obj.wait_for_number_of_element(run_css1, expected_number=7, time_out=wait_time)
        visual_obj.wait_for_number_of_element(run_css2, expected_number=157, time_out=wait_time)
        
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='totalLabel']", msg="Step 03:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, parent_css='#MAINTABLE_1 svg > g', label_css="text[class^='pieLabel!g']", msg="Step 03:02:Verify pie label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#MAINTABLE_1', label_css="[class^='title'] span", msg="Step 03:3")
        visual_obj.verify_number_of_pie_segments('#MAINTABLE_1', 1, 7, msg="Step 03:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 03:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_1", msg="Step 03:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_2', msg="Step 03:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_2', msg="Step 03:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_2', msg="Step 03:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 03:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#MAINTABLE_2', msg="Step 03:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_2", msg="Step 03:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_3', msg="Step 03:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_3', msg="Step 03:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_3', msg="Step 03:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 03:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#MAINTABLE_3', attribute='stroke', msg="Step 03:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_3", msg="Step 03:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_4', msg="Step 03:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_4', msg="Step 03:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 03:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#MAINTABLE_4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 03:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#MAINTABLE_4', msg="Step 03:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_4", msg="Step 03:27: Verify legends")
        
        """
        Step 04: Close the output window
        """
        visual_obj.switch_to_previous_window()
        time.sleep(Global_variables.longwait)
        visual_obj.wait_for_number_of_element(app_btn_css, expected_number=1, time_out=wait_time)
        
        """
        Step 05: Click IA > Save as > Select "SmokeTest" > Mycontent folder > Enter title as "Analytical Dashboard1" > Click Save
        """
        visual_obj.save_as_from_application_menu_item(save_fex_name)
        
        """
        Step 06: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual_obj.logout_visualization_using_api()
        
        """
        Step 07: Edit the saved Visualization using "rsadv" user with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Analytical_Dashboard1.fex&tool=Document
        """
        visual_obj.edit_fex_using_api_url(edit_fex_folder_after_save, fex_name=save_fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=7, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=157, time_out=wait_time)
        
        """
        Verify restore successful
        """
        "---1. ring pie chart---"
        visual_obj.verify_pie_label_in_single_group(expected_label_list1, parent_css='#ar_TableChart_1 svg > g', label_css="text[class^='totalLabel']", msg="Step 07:01:Verify x_axis label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list2, parent_css='#ar_TableChart_1 svg > g', label_css="text[class^='pieLabel!g']", msg="Step 07:02:Verify pie label in runtime")
        visual_obj.verify_pie_label_in_single_group(expected_label_list3, parent_css='#ar_TableChart_1', label_css="[class^='title'] span", msg="Step 07:3")
        visual_obj.verify_number_of_pie_segments('#ar_TableChart_1', 1, 7, msg="Step 07:04:Verify x_axis label in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mwedge!']", 'lochmara_1', parent_css='#ar_TableChart_1', msg="Step 07:05:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_1", msg="Step 07:06: Verify legends")
        
        "---2. bubble chart---"
        expected_x_axis_labels=['0', '4M', '8M', '12M', '16M']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_2', msg="Step 07:07:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_2', msg="Step 07:08:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Revenue']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_2', msg="Step 07:09:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Product Analysis']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_2', x_or_y_axis_title_css="[class^='title'] span", msg="Step 07:10:Verify y_axis title at runtime")
        parent_css_with_tag_name="#ar_TableChart_2"
        visual_obj.verify_number_of_circles(parent_css_with_tag_name, 1, 158, msg="Step 07:11:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("circle[class^='riser!s0!g1!mmarker!']", 'lochmara_1', parent_css='#ar_TableChart_2', msg="Step 07:12:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit', '7M', '3.5M', '0M']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_2", msg="Step 07:13: Verify legends")
        
        "---3. Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_3', msg="Step 07:14:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_3', msg="Step 07:15:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_3', msg="Step 07:16:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Revenue vs COGS by Month']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_3', x_or_y_axis_title_css="[class^='title'] span", msg="Step 07:17:Verify y_axis title at runtime")
        parent_css_with_tag_name="#ar_TableChart_3 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, msg="Step 07:18:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!']", 'lochmara_1', parent_css='#ar_TableChart_3', attribute='stroke', msg="Step 07:19:Verify chart color")
        expected_legends=['Revenue', 'Cost of Goods']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_3", msg="Step 07:20: Verify legends")
        
        "---4. Bar chart---"
        expected_x_axis_labels=['DMP-692', 'DS3205/37', 'DS1155/37', 'B00D7MOHDO', 'BCG34HRE4KN', 'JVC XV-BP11', 'Samsung HT-Z120', 'LG MDD72', 'Sennheiser SET830S', 'Sony STRDH810']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_4', msg="Step 07:21:Verify x_axis label in runtime")
        expected_y_axis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_4', msg="Step 07:22:Verify y-axis label in runtime")
        expected_x_axis_title_list=['Model']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_4', msg="Step 07:23:Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity Sold by Product']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_4', x_or_y_axis_title_css="[class^='title'] span", msg="Step 07:24:Verify y_axis title at runtime")
        parent_css_with_tag_name="#ar_TableChart_4 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 157, msg="Step 07:25:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!']", 'soft_orange1', parent_css='#ar_TableChart_4', msg="Step 07:26:Verify chart color")
        expected_legends=['Revenue', '0M', '3.8M', '7.5M', '11.3M', '15M']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_4", msg="Step 07:27: Verify legends")
        
        """
        Step 08: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()