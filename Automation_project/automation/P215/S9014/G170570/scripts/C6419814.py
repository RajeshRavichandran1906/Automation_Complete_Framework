'''
Created on Oct 22, 2018

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419814
Testcase Name : Verify to check Advanced Chart tool for Bar- 'Sales by Region Dashboard - Line chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.lib import utillity

class C6419814_TestClass(BaseTestCase):

    def test_C6419814(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        utillobj=utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 70
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        chart_title='Sales by Month (TY vs LY)'
        x_axis_title=['Sale Month']
        expected_legend_list=['Sales (TY)', 'Sales (LY)']
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_1"
        NO_OF_RISERS_WITHTAGNAME="#"+PARENT_CSS+" rect[class^='riser!']"
        NO_OF_RISERS_WITHTAGNAME1="#"+PARENT_CSS+" path[class^='riser!']"
        TOTAL_RISERS="[class*='riser!s']"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_riser_css="#"+PARENT_CSS+" "+linechart_no_of_risers
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 02 : Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=CHART_SEGMENT_CSS, no_of_element=26)
        
        """Verify output"""
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 02:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 02:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 02:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 02:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 02:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 02:6:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 02:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 02:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 02.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 03 : Go to Line chart "Sales by Month (TY vs LY)"
        Step 04 : Click first menu dropdown > Select "Chart/Roll up Tool"
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        
        """
        Step 05 : Click 'Bar' chart > OK
        """
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "bar", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_RISER_CSS1="riser!s0!g0!mbar!"
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '1M', '2M', '3M', '4M', '5M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 05:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 05:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 05:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 05:6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 05:07 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 05:08 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 24, msg="Step 05:09 :")
        
        
        """
        Step 06 : Select "Chart/Roll up Tool" > Click Stacked Bar > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "stackedbar", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 06:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 06:04 : Verify number of segments in Stacked bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 06:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 06.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 06:07 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 06:08 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 2, 12, msg="Step 06:09:")
        
        """
        Step 07 : Select "Chart/Roll up Tool" > Click Percent Bar > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "percentbar", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0%', '20%', '40%', '60%', '80%', '100%']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 07.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 07:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 07:04 : Verify number of segments in Percent bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 07:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 07.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 07:07 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 07:08 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 2, 12, msg="Step 07:09:")
        
        """
        Step 08 : Select "Chart/Roll up Tool" > Click Column > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "column", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 08.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 08:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 08:04 : Verify number of segments in Column bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 08:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 08.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 08:07 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 08:08 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 24, msg="Step 08:09:")
        
        """
        Step 09 : Select "Chart/Roll up Tool" > Click Stacked Column > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "stackedcolumn", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 09.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 09:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 09:04 : Verify number of segments in Stacked Column bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 09:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 09.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 09:07 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 09:08 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 24, msg="Step 09:09:")
        
        """
        Step 10 : Select "Chart/Roll up Tool" > Click Percent Column > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "percentcolumn", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0%', '20%', '40%', '60%', '80%', '100%']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 10:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 10.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 10:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 10:04 : Verify number of segments in Percent Column bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 10:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 10.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 10:07 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 10:08 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 2, 12, msg="Step 10:09:")
        
        """
        Step 11 : Select "Chart/Roll up Tool" > Click Column Depth > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "columndepth", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 144, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 11:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 11.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'venice_blue', parent_css="#"+PARENT_CSS, msg="Step 11:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 144, "Step 11:04 : Verify number of segments in Column Depth bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 11.4 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 11.5: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 11.6 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 11.7 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 4, 12, msg="Step 11.8:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME1, 8, 12, msg="Step 11.9:")
        
        """ 3D wall verification """
        wall1_css="#"+PARENT_CSS+" svg g .fillPanel"
        wall2_css="#"+PARENT_CSS+" svg g .chartFrame"
        utillobj.verify_object_visible(wall1_css, True, "Step 11:10 : Verify Vertical and Horizontal 3d wall is present in the columndepth chart")
        utillobj.verify_object_visible(wall2_css, True, "Step 11:11 : Verify background chart frame 3d wall is present in the columndepth chart")
        
        """
        Step 12 : Select "Chart/Roll up Tool" > Click Stacked Depth > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "stackeddepth", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 72, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 12:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 12.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'venice_blue', parent_css="#"+PARENT_CSS, msg="Step 12:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 72, "Step 12:04 : Verify number of segments in Stacked Depth bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 12.5 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 12.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 12.7 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 12.8 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 2, 12, msg="Step 12.9:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME1, 4, 12, msg="Step 12.10:")
        
        """ 3D wall verification """
        utillobj.verify_object_visible(wall1_css, True, "Step 12:11 : Verify Vertical and Horizontal 3d wall is present in the stackeddepth chart")
        utillobj.verify_object_visible(wall2_css, True, "Step 12:12 : Verify background chart frame 3d wall is present in the stackeddepth chart")
        
        """
        Step 13 : Select "Chart/Roll up Tool" > Click Percent Depth > OK
        """
        active_chart_obj.create_new_item("MAINTABLE_1", "Chart/Rollup Tool", index=1)
        chart_obj.wait_for_number_of_element('#wall1', 1, MEDIUM_WAIT)
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "percentdepth", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 72, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0%', '20%', '40%', '60%', '80%', '100%']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 13:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 13.2: Verify chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'venice_blue', parent_css="#"+PARENT_CSS, msg="Step 13:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 72, "Step 13:04 : Verify number of segments in Percent Depth bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 13.5 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 13.6: ')
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 13.7 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 13.8 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 2, 12, msg="Step 13.9:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME1, 4, 12, msg="Step 13.10:")
        
        """ 3D wall verification """
        utillobj.verify_object_visible(wall1_css, True, "Step 13:11 : Verify Vertical and Horizontal 3d wall is present in the Percent Depth chart")
        utillobj.verify_object_visible(wall2_css, True, "Step 13:12 : Verify background chart frame 3d wall is present in the Percent Depth chart")
        
        """
        Step 14: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()