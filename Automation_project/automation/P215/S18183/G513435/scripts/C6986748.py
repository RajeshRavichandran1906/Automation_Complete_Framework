'''
Created on Oct 24, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6986748&group_by=cases:section_id&group_order=asc&group_id=513435
Testcase Name : Verifyto Run and Edit 'Scatter Matrix - Profit vs Cogs' 
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6986748_TestClass(BaseTestCase):

    def test_C6986748(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 60
        LONG_WAIT= 240
        USERNAME= 'mrid'
        PASSWORD= 'mrpass'
        FEX_NAME='Scatter_Matrix_Profit_vs_Cogs'
        NEW_FEX_NAME='Scatter_Matrix_Profit_vs_Cogs1'
        REOPEN_FEX_NAME='Scatter_Matrix_Profit_vs_Cogs1'
        FOLDER_NAME="Retail_Samples/Charts"
        FEX_FOLDER_AFTER_SAVE='SmokeTest/~rsadv'
        
        EXPECTED_XAXIS_LABEL_LIST=['0', '1,500', '3,000', '4,500', '', '0', '1,500', '3,000', '4,500', '', '0', '1,500', '3,000', '4,500', '', '0', '1,500', '3,000', '4,500', '']
        EXPECTED_YAXIS_LABEL_LIST=['-200', '450', '1,100', '1,750', '', '-200', '450', '1,100', '1,750', '', '-200', '450', '1,100', '1,750', '', '-200', '450', '1,100', '1,750', '']
        CHART_XAXIS_TITLE=['AVE Cost of Goods', 'AVE Cost of Goods', 'AVE Cost of Goods', 'AVE Cost of Goods']
        CHART_YAXIS_TITLE=['AVE Gross Profit', 'AVE Gross Profit', 'AVE Gross Profit', 'AVE Gross Profit']
        EXPECTED_ROWVAL_LIST=['Sale Quarter', '1', '2', '3', '4']
        EXPECTED_COLVAL_LIST=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        EXPECTED_CHART_TITLE="Scatter Matrix - Average Profit vs Average COG"
        EXPECTED_LEGEND_LIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'AVE Revenue', '6,798', '28']
        EXPECTED_TOOLTIP_LIST=['Sale Quarter:1', 'Store Business Region:EMEA', 'AVE Cost of Goods:$4,214.29', 'AVE Gross Profit:$1,207.22', 'AVE Revenue:$5,421.50', 'Product Category:Camcorder', 'Model:Sony HXRNX5U']
        
        QUERY_FIELD_LIST=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Sale,Quarter', 'Columns', 'Store,Business,Region', 'Axis', 'Vertical Axis', 'AVE.Gross Profit', 'Horizontal Axis', 'AVE.Cost of Goods', 'Marker', 'Size', 'AVE.Revenue', 'Detail', 'Model', 'Color BY', 'Product,Category', 'Tooltip', 'Multi-graph', 'Animate']
        PREVIEW_EXPECTED_XAXIS_LABEL_LIST=['0', '875', '1,750', '2,625', '']
        PREVIEW_EXPECTED_YAXIS_LABEL_LIST=['-200', '50', '300', '550', '']
        PREVIEW_EXPECTED_ROWVAL_LIST=['Sale Quarter', '1']
        PREVIEW_EXPECTED_COLVAL_LIST=['Store Business Region', 'North America']
        PREVIEW_EXPECTED_LEGEND_LIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'AVE Revenue', '4,000', '2,014.5', '29']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        RUN_PARENT_CSS= 'jschart_HOLD_0'
        PREVIEW_PARENT_CSS= 'pfjTableChart_1'
        APPLICATION_CSS= '#applicationButton'
        RISER_CSS="[class='riser!s0!g11!mmarker!r0!c2!']"
        TOTAL_CIRCLE_CSS="#"+RUN_PARENT_CSS+" circle[class^='riser']"
        PREVIEW_TOTAL_CIRCLE_CSS="#"+PREVIEW_PARENT_CSS+" circle[class^='riser']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1:Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 2:Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Scatter_Matrix_Profit_vs_Cogs.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USERNAME, mrpass=PASSWORD, run_chart_css=TOTAL_CIRCLE_CSS, no_of_element=2185)    
             
        """    
            Step 3:Verify the following Scatter Matrix Chart
        """
        chart_obj.verify_x_axis_title_in_run_window(CHART_XAXIS_TITLE, msg='Step 03:01:')
        chart_obj.verify_y_axis_title_in_run_window(CHART_YAXIS_TITLE, msg='Step 03:02:')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 2185, "Step 03:03: Verify number of riser segments in run window")
        chart_obj.verify_x_axis_label_in_run_window(EXPECTED_XAXIS_LABEL_LIST, parent_css="#"+RUN_PARENT_CSS, msg='Step 03:04:')
        chart_obj.verify_y_axis_label_in_run_window(EXPECTED_YAXIS_LABEL_LIST, parent_css="#"+RUN_PARENT_CSS, msg='Step 03:05:')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_PARENT_CSS, msg="Step 03:06:")
        chart_obj.verify_rows_label(EXPECTED_ROWVAL_LIST, "#"+RUN_PARENT_CSS, msg='Step 03:07:')
        chart_obj.verify_column_label(EXPECTED_COLVAL_LIST, "#"+RUN_PARENT_CSS, msg='Step 03:08:')
        chart_obj.verify_chart_title(EXPECTED_CHART_TITLE, 'run', "Step 03:09: Verify chart title")
        chart_obj.verify_number_of_circles_in_run_window(0, 2186, "Step 03:10: Verify number of circles in runwindow", parent_css="#"+RUN_PARENT_CSS)
        chart_obj.verify_legends_in_run_window(EXPECTED_LEGEND_LIST, parent_css="#"+RUN_PARENT_CSS, msg="Step 03:11:", legend_length=10)  
            
        """   
            Step 4:Hover over any points, Verify the tooltip
        """ 
        TOOLTIP_RISER_CSS='riser!s1!g13!mmarker!r0!c0!'
        chart_obj.verify_tooltip_in_run_window(TOOLTIP_RISER_CSS, EXPECTED_TOOLTIP_LIST, "Step 04:01: Verify tooltip", parent_css="#"+RUN_PARENT_CSS)   
            
        """   
            Step 5:Resize the browser window and verify it does not throws any error message and then maximize the browser window
        """    
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(TOTAL_CIRCLE_CSS, 2185, MEDIUM_WAIT)
        chart_obj.verify_number_of_circles_in_run_window(0, 2186, "Step 05:01: Verify number of circles in runwindow", parent_css="#"+RUN_PARENT_CSS)
        chart_obj.maximize_browser()
          
        """    
            Step 6:Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
             
        """    
            Step 7:Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Scatter_Matrix_Profit_vs_Cogs.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(FOLDER_NAME, fex_name=FEX_NAME, mrid=USERNAME, mrpass=PASSWORD)   
        chart_obj.wait_for_number_of_element(PREVIEW_TOTAL_CIRCLE_CSS, 62, LONG_WAIT)
            
        """    
            Step 8:Verify the following Query panel and Scatter chart in Live Preview
        """    
        PREVIEW_RISER_CSS="[class='riser!s0!g2!mmarker!r0!c0!']"
        chart_obj.verify_all_fields_in_query_pane(QUERY_FIELD_LIST, "Step 08:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_title_in_preview(CHART_XAXIS_TITLE, msg='Step 08:02:')
        chart_obj.verify_y_axis_title_in_preview(CHART_YAXIS_TITLE, msg='Step 08:03:')
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS, 62, "Step 08:04: Verify number of riser segments in run window", custom_css=".chartPanel circle[class^='riser']")
        chart_obj.verify_x_axis_label_in_preview(PREVIEW_EXPECTED_XAXIS_LABEL_LIST, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 08:05:')
        chart_obj.verify_y_axis_label_in_preview(PREVIEW_EXPECTED_YAXIS_LABEL_LIST, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 08:06:')
        chart_obj.verify_chart_color_using_get_css_property_in_preview(PREVIEW_RISER_CSS, 'bar_blue', parent_css="#"+PREVIEW_PARENT_CSS, msg="Step 08:07:")
        chart_obj.verify_rows_label(PREVIEW_EXPECTED_ROWVAL_LIST, "#"+PREVIEW_PARENT_CSS, msg='Step 08:08:')
        chart_obj.verify_column_label(PREVIEW_EXPECTED_COLVAL_LIST, "#"+PREVIEW_PARENT_CSS, msg='Step 08:09:')
        chart_obj.verify_chart_title(EXPECTED_CHART_TITLE, 'preview', "Step 08:10: Verify chart title")
        chart_obj.verify_number_of_circles_in_run_window(0, 63, "Step 08:11: Verify number of circles in runwindow", parent_css="#"+PREVIEW_PARENT_CSS)
        chart_obj.verify_legends_in_preview(PREVIEW_EXPECTED_LEGEND_LIST, parent_css="#"+PREVIEW_PARENT_CSS, msg="Step 08:12:", legend_length=10)
          
        """    
            Step 09:Click Run, Verify the output
        """   
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        CIRCLE_CSS="circle[class^='riser']"
        chart_obj.wait_for_number_of_element(CIRCLE_CSS, 2185, LONG_WAIT)
        
        LEGEND_LIST1=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'AVE Revenue', '6,798', '28']
        
        chart_obj.verify_x_axis_title_in_run_window(CHART_XAXIS_TITLE, msg='Step 09:01:')
        chart_obj.verify_y_axis_title_in_run_window(CHART_YAXIS_TITLE, msg='Step 09:02:')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 2185, "Step 09:03: Verify number of riser segments in run window")
        chart_obj.verify_x_axis_label_in_run_window(EXPECTED_XAXIS_LABEL_LIST, parent_css="#"+RUN_PARENT_CSS, msg='Step 09:04:')
        chart_obj.verify_y_axis_label_in_run_window(EXPECTED_YAXIS_LABEL_LIST, parent_css="#"+RUN_PARENT_CSS, msg='Step 09:05:')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_PARENT_CSS, msg="Step 09:06:")
        chart_obj.verify_rows_label(EXPECTED_ROWVAL_LIST, "#"+RUN_PARENT_CSS, msg='Step 09:07:')
        chart_obj.verify_column_label(EXPECTED_COLVAL_LIST, "#"+RUN_PARENT_CSS, msg='Step 09:08:')
        chart_obj.verify_chart_title(EXPECTED_CHART_TITLE, 'run', "Step 09:09: Verify chart title")
        chart_obj.verify_number_of_circles_in_run_window(0, 2186, "Step 09:10: Verify number of circles in runwindow", parent_css="#"+RUN_PARENT_CSS)
        chart_obj.verify_legends_in_run_window(LEGEND_LIST1, parent_css="#"+RUN_PARENT_CSS, msg="Step 09:11:")  
        
        """   
            Step 10:Click IA > Save As> Select "SmokeTest" > My Content folder > Enter title as "Scatter Matrix - Profit vs Cogs1" > Click Save
        """    
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(APPLICATION_CSS, 1, MEDIUM_WAIT)
        chart_obj.save_as_from_application_menu_item(NEW_FEX_NAME)
            
        """   
            Step 11:Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()    
             
        """   
            Step 12:Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Scatter_Matrix_Profit_vs_Cogs1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(FEX_FOLDER_AFTER_SAVE, fex_name=REOPEN_FEX_NAME, mrid=USERNAME, mrpass=PASSWORD)   
        chart_obj.wait_for_number_of_element(PREVIEW_TOTAL_CIRCLE_CSS, 62, LONG_WAIT)
        
        chart_obj.verify_all_fields_in_query_pane(QUERY_FIELD_LIST, "Step 12:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_title_in_preview(CHART_XAXIS_TITLE, msg='Step 12:02:')
        chart_obj.verify_y_axis_title_in_preview(CHART_YAXIS_TITLE, msg='Step 12:03:')
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS, 62, "Step 12:04: Verify number of riser segments in run window", custom_css=".chartPanel circle[class^='riser']")
        chart_obj.verify_x_axis_label_in_preview(PREVIEW_EXPECTED_XAXIS_LABEL_LIST, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 12:05:')
        chart_obj.verify_y_axis_label_in_preview(PREVIEW_EXPECTED_YAXIS_LABEL_LIST, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 12:06:')
        chart_obj.verify_chart_color_using_get_css_property_in_preview(PREVIEW_RISER_CSS, 'bar_blue', parent_css="#"+PREVIEW_PARENT_CSS, msg="Step 12:07:")
        chart_obj.verify_rows_label(PREVIEW_EXPECTED_ROWVAL_LIST, "#"+PREVIEW_PARENT_CSS, msg='Step 12:08:')
        chart_obj.verify_column_label(PREVIEW_EXPECTED_COLVAL_LIST, "#"+PREVIEW_PARENT_CSS, msg='Step 12:09:')
        chart_obj.verify_chart_title(EXPECTED_CHART_TITLE, 'preview', "Step 12:10: Verify chart title")
        chart_obj.verify_number_of_circles_in_run_window(0, 63, "Step 12:11: Verify number of circles in runwindow", parent_css="#"+PREVIEW_PARENT_CSS)
        chart_obj.verify_legends_in_preview(PREVIEW_EXPECTED_LEGEND_LIST, parent_css="#"+PREVIEW_PARENT_CSS, msg="Step 12:12:", legend_length=10)
           
        """   
            Step 13:Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()