'''
Created on Jul 10, 2018

@author: KS13172
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2275842&group_by=cases:section_id&group_order=asc&group_id=170568
TestCase_Name : Verify to Run and Edit 'Top Ten Stores'
'''
import unittest, time
from common.wftools import report, chart
from common.lib.basetestcase import BaseTestCase

class C2275843_TestClass(BaseTestCase):

    def test_C2275843(self):
        
        driver = self.driver
        report_obj=report.Report(driver)
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = "C2275843"
        short_wait = 2
        medium_wait = 30
        long_wait = 60
        username = 'mrid'
        password = 'mrpass'
        fex_name="Top_Ten_Stores"
        new_fex_name="Top_Ten_Stores1"
        folder_name="Retail_Samples/Reports/Auto_Link"
        fex_folder_after_save="SmokeTest/~rsadv"
        autolink_tooltip = ['Auto LinksGauge - Gross Profit by Sale YearReport - Store Product Metrics']
        totalLabel=['$1M', '$1M']
        groupLabel=['2015','2016']
        gaugelabels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '1.6M', '0', '0.4M', '0.8M', '1.2M', '1.6M', '1.6M']
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'Quantity,Sold', 'By', 'Quantity,Sold', 'RANK', 'Store Name', 'Across']
        filter_field_name = "Model Equal to Optional Simple Parameter (Name: MODEL)"
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        rank_css = "table[summary='Summary'] td.x5:nth-child(1)"
        table_hyperlink_css = "table[summary='Summary'] > tbody > tr:nth-child(4) > td:nth-child(2) a"
        table_css = "table[summary='Summary'] > tbody > tr:nth-child(3) > td:nth-child(1)"
        chart_title_css="#jschart_HOLD_0.chart text.title"
        color_css1="path.gaugeRange:nth-child(1)"
        color_css3="path.gaugeRange:nth-child(3)"
        color_css5="path.gaugeRange:nth-child(5)"
        preview_title_css="#TableChart_1 span"
        bg_css ="[id*='DockPanel'] [id*='BiLabel'] div[style*='top:52pt']"
        iframe_css="#resultArea [id^=ReportIframe-]"
        application_css="#applicationButton"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01 : Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02 : Run the Report using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS/WFC/Repository/Retail_Samples/Reports/Auto_Link&BIP_item=Top_Ten_Stores.fex
        """        
        report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password)
#         report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, home_page='old')
        
        """
        Step 03 :Verify the output
        Verify the output with Hyperlink 
        Verify the background color for Rank 
        Verify first row value of the Report output
        """
        report_obj.wait_for_visible_text(rank_css, "RANK", long_wait)
        report_obj.verify_table_cell_property(4, 2, table_hyperlink_css, underline=True, msg="Step03.1: Verify output text Web with hyperlink")
        report_obj.verify_table_cell_property(3, 1, table_css, bg_color='dim_gray', font_color='white', text_value='RANK',msg="Step03.2: Verify background color for Rank")
#         report_obj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Step03_Ds01.xlsx", desired_no_of_rows=4)
        report_obj.verify_table_data_set(None, Test_Case_ID+"_Step03_Ds01.xlsx", msg="Step03.3:Verify first row value of the Report output", desired_no_of_rows=4)
        
        """
        Step04: Click on "London" Hyperlink
        Verify the Auto link and hover over on Menu
        Step05: Verify the following Auto link menus are displayed
        Step06: Click "Gauge-Gross Profit by Sale Year"
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary= 'Summary']", 5,2, "Auto Links->Gauge - Gross Profit by Sale Year", verify_tooltip=autolink_tooltip, msg="Step05: Verify Auto link menus are displayed", verify_type='asin')
        
        """
        Step07: Verify the following Gauge chart is displayed
        """
        time.sleep(short_wait)
        report_obj.switch_to_new_window()
        chart_obj.wait_for_visible_text(chart_title_css, "Gross Profit Year to YearLondon", medium_wait)
        chart_obj.verify_chart_title("Gross Profit Year to YearLondon", 'run', "Step07.01: Verify chart title in run window")
        chart_obj.verify_data_labels('jschart_HOLD_0',totalLabel,'Step 07:02: Verify total_labels',custom_css=".chartPanel text[class^='totalLabel']")
        chart_obj.verify_data_labels('jschart_HOLD_0',groupLabel,'Step 07:03: Verify labels',custom_css=".chartPanel text[class^='groupLabel']")
        chart_obj.verify_data_labels('jschart_HOLD_0',gaugelabels,'Step 07:04: Verify labels',custom_css=".chartPanel g text[transform*='rotate']")
         
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 07:05: verify the Gauge range", custom_css=".chartPanel path[class*='gaugeRange']")
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 2, "Step 07:06: verify the needle", custom_css=".chartPanel path[class*='needle']")
        
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mneedle", "cerulean_blue", "Step07:07: Verify needle blue color")
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'pink', 'Step07:08.1: Verify Gauge pink color',custom_css=color_css1)
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'yellow1', 'Step07:08.2: Verify Gauge yellow1 color',custom_css=color_css3)
        chart_obj.verify_chart_color('jschart_HOLD_0',None, 'lime', 'Step07:08.3: Verify Gauge lime color',custom_css=color_css5)
        time.sleep(short_wait)        
        
        """
        Step08: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_visible_text(chart_title_css, "Gross Profit Year to YearLondon", medium_wait)
        chart_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, "Step 08: verify the Gauge range", custom_css=".chartPanel path[class*='gaugeRange']")
        report_obj.maximize_browser()
        chart_obj.wait_for_visible_text(chart_title_css, "Gross Profit Year to YearLondon", medium_wait)
        report_obj.switch_to_previous_window()
        report_obj.wait_for_visible_text(rank_css, "RANK", long_wait)
                
        """
        Step09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
        Step10: Edit the Report using "rsadv" user
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Reports/Auto_Link/Top_Ten_Stores.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(folder_name, 'Report', fex_name, mrid=username, mrpass=password)
        report_obj.wait_for_visible_text(preview_title_css, "Top Ten Stores MODEL", long_wait)
        """
        Step11: Verify the Report launched in IA tool
        Verify the Query panel,Filter Pane and Live Preview
        Verify the background color for Rank
        """        
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step11.2.1: Verify the Query panel")
        report_obj.verify_filter_pane_field(filter_field_name, 1, "Step11.2.2: Verify the filter panel")
        report_obj.verify_report_preview_cell_background(bg_css, 'dim_gray', "Step11.2.3: Verification of preview Cell Background color.")
        
