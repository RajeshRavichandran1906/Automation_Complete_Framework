'''
Created on Jul 18, 2018

@author: BM13368
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667719&group_by=cases:section_id&group_id=512444&group_order=asc
TestCase_Name : Verify to Run and Edit 'Gross Profit by Sale Year'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6667719_TestClass(BaseTestCase):

    def test_C6667719(self):
        
        chart_obj=chart.Chart(self.driver)
        
        fex_name="Gross_Profit_by_Sale_Year"
        save_fex_name="Gross_Profit_by_Sale_Year1"
        folder_name="Retail_Samples/Charts/Autolink_Targets"
        folder_name_to_edit_after_save="SmokeTest/~rsadv"
        
        long_time=240
        medium_wait=60
        chart_title_text="Gross Profit Year to Year"
        application_css='#applicationButton'
        query_field_list=['Chart (wf_retail)', 'Measure (Sum)', 'Gross Profit', 'By', 'Sale,Year', 'Multi-graph']
        filter_field_name1 = "Sale,Year Equal to 2015 or 2016"
        filter_field_name2="Store Name Equal to Optional Simple Parameter (Name: STORE_NAME)"
        
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts/Autolink_Targets&BIP_item=Gross_Profit_by_Sale_Year.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid="mrid", mrpass="mrpass", run_chart_css="#jschart_HOLD_0.chart text.title")
           
        """ 
            Step 03 : Verify the following Gauge Chart
        """
        chart_obj.verify_chart_title(chart_title_text, 'run', "Step 03.01: Verify chart title in run window")
        totalLabel=['$25M','$36M']
        chart_obj.verify_data_labels('jschart_HOLD_0',totalLabel,'Step 03:02: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
           
        groupLabel=['2015','2016']
        chart_obj.verify_data_labels('jschart_HOLD_0',groupLabel,'Step 03:03: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
           
        gaugelabels=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M']
        chart_obj.verify_data_labels('jschart_HOLD_0',gaugelabels,'Step 03:04: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
           
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 03:05: verify the Gauge range", custom_css=".chartPanel path[class*='gaugeRange']")
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 2, "Step 03:06: verify the needle", custom_css=".chartPanel path[class*='needle']")
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mneedle", "cerulean_blue", "Step 03:07: Verify needle blue color")
           
        color_css1="path.gaugeRange:nth-child(1)"
        color_css3="path.gaugeRange:nth-child(3)"
        color_css5="path.gaugeRange:nth-child(5)"
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'pink', 'Step 03:08: Verify Gauge green color',custom_css=color_css1)
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'yellow1', 'Step 03:09: Verify Gauge green color',custom_css=color_css3)
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'lime', 'Step 03:10: Verify Gauge green color',custom_css=color_css5)
           
        """
            Step 04 : Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element("#jschart_HOLD_0.chart text.title", 1, medium_wait)
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 04: verify the Gaugerange", custom_css=".chartPanel path[class*='gaugeRange']")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element("#jschart_HOLD_0.chart text.title", 1, medium_wait)
         
        """
            Step 05 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
          
        """
            Step 06 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Autolink_Targets/Gross_Profit_by_Sale_Year.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid="mrid", mrpass="mrpass")
        css="#TableChart_1 [class='groupLabel!g0!mgroupLabel!']"
        visible_text="2015"
        chart_obj.wait_for_visible_text(css, visible_text, long_time)
        
        """
            Step 06 :Verify the following Query Pane,Filter Pane and Chart in Live Preview
        """
        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 06:01: Verify the Query panel")
        chart_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 06:02: Verify the filter panel")
        chart_obj.verify_filter_pane_field(filter_field_name2, 2, "Step 06:03: Verify the filter panel")
        
        expected_title="Gross Profit Year to YearSTORE_NAME"
        chart_obj.verify_chart_title(expected_title, 'preview', "Step 06:04:Verify preview chart title")
        
        """ Verify the Heading is center aligned """
        chart_obj.verify_chart_title_text_align('middle', 'preview', "Step 06:05:Verify chart title alignment")
        
        chart_obj.verify_data_labels('TableChart_1',['$0M'],'Step 06:06:: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        chart_obj.verify_data_labels('TableChart_1',['2015'],'Step 06:07: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        labels=['0', '20', '40', '60', '80', '100', '120']
        chart_obj.verify_data_labels('TableChart_1',labels,'Step 06:08: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
        chart_obj.verify_number_of_chart_segment('TableChart_1', 5, "Step 06:05: verify the Gauge", custom_css=".chartPanel path[class*='gaugeRange']")
        chart_obj.verify_number_of_chart_segment('TableChart_1', 1, "Step 06:06: verify the Gauge", custom_css=".chartPanel path[class*='needle']")
        
        """
            Step 07 :Click Run
            Verify the Chart run successfully 
            Verify the Heading is center aligned
        """
        chart_obj.run_chart_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        css="#jschart_HOLD_0 .title"
        chart_title_text="Gross Profit Year to Year"
        chart_obj.wait_for_visible_text(css, chart_title_text,long_time)
        
        chart_obj.verify_chart_title(chart_title_text, 'run', "Step 06:04:Verify preview chart title")
        
        chart_obj.verify_chart_title_text_align('middle', 'run', "Step 07:01:Verify chart title alignment")
        
        totalLabel=['$25M','$36M']
        chart_obj.verify_data_labels('jschart_HOLD_0',totalLabel,'Step 07:02: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
         
        groupLabel=['2015','2016']
        chart_obj.verify_data_labels('jschart_HOLD_0',groupLabel,'Step 07:03: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
         
        gaugelabels=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M']
        chart_obj.verify_data_labels('jschart_HOLD_0',gaugelabels,'Step 07:04: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
         
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 07:05: verify the Gauge range", custom_css=".chartPanel path[class*='gaugeRange']")
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 2, "Step 07:06: verify the needle", custom_css=".chartPanel path[class*='needle']")
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mneedle", "cerulean_blue", "Step 07:07: Verify needle blue color")
         
        color_css1="path.gaugeRange:nth-child(1)"
        color_css3="path.gaugeRange:nth-child(3)"
        color_css5="path.gaugeRange:nth-child(5)"
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'pink', 'Step 07:08: Verify Gauge green color',custom_css=color_css1)
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'yellow1', 'Step 07:09: Verify Gauge green color',custom_css=color_css3)
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'lime', 'Step 07:10: Verify Gauge green color',custom_css=color_css5)
        
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        
        """
            Step 08 : Click IA > Save > Select "SmokeTest" > MYContent folder > Enter title as "Gross_Profit_by_Sale_Year1" > Click Save
        """
        chart_obj.save_as_from_application_menu_item(save_fex_name)
        
        """
            Step 09 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
            Step 10 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Gross_Profit_by_Sale_Year1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name_to_edit_after_save, fex_name=save_fex_name, mrid="mrid", mrpass="mrpass")
        css="#TableChart_1 [class='groupLabel!g0!mgroupLabel!']"
        chart_obj.wait_for_visible_text(css, "2015", long_time)
        
        """
            Verify it restored successfully without any error
        """
        query_field_list=['Chart (wf_retail)', 'Measure (Sum)', 'Gross Profit', 'By', 'Sale,Year', 'Multi-graph']
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 10:01: Verify the Query panel")
        
        chart_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 10:02: Verify the filter panel")
        chart_obj.verify_filter_pane_field(filter_field_name2, 2, "Step 10:03: Verify the filter panel")
        
        expected_title="Gross Profit Year to YearSTORE_NAME"
        chart_obj.verify_chart_title(expected_title, 'preview', "Step 10:04:Verify preview chart title")
        
        """ Verify the Heading is center aligned """
        chart_obj.verify_chart_title_text_align('middle', 'preview', "Step 10:05:Verify chart title alignment")
        
        chart_obj.verify_data_labels('TableChart_1',['$0M'],'Step 10:06:: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        chart_obj.verify_data_labels('TableChart_1',['2015'],'Step 10:07: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        labels=['0', '20', '40', '60', '80', '100', '120']
        chart_obj.verify_data_labels('TableChart_1',labels,'Step 10:08: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
        chart_obj.verify_number_of_chart_segment('TableChart_1', 5, "Step 10:09: verify the Gauge", custom_css=".chartPanel path[class*='gaugeRange']")
        chart_obj.verify_number_of_chart_segment('TableChart_1', 1, "Step 10:10: verify the Gauge", custom_css=".chartPanel path[class*='needle']")
        
        """
            Step 11 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()