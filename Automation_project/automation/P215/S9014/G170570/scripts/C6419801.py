'''
Created on Sep 21, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6419801&group_by=cases:section_id&group_id=170570&group_order=asc
Testcase Name : Verify to check Advanced Chart tool for Pie- 'Sales by Region Dashboard - Pie chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart

class C6419801_TestClass(BaseTestCase):

    def test_C6419801(self):
        
        driver = self.driver
       
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        MEDIUM_WAIT= 70
        SHORT_WAIT=20
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
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        RINGPIE_LABEL_CSS="#"+PARENT_CSS+" [class^='totalLabel']"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        WALL1_WINDOW_CSS="wall1"
        WALL1_BAR_CSS="#"+WALL1_WINDOW_CSS+" #chticon_1_0_bar1"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsbas (basic user)
            http://machine:port/ibi_apps
            Step 02 : Run the Document using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=RINGPIE_LABEL_CSS, no_of_element=1)
        
        """
            Step 03 : Go to the Pie chart "Sales by Product Category"
        """
        RINGPIE_EXPECTED_TOTALLABEL1=['70.1M']
        chart_obj.verify_legends_in_run_window(RINGPIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 03:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 03:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS2, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 03:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS3, 'pale_yellow', parent_css="#"+PARENT_CSS, msg="Step 03:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_LABEL, "Step 03:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_TOTALLABEL1, "Step 03:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 03:07: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 03:08:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 03:09: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        
        """
            Step 04 : Click "Advanced Chart" icon
            Step 05 : Click "Advanced Chart" icon > Pie > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "piebevel")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        NO_OF_RISERS_WITHTAGNAME="#"+PARENT_CSS+" path[class*='riser']"
        PIE_EXPECTED_LEGENDLIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_legends_in_run_window(PIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 05:01:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 05:02: Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 05:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(RINGPIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!g']", msg='Step 05:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 1, "Step 05:07: Verify number of pie slicers")
        
        """
            Step 06 : Click "Advanced Chart" icon > Pie with Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "piewithdepth")
        chart_obj.wait_for_number_of_element("#"+PARENT_CSS+" [class*='riser']", 37, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        PIEDEPTH_EXPECTED_LEGEND_LIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_legends_in_run_window(PIEDEPTH_EXPECTED_LEGEND_LIST, parent_css="#"+PARENT_CSS, msg="Step 06:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 06:02:")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 37, "Step 06:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(RINGPIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!g']", msg='Step 06:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 06:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 5, "Step 06:07: Verify number of pie with depth")
        
        """
            Step 07 : Click "Advanced Chart" icon > Donut(Cylinder) > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "dountcylinder")
        chart_obj.wait_for_number_of_element("#"+PARENT_CSS+" [class*='riser']", 14, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        chart_obj.verify_legends_in_run_window(PIEDEPTH_EXPECTED_LEGEND_LIST, parent_css="#"+PARENT_CSS, msg="Step 07:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 07:02:")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 14, "Step 07:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(RINGPIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!g']", msg='Step 07:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 07:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 2, "Step 07:07: Verify number of donut cylinder")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_TOTALLABEL1, "Step 07:08: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True)
        
        """
            Step 08 : Click "Advanced Chart" icon > Donut with Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "dountwithDepth")
        DONUT_CSS="#"+PARENT_CSS+" [class*='riser']"
        chart_obj.wait_for_number_of_element(DONUT_CSS, 46, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        chart_obj.verify_legends_in_run_window(PIEDEPTH_EXPECTED_LEGEND_LIST, parent_css="#"+PARENT_CSS, msg="Step 08:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 08:02:")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 46, "Step 08:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(RINGPIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!g']", msg='Step 08:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 08:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 6, "Step 08:07: Verify number of donut cylinder")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_TOTALLABEL1, "Step 08:08: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True)
        
        """
            Step 09 : Click "Advanced Chart" icon > Donut > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "donutbevel")
        chart_obj.wait_for_number_of_element(DONUT_CSS, 7, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        chart_obj.verify_legends_in_run_window(RINGPIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 09:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 09:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS2, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 09:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS3, 'pale_yellow', parent_css="#"+PARENT_CSS, msg="Step 09:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_LABEL, "Step 09:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_TOTALLABEL1, "Step 09:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!g']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 09:07: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 09:08:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09:09: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        
        """
            Step 10 :  Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()