#         report_obj.create_acrossreport_data_set_in_preview("TableChart_1", 2, 2, 10, 2, Test_Case_ID+"Step11_Ds01.xlsx")
        report_obj.verify_across_report_data_set_in_preview("TableChart_1", 2,3,2,3, Test_Case_ID+"_Step11_Ds01.xlsx", "Step 11:03: Verify the created across dataset in preview")
        
        
        """
        Step12: Click Run inside IA tool
        Verify the output with Hyperlink 
        Verify the background color for Rank 
        Verify first row value of the Report output
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text(rank_css, "RANK", long_wait)
        report_obj.verify_table_cell_property(4, 2, table_hyperlink_css, underline=True, msg="Step12.1: Verify output text Web with hyperlink")
        report_obj.verify_table_cell_property(3, 1, table_css, bg_color='dim_gray', font_color='white', text_value='RANK',msg="Step12.2: Verify background color for Rank")
        report_obj.verify_table_data_set(None, Test_Case_ID+"_Step03_Ds01.xlsx", msg="Step12.3: Verify first row value of the Report output", desired_no_of_rows=4)
        
        """
        Step13: Click IA > Save> Select 'SmokeTest folder' > Enter title as "Top Ten Stores1" > Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.wait_for_number_of_element(application_css, 1, long_wait)
        report_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step14: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
        Step15: Edit the Report using "rsadv" user
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Top_Ten_Stores1.fex&tool=Report
        Verify it restored successfully without any error
        """
        report_obj.edit_fex_using_api_url(fex_folder_after_save, 'Report', new_fex_name, mrid=username, mrpass=password)
        report_obj.wait_for_visible_text(preview_title_css, "Top Ten Stores MODEL", long_wait)
        report_obj.verify_across_report_data_set_in_preview("TableChart_1", 2,3,2,3, Test_Case_ID+"_Step11_Ds01.xlsx", "Step15: Verify report restored successfully")

        """
        Step16: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()