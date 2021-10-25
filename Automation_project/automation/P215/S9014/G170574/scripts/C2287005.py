'''
Created on Aug 9, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287005
TestCase_Name : Verify to Run and Edit 'Average Cost v Sales'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287005_TestClass(BaseTestCase):

    def test_C2287005(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = 'C2287005'
        short_wait = 2
        medium_wait= 30
        long_wait= 60
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Average_Cost_v_Sales'
        new_fex_name='Average Cost v Sales1'
        reopen_fex_name= 'Average_Cost_v_Sales1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Revenue', 'Marker', 'Size', 'Detail', 'Product,Subcategory', 'Color BY', 'Product,Category', 'Tooltip', 'Multi-graph', 'Animate']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run= 'jschart_HOLD_0'
        chart_parent_run_css= '#jschart_HOLD_0'
        chart_parent_preview = 'pfjTableChart_2'
        chart_parent_preview_css = '#pfjTableChart_2'
        total_riser_css= "svg g>circle[class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Average_Cost_v_Sales.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password)
#         chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,home_page='old')
        
        """
        Verify the output:
        """
        chart_xaxis_title= ['Revenue']
        chart_yaxis_title= ['Gross Profit']
        expected_xval_list= ['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        expected_yval_list= ['0', '10M', '20M', '30M', '40M', '50M', '60M']
        preview_xval_list= ['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        preview_yval_list= ['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000']
        riser_css= 'riser!s3!g0!mmarker'
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, chart_parent_run_css, msg='Step02.1a')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, chart_parent_run_css, msg='Step02.1b')
        chart_obj.verify_number_of_circles_in_preview(chart_parent_run_css, 21,22, "Step02.2: Verify number of circles in run window")
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, chart_parent_run_css, msg='Step02.3')
        chart_obj.verify_y_axis_label_in_run_window(expected_yval_list, chart_parent_run_css, msg='Step02.4')
        chart_obj.verify_chart_color(chart_parent_run, riser_css, 'pale_yellow', "Step02.5: Verify chart color")
        
        """
        Step03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 21, medium_wait)
        chart_obj.verify_number_of_circles_in_preview(chart_parent_run_css, 21,22, "Step03.2: Verify number of circles in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 21, medium_wait)
                
        """
        Step04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step05: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Discount_by_Region.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 15, long_wait)
        
        """
        Step06: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step07: Verify the Query panel in preview")
        
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, chart_parent_preview_css, msg='Step06.1a')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, chart_parent_preview_css, msg='Step06.1b')
        chart_obj.verify_number_of_circles_in_preview(chart_parent_preview_css, 15,16, "Step06.2: Verify number of circles in run window")
        chart_obj.verify_x_axis_label_in_run_window(preview_xval_list, chart_parent_preview_css, msg='Step06.3')
        chart_obj.verify_y_axis_label_in_run_window(preview_yval_list, chart_parent_preview_css, msg='Step06.4')
        chart_obj.verify_chart_color(chart_parent_preview, riser_css, 'pale_yellow', "Step06.5: Verify chart color")

        """
        Step07: Click Run inside IA tool
        Verify the output:
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 21, medium_wait)
        
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, chart_parent_run_css, msg='Step07.1a')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, chart_parent_run_css, msg='Step07.1b')
        chart_obj.verify_number_of_circles_in_preview(chart_parent_run_css, 21,22, "Step07.2: Verify number of circles in run window")
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, chart_parent_run_css, msg='Step07.3')
        chart_obj.verify_y_axis_label_in_run_window(expected_yval_list, chart_parent_run_css, msg='Step07.4')
        chart_obj.verify_chart_color(chart_parent_run, riser_css, 'pale_yellow', "Step07.5: Verify chart color")
        
        """
        Step08: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as " Average Cost v Sales1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, long_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step10: Edit the Report using "rsadv" user
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Average_Cost_v_Sales.fex&tool=Chart
        Verify it restored successfully without any error
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 15, long_wait)
        
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, chart_parent_preview_css, msg='Step10.1a')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, chart_parent_preview_css, msg='Step10.1b')
        chart_obj.verify_number_of_circles_in_preview(chart_parent_preview_css, 15,16, "Step10.2: Verify number of circles in run window")
        chart_obj.verify_x_axis_label_in_run_window(preview_xval_list, chart_parent_preview_css, msg='Step10.3')
        chart_obj.verify_y_axis_label_in_run_window(preview_yval_list, chart_parent_preview_css, msg='Step10.4')
        chart_obj.verify_chart_color(chart_parent_preview, riser_css, 'pale_yellow', "Step10.5: Verify chart color")
        
        """
        Step11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()