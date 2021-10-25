'''
Created on Aug 14, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287015
TestCase_Name : Verify to Run and Edit 'Average Discount Heatmap'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287015_TestClass(BaseTestCase):

    def test_C2287015(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = 'C2287015'
        short_wait = 2
        medium_wait= 30
        long_wait= 60
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Average_Discount_Heatmap'
        new_fex_name='Average Discount Heatmap1'
        reopen_fex_name= 'Average_Discount_Heatmap1'
        folder_name='Retail_Samples/Portal/Large_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Sale,Year', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'AVE.PercentDiscount', 'Multi-graph', 'Animate']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'pfjTableChart_2'
        total_riser_css= "[class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets&BIP_item=Average_Discount_Heatmap.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password)
        
        """
        Verify the output
        """
        chart_title_list= ['Product Category', 'Sale Year']
        expected_xval_list= ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_zval_list= ['2013', '2014', '2015', '2016', '2017', '2018']
        legend_list= ['AVE PercentDiscount', '4.2', '4.35', '4.5', '4.65', '4.8']
        preview_legend_list= ['AVE PercentDiscount', '1', '2', '3', '4', '5']
        expected_preview_xval_list= ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_preview_zval_list= ['2014']
        riser_css= "riser!s1!g2!mbar"
        preview_riser_css= "riser!s0!g2!mbar"
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_run_css, msg='Step02.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step02.2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step02.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step02.4')
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step02:5: Verify pie Legend List in run window')
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'banana_mania1', "Step02.6: Verify chart color")
        
        """
        Step03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step03: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
                
        """
        Step04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step05: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets/Average_Discount_Heatmap.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 7, long_wait)
        
        """
        Step06: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step06: Verify the Query panel in preview")
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_preview_css, msg='Step06.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step06.2: Verify number of riser segments in preview window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_preview_xval_list, "#"+chart_parent_preview_css, msg='Step06.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_preview_zval_list, "#"+chart_parent_preview_css, msg='Step06.4')
        chart_obj.verify_legends_in_preview(preview_legend_list, "#"+chart_parent_preview_css, msg="Step06:5:Verify legends in preview")
        chart_obj.verify_chart_color(chart_parent_preview_css, preview_riser_css, 'pale_green1', "Step06.6: Verify chart color")
        
        """
        Step07: Click Run inside IA tool
        Verify the output:
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_run_css, msg='Step07.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step07.2: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, "#"+chart_parent_run_css, msg='Step07.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_zval_list, "#"+chart_parent_run_css, msg='Step07.4')
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step07:5: Verify Legend List in run window')
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'banana_mania1', "Step07.6: Verify chart color")
        
        """
        Step08: Click IA > Save> Select "SmokeTest" folder > Enter title as "Average Discount Heatmap1" > Click Save
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
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Average_Discount_Heatmap1.fex&tool=Chart
        Verify it restored successfully without any error
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 7, long_wait)
        
        chart_obj.verify_x_axis_title_in_run_window(chart_title_list, "#"+chart_parent_preview_css, msg='Step10.1')
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step10.2: Verify number of riser segments in preview window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_run_window(expected_preview_xval_list, "#"+chart_parent_preview_css, msg='Step10.3')
        chart_obj.verify_z_axis_label_in_run_window(expected_preview_zval_list, "#"+chart_parent_preview_css, msg='Step10.4')
        chart_obj.verify_legends_in_preview(preview_legend_list, "#"+chart_parent_preview_css, msg="Step10:5:Verify legends in preview")
        chart_obj.verify_chart_color(chart_parent_preview_css, preview_riser_css, 'pale_green1', "Step10.6: Verify chart color")
        
        """
        Step11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()