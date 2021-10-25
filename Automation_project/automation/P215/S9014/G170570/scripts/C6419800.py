'''
Created on Sep 20, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6419800&group_by=cases:section_id&group_id=170570&group_order=asc
Testcase Name : Verify to check Advanced Chart tool for Bar- 'Sales by Region Dashboard - Pie chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6419800_TestClass(BaseTestCase):

    def test_C6419800(self):
        
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
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_0"
        
        RINGPIE_EXPECTED_LABEL=['Revenue']
        RINGPIE_EXPECTED_LEGENDLIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        RINGPIE_RISER_CSS1="[class='riser!s4!g0!mwedge!']"
        RINGPIE_RISER_CSS2="[class='riser!s0!g0!mwedge!']"
        RINGPIE_RISER_CSS3="[class='riser!s3!g0!mwedge!']"
        TOTAL_RISERS="[class*='riser!s']"
        CHART_TITLE='Sales by Product Category'
        NO_OF_RISERS_WITHTAGNAME="#"+PARENT_CSS+" rect[class^='riser!']"
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        RINGPIE_LABEL_CSS="#"+PARENT_CSS+" [class^='totalLabel']"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
            Step 01 : Sign to Webfocus using rsbas (basic user)
            http://machine:port/ibi_apps
            Step 02 : Run the Document using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=RINGPIE_LABEL_CSS, no_of_element=1)
        
        RINGPIE_EXPECTED_TOTALLABEL1=['70.1M']
        chart_obj.verify_legends_in_run_window(RINGPIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 03:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 03:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS2, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 03:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS3, 'pale_yellow', parent_css="#"+PARENT_CSS, msg="Step 03:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_LABEL, "Step 03:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_TOTALLABEL1, "Step 03:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 03:07: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 03:08:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 03:09: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        
        """
            Step 03 : Go to the Pie chart "Sales by Product Category"
            Step 04 : Click "Advanced Chart" icon
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        
        """
            Step 05 : Select "Bar Chart" > OK
        """
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "bar")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        BAR_RISER_CSS1="riser!s0!g0!mbar!"
        BAR_EXPECTED_LEGENDLIST=['Product Category', 'Revenue']
        BAR_EXPECTED_XAXIS_TITLE=['Product Category']
        BAR_EXPECTED_YAXIS_TITLE=['Revenue']
        BAR_EXPECTED_XAXIS_LABELLIST=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Produc...']
        
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '8M', '16M', '24M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 05:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 05:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 05:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 05:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 05:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 05:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 05:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 05:10 :")
        
        """
            Step 06 : Click "Advanced Chart" icon > Stacked Bar > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "stackedbar")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 06:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 06:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 06:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 06:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 06:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 06:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 06:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 06:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 06:10 :")
        
        """
            Step 07 : Click "Advanced Chart" icon > Percent Bar > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "percentbar")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        if Global_variables.browser_name in ('cr', 'Chrome', 'chrome'):
            BAR_EXPECTED_YAXIS_LABELLIST2=['0%', '20%', '40%', '60%', '80%', '100%']
            chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, msg="Step 07:01 :")
        else:
            BAR_EXPECTED_YAXIS_LABELLIST2= ['0%', '40%', '80%', '120%'] 
            chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Syste...', 'Televisions', 'Video Product...'], parent_css="#"+PARENT_CSS, msg="Step 07:01 :")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07:02 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 07:03 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 07:04 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 07:05 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 07:06 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 07:07 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 07:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST2, parent_css="#"+PARENT_CSS, msg="Step 07:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 07:10 :")
        
        """
            Step 08 : Click "Advanced Chart" icon > Column > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "column")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        
        BAR_EXPECTED_YAXIS_LABELLIST3=['0', '4M', '8M', '12M', '16M', '20M', '24M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 08:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 08:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 08:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 08:05 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 08:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 08:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 08:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST3, parent_css="#"+PARENT_CSS, msg="Step 08:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 08:10 :")
        
        """
            Step 09 : Click "Advanced Chart" icon > Stacked Column > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "stackedcolumn")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 09:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 09:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 09:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 09:05 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 09:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 09:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 09:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST3, parent_css="#"+PARENT_CSS, msg="Step 09:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 09:10 :")
        
        """
            Step 10 : Click "Advanced Chart" icon > Percent Column > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "percentcolumn")
        
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        BAR_EXPECTED_YAXIS_LABELLIST2=['0%', '20%', '40%', '60%', '80%', '100%']
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 10:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 10:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 10:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 10:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 10:05 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 10:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 10:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 10:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST2, parent_css="#"+PARENT_CSS, msg="Step 10:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 10:10 :")
        
        """
            Step 11: Click "Advanced Chart" icon > Column Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "columndepth")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 42, MEDIUM_WAIT)
        
        wall1_css="#"+PARENT_CSS+" svg g .fillPanel"
        wall2_css="#"+PARENT_CSS+" svg g .chartFrame"
        
        """
            Verify the Output
        """
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 11:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 11:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'venice_blue', parent_css="#"+PARENT_CSS, msg="Step 11:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 42, "Step 11:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 11:05 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 11:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 11:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 11:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST3, parent_css="#"+PARENT_CSS, msg="Step 11:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 2, msg="Step 11:10 :")
        
        """ 3D wall verification """
        
        utillobj.verify_object_visible(wall1_css, True, "Step 11:11 : Verify Vertical and Horizontal 3d wall is present in the columndepth chart")
        utillobj.verify_object_visible(wall2_css, True, "Step 11:12 : Verify background chart frame 3d wall is present in the columndepth chart")
        
        """
            Step 12 : Click "Advanced Chart" icon > Stacked Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "stackeddepth")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 21, MEDIUM_WAIT)
        
        utillobj.verify_object_visible(wall1_css, True, "Step 12:01 : Verify Vertical and Horizontal 3d wall is present in the stackeddepth chart")
        utillobj.verify_object_visible(wall2_css, True, "Step 12:02 : Verify background chart frame 3d wall is present in the stackeddepth chart")
        
        """
            Verify the Output
        """
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 12:03 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 12:04 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'venice_blue', parent_css="#"+PARENT_CSS, msg="Step 12:05 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 21, "Step 12:06 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 12:07 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 12:08 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 12:09 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 12:10 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST3, parent_css="#"+PARENT_CSS, msg="Step 12:11 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 12:12 :")
        
        """
            Step 13 : Click "Advanced Chart" icon > Percent Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "percentdepth")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 21, MEDIUM_WAIT)
        
        utillobj.verify_object_visible(wall1_css, True, "Step 13:01 : Verify Vertical and Horizontal 3d wall is present in the percentdepth chart")
        utillobj.verify_object_visible(wall2_css, True, "Step 13:02 : Verify background chart frame 3d wall is present in the percentdepth chart")
        
        """
            Verify the Output
        """
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 13:03 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 13:04 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'venice_blue', parent_css="#"+PARENT_CSS, msg="Step 13:05 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 21, "Step 13:06 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 13:07 : ")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 13:08 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 13:09 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 13:10 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST2, parent_css="#"+PARENT_CSS, msg="Step 13:11 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, msg="Step 13:12 :")
        
        """
            Step 14 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        
        

if __name__ == "__main__":
    unittest.main()