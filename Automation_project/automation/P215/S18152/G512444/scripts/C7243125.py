'''
Created on Jan 1, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2343329&group_by=cases:section_id&group_id=171399&group_order=asc
Testcase Name : Verify to Run and Edit 'Insight - Time Series for sales and profit'
'''
import unittest
import time
import re
from common.wftools import chart
from common.lib.basetestcasenocap import BaseTestCase
from common.lib import utillity
import uiautomation as a

class C7243125_TestClass(BaseTestCase):

    def test_C7243125(self):
        
        chart_obj=chart.Chart(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        fex_name="Insight_-_Time_Series_for_sales_and_profit"
        save_fex_name="Insight_-_Time_Series_for_sales_and_profit1"
        folder_name="Retail_Samples/Charts"
        folder_name_to_edit_after_save="SmokeTest/~rsadv"
        medium_wait=60
        long_wait=250
        short_wait=30
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="runbox_id"
        chart_parent_preview_css="TableChart_1"
        RISER_CSS1="#"+chart_parent_run_css+" path[class^='riser']"
        Y_AXIS_TITLE_CSS="text[class='y2axis-title']"
        LOG_SCALE_CSS="#"+chart_parent_run_css+" text[class='yaxis-labels!m3!']"
        total_riser_css_with_tagname=" path[class^='riser!']"
        preview_riser_css="#"+chart_parent_preview_css+total_riser_css_with_tagname
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 1:Sign to Webfocus using "rsadv" user
        http://machine:port/ibi_apps
        Step 2:Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Insight_-_Time_Series_for_sales_and_profit.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid="mrid", mrpass="mrpass", run_chart_css=RISER_CSS1, no_of_element=14)
 
        """
        Step 3:Verify the following "Insight Line chart"
        """
        
        expected_x_axis_labels=['2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3']
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        expected_y1_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Quantity Sold']
        expected_x_axis_title_list=['Sale Year/Quarter']
        
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 03.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 03.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 03.3: Verify xaxis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y1_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 03.4: Verify y1_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css=Y_AXIS_TITLE_CSS,msg="Step 03.5: Verify y1_axis title at runtime")
        parent_css_with_tag_name = "#"+chart_parent_run_css+ " path"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 2, msg="Step 03.6: Verify number of risers at runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!ay1!mline!']", 'bar_blue', parent_css="#"+chart_parent_run_css, attribute='stroke', msg="Step 03.7: Verify chart color")
        
        """
        Step 4:Hover over any line point, Verify the tooltip
        """
        riser_css="marker!s4!g16!ay1!mmarker!"
        expected_tooltip_list=['Sale Year/Quarter:2017 Q1', 'Gross Profit:$5,795,979.49', 'Product Category:Stereo Systems']
        chart_obj.verify_tooltip_in_run_window(riser_css, expected_tooltip_list, "Step 4:01:Verify tooltip valus", parent_css="#"+chart_parent_run_css,use_marker_enable=True)
        
        """
        Step 5:Click "More option" icon under bucket shelf > Select Export Image
        """
        chart_obj.select_header_option_item_in_insight(header_option_item='more_options')
        time.sleep(1)
        chart_obj.select_or_verify_more_option_menu_item_in_insight('Export Image')
        time.sleep(5)
         
        """
        Step 6:Verify image is downloaded
        Note: Download type will be differ for browsers
        """
        browser_name=utillobj.parseinitfile('browser')
        if browser_name == 'Chrome':
            cr_status=a.GroupControl(Name='Downloads bar').ButtonControl(RegexName='.*Insight - Time Series for sales and profit.*png').Exists()
            utillobj.asequal(True, cr_status, "Step 5:Verify image is downloaded")
        elif browser_name == 'Firefox':
            ff_status=a.EditControl(RegexName='.*Insight - Time Series for sales and profit.*png').Exists()
            utillobj.asequal(True, ff_status, "Step 5:Verify image is downloaded")
        else:
            e_status= bool(re.match('.*Insight - Time Series for sales and profit.*png', a.TextControl(Name='Notification bar Text').AccessibleCurrentValue()))
            utillobj.asequal(True, e_status, "Step 5:Verify image is downloaded")
            
        """
        Step 7:Click "More option" icon under bucket shelf > Select "Y-axis Log Scale"
        Verify Y-axis value is changed
        """
        time.sleep(1)
        chart_obj.select_header_option_item_in_insight(header_option_item='more_options')
        time.sleep(0.75)
        chart_obj.select_or_verify_more_option_menu_item_in_insight('Y-Axis Log Scale')
        time.sleep(60)
        chart_obj.wait_for_visible_text(LOG_SCALE_CSS, '100M ', medium_wait)
        expected_y_axis_labels1=['0.1M', '1M', '10M', '100M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels1, parent_css="#"+chart_parent_run_css, msg="Step 8: Verify y-axis label in runtime")

        """
        Step 8:Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels1, parent_css="#"+chart_parent_run_css, msg="Step 8: Verify y-axis label in runtime")
 
        """
        Step 9:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.maximize_browser()
        chart_obj.api_logout()
 
        """
        Step 10:Edit the Chart using "rsadv" with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Insight_-_Time_Series_for_sales_and_profit.fex&tool=Chart
        """
         
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M', '2.8M']
        preview_chart_x_axis_label=['2014 Q1']
        preview_chart_y_axis_label=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000']
        preview_chart_y2_axis_label=['0', '20', '40', '60', '80', '100']
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Quantity,Sold', 'Horizontal Axis', 'Sale,Year/Quarter', 'Marker', 'Color BY', 'Product,Category', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        filter_field='Product,Category Equal to Optional Multiselect Dynamic Parameter (Name: PRODUCT_CATEGORY, Field: PRODUCT_CATEGORY in retail_samples/WF_RETAIL_LITE) Sort Ascending'
        expected_y_axis_title_list=['Quantity Sold']
        riser_preview_css="[class*='risers']"
        chart_color_css="[class='marker!s0!g0!mmarker!']"
        
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid="mrid", mrpass="mrpass")
        chart_obj.wait_for_number_of_element(preview_riser_css, 14, long_wait)
        
        """
        Step 11:Verify the following Query panel,Filter pane and Line chart in Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 11:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, attribute='stroke', msg='Step 11:02: Verify chart color in preview')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 11:03: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 11:04: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "white", parent_css="#"+chart_parent_preview_css, msg="Step 11:05: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 11:06: Verify number of chart segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 11:07:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 11:08:Verify yaxis title in preview")
        chart_obj.verify_y_axis_title_in_preview(preview_chart_y2_axis_label, parent_css="#"+chart_parent_preview_css, x_or_y_axis_title_css="text[class*='y2axis-label']",msg="Step 1:09:Verify yaxis2 title in preview")
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 11:10: Verify filter pane field is available in filterbox")
        
        """
        Step 12:Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 14, medium_wait)
        
        expected_x_axis_labels=['2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3']
        expected_y_axis_labels=['0', '3M', '6M', '9M', '12M']
        expected_y1_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Quantity Sold']
        expected_x_axis_title_list=['Sale Year/Quarter']
        
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 12.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 12.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 12.3: Verify xaxis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y1_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 12.4: Verify y1_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css=Y_AXIS_TITLE_CSS,msg="Step 12.5: Verify y1_axis title at runtime")
        parent_css_with_tag_name = "#"+chart_parent_run_css+ " path"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 2, msg="Step 12.6: Verify number of risers at runtime")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!ay1!mline!']", 'bar_blue', parent_css="#"+chart_parent_run_css, attribute='stroke', msg="Step 12.7: Verify chart color")

        """
        Step 13:Click IA > Save > Select "SmokeTest" folder> Enter title as "Insight - Time Series for sales and profit1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, short_wait)
        chart_obj.save_as_from_application_menu_item(save_fex_name)
 
        """
        Step 14:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
 
        """
        Step 15:Edit the saved Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Insight_-_Time_Series_for_sales_and_profit1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name_to_edit_after_save, fex_name=save_fex_name, mrid='mrid', mrpass='mrpass')
        chart_obj.wait_for_number_of_element(preview_riser_css, 14, long_wait)
        
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M', '2.8M']
        preview_chart_x_axis_label=['2014 Q1']
        preview_chart_y_axis_label=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000']
        preview_chart_y2_axis_label=['0', '20', '40', '60', '80', '100']
        expected_y_axis_title_list=['Quantity Sold']
        riser_preview_css="[class*='risers']"
        chart_color_css="[class='marker!s0!g0!mmarker!']"
        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 15:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, attribute='stroke', msg='Step 15:2: Verify chart color in preview')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 15:03: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 15:04: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "white", parent_css="#"+chart_parent_preview_css, msg="Step 10:05: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 15:06: Verify number of chart segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 15:07:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 15:08:Verify yaxis title in preview")
        chart_obj.verify_y_axis_title_in_preview(preview_chart_y2_axis_label, parent_css="#"+chart_parent_preview_css, x_or_y_axis_title_css="text[class*='y2axis-label']",msg="Step 15:09:Verify yaxis2 title in preview")
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 15:10: Verify filter pane field is available in filterbox")
 
        """
        Step 16:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()
        