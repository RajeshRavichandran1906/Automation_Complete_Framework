'''
Created on Aug 8, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667854
TestCase_Name : Verify to Run and Edit Discount by Region
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6667854_TestClass(BaseTestCase):

    def test_C6667854(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 60
        long_wait= 240
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Discount_by_Region'
        new_fex_name='Discount by Region1'
        reopen_fex_name= 'Discount_by_Region1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Store,Business,Region', 'Horizontal Axis', 'Sale,Quarter', 'Marker', 'Color', 'AVE.Discount', 'Multi-graph', 'Animate']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'pfjTableChart_2'
        total_riser_css= "svg g>rect[class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Discount_by_Region.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password)
        
        """
        Step03: Hover over anywhere on Heatmap, Verify the tooltip
        """
        chart_title_list= ['Sale Quarter', 'Store Region']
        expected_xval_list= ['1', '2', '3', '4']
        expected_zval_list= ['EMEA', 'North America', 'Oceania', 'South America']
        expected_preview_xval_list= ['1']
        expected_preview_zval_list= ['North America']
        riser_css= "riser!s1!g1!mbar"
        first_riser_css= "riser!s0!g0!mbar"
        expected_tooltip_list= ['AVE Discount:$19.70', 'Store Region:North America', 'Sale Quarter:2']
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_run_css, msg='Step03.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 16, "Step03.2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step03.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step03.4')
        chart_obj.verify_tooltip_in_run_window(riser_css, expected_tooltip_list, "Step03.5", "#"+chart_parent_run_css, move_to_tooltip=True)
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'reef1', "Step03.6: Verify chart color")
        
        """
        Step04: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 16, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 16, "Step04: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 16, medium_wait)
                
        """
        Step05: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step06: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Discount_by_Region.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 1, long_wait)
        
        """
        Step07: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step07: Verify the Query panel in preview")
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_preview_css, msg='Step07.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step07.2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_preview_xval_list, "#"+chart_parent_preview_css, msg='Step07.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_preview_zval_list, "#"+chart_parent_preview_css, msg='Step07.4')
        chart_obj.verify_chart_color(chart_parent_preview_css, first_riser_css, 'sandy_brown1', "Step07.5: Verify chart color")
        
        """
        Step08: Click Run inside IA tool
        Verify the output:
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 16, medium_wait)
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_run_css, msg='Step08.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 16, "Step08.2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step08.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step08.4')
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'reef1', "Step08.5: Verify chart color")
        
        """
        Step09: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Discount by Region1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, long_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step10: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step11: Edit the Report using "rsadv" user
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Discount_by_Region1.fex&tool=Chart
        Verify it restored successfully without any error
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 1, long_wait)
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_preview_css, msg='Step11.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step11.2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_preview_xval_list, "#"+chart_parent_preview_css, msg='Step11.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_preview_zval_list, "#"+chart_parent_preview_css, msg='Step11.4')
        chart_obj.verify_chart_color(chart_parent_preview_css, first_riser_css, 'sandy_brown1', "Step11.5: Verify chart color")
        
        """
        Step12: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()