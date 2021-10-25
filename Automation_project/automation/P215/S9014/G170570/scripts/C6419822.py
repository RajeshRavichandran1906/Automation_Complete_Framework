'''
Created on Oct 19, 2018

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419822
Testcase Name : Verify to check Advanced Chart tool for Scatter/Bubble/Heatmap- 'Sales by Region Dashboard - Line chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.lib import utillity

class C6419822_TestClass(BaseTestCase):

    def test_C6419822(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 70
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        chart_title='Sales by Month (TY vs LY)'
        linechart_x_axis_title=['Sale Month']
        scatter_x_axis_title=['Sale Month']
        scatter_y_axis_title=['Sales (TY)']
        bubble_x_axis_title=['Sale Month']
        bubble_y_axis_title=['Sales (TY)']
        heatmap_x_axis_title=['Sale Month', 'Sales (TY)']
        linechart_expected_legend_list=['Sales (TY)', 'Sales (LY)']
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        scatter_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        scatter_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        bubble_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        bubble_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        heatmap_expected_legend_list=['2.6M', '3M', '3.2M', '3.5M', '3.9M']
        heatmap_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        heatmap_z_axis_label1=['[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]', '[object Object]']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_1"
        linechart_parent_css="MAINTABLE_1"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        linechart_no_of_risers="path[class^='riser']"
        scatter_no_of_risers="circle[class^='riser']"
        bubble_no_of_risers="circle[class^='riser']"
        heat_no_of_risers="rect[class^='riser']"
        linechart_no_of_riser_css="#"+linechart_parent_css+" "+linechart_no_of_risers
        scatter_no_of_riser_css="#"+PARENT_CSS+" "+scatter_no_of_risers
        bubble_no_of_riser_css="#"+PARENT_CSS+" "+bubble_no_of_risers
        heat_no_of_riser_css="#"+PARENT_CSS+" "+heat_no_of_risers
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 02 : Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=CHART_SEGMENT_CSS, no_of_element=26)
        
        """Verify output"""
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 02:1: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 02:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 02:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 02:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 02:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 02:6:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 02:7: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 02:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 02.9: Verify Line chart title", parent_css="#"+linechart_parent_css, title_css="[class^='title']")
        
        """
        Step 03 : Go to Line chart "Sales by Month (TY vs LY)"
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        
        """
        Step 04 : Click "Advanced Chart" icon > Scatter (XY Plot) > OK
        """
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "scatter(xy_plot)", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 12, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(scatter_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 04:1: ')
        chart_obj.verify_y_axis_title_in_run_window(scatter_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 04.2: ')
        chart_obj.verify_x_axis_label_in_run_window(scatter_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 04.3: ")
        chart_obj.verify_y_axis_label_in_run_window(scatter_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 04.4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mmarker!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 04:5: Verify scatter color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 12, "Step 04:6:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 04:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(scatter_no_of_riser_css, 1, 12, msg="Step: 04:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 04.9: Verify scatter chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 05 : Click "Advanced Chart" icon > Bubble > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        active_chart_obj.select_advance_chart(wall1_window_css, "bubble", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 12, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(bubble_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 05:1: ')
        chart_obj.verify_y_axis_title_in_run_window(bubble_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 05.2: ')
        chart_obj.verify_x_axis_label_in_run_window(bubble_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 05.3: ")
        chart_obj.verify_y_axis_label_in_run_window(bubble_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 05.4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mmarker!']", "bar_blue", parent_css="#"+PARENT_CSS, msg="Step 05:5: Verify bubble color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 12, "Step 05:6:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 05:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(bubble_no_of_riser_css, 1, 12, msg="Step: 05:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.9: Verify bubble chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 06 : Click "Advanced Chart" icon > Heatmap > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        active_chart_obj.select_advance_chart(wall1_window_css, "heatmap", 1)
        chart_obj.wait_for_number_of_element(heat_no_of_riser_css, 12, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(heatmap_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 06:1: ')
        chart_obj.verify_legends_in_run_window(heatmap_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 06:3: ')
        chart_obj.verify_x_axis_label_in_run_window(heatmap_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 06.4: ")
        chart_obj.verify_z_axis_label_in_run_window(heatmap_z_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 06.5: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s11!g11!mbar!']", "elf_green", parent_css="#"+PARENT_CSS, msg="Step 06.6: Verify riser color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 12, "Step 06.7:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 06.8: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(heat_no_of_riser_css, 1, 12, msg="Step: 06.9: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.10: Verify heatmap title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 07 : Click Original Chart icon
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 2)
        
        """Verify the original Line chart is displayed"""
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 07:1: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 07:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 07:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 07:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 07:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 07:6:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 07:7: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 07:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 07.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()
