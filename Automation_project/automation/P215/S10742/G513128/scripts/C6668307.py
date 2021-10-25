'''
Created on Aug 17, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6668307
TestCase_Name : Verify to Run and Edit Store Sales by Region
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6668307_TestClass(BaseTestCase):

    def test_C6668307(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
       
        medium_wait= 50
        long_wait= 240
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Store_Sales_by_Region'
        new_fex_name='Store Sales by Region1'
        reopen_fex_name= 'Store_Sales_by_Region1'
        folder_name='Retail_Samples/Portal/Large_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        query_field_list= ['Chart (wf_retail_lite)', 'Location', 'Layer', 'Store,Address,GIS Point', 'Marker', 'Size', 'Revenue', 'Color BY', 'Store,Business,Region', 'Tooltip', 'Multi-graph']
        legend_title= ['Store Business Region']
        legend_list= ['EMEA', 'North America', 'Oceania', 'South America']
        preview_legend_list= ['North America']
        sizelegend_title= ['Revenue']
        sizelegend_list= ['327.8M', '164M']
        preview_sizelegend_list= ['65,823']
        run_map_scale=['4000km', '2000mi']
        preview_run_map_scale=['4000km', '2000mi']
        riser_css= "riser!s1!g4!mregion"
        preview_riser_css= "riser!s0!g0!mregion"
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        parent_run_css= 'jschart_HOLD_0'
        parent_preview_css= 'pfjTableChart_2'
        total_riser_css= "[class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        no_of_circles="#"+parent_run_css+" "+total_riser_css
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets&BIP_item=Store_Sales_by_Region.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,run_chart_css=no_of_circles, no_of_element=86)
        
        """
        Verify the output
        """
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, legend_title, 'Step02.1. Verify Legend title', custom_css="[class*='legend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, legend_list, 'Step02.2: Verify Legend List', custom_css="[class*='legend-labels']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, sizelegend_title, 'Step02.3: Verify Size Legend title', custom_css="[class*='sizeLegend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, sizelegend_list, 'Step02.4: Verify Size Legend List', custom_css="[class*='sizeLegend-labels']", same_group=True)
        chart_obj.verify_map_scale_in_run_window(parent_run_css, run_map_scale, 'Step02.5: Verify map scale', custom_css=".esriScalebarLabel")
        chart_obj.verify_chart_color(parent_run_css, riser_css, 'pale_green', 'Step02.6: Verify map color')
        chart_obj.verify_number_of_circles_in_run_window(86,87,"Step02.7: Verify number of circles", "#"+parent_run_css)
        
        """
        Step03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 86, medium_wait)
        chart_obj.verify_number_of_circles_in_run_window(86,87,"Step03: Verify number of circles", "#"+parent_run_css)
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 86, medium_wait)
                
        """
        Step04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step05: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets/Store_Sales_by_Region.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 1, long_wait)
        
        """
        Step06: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step06: Verify the Query panel in preview")
        
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, legend_title, 'Step06.1. Verify Legend title', custom_css="[class*='legend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, preview_legend_list, 'Step06.2: Verify Legend List', custom_css="[class*='legend-labels']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, sizelegend_title, 'Step06.3: Verify Size Legend title', custom_css="[class*='sizeLegend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, preview_sizelegend_list, 'Step06.4: Verify Size Legend List', custom_css="[class*='sizeLegend-labels']", same_group=True)
        chart_obj.verify_chart_color(parent_preview_css, preview_riser_css, 'bar_blue', 'Step06.5 Verify map color')
        chart_obj.verify_number_of_circles_in_run_window(1,2,"Step06.6: Verify number of circles", "#"+parent_preview_css)
        
        """
        Step07: Click Run inside IA tool
        Verify the output:
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 86, long_wait)
        chart_obj.wait_for_visible_text("[class*='sizeLegend-title']", "Revenue", medium_wait)
        
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, legend_title, 'Step07.1. Verify Legend title', custom_css="[class*='legend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, legend_list, 'Step07.2: Verify Legend List', custom_css="[class*='legend-labels']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, sizelegend_title, 'Step07.3: Verify Size Legend title', custom_css="[class*='sizeLegend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_run_css, sizelegend_list, 'Step07.4: Verify Size Legend List', custom_css="[class*='sizeLegend-labels']", same_group=True)
        chart_obj.verify_chart_color(parent_run_css, riser_css, 'pale_green', 'Step07.5: Verify map color')
        chart_obj.verify_number_of_circles_in_run_window(86,87,"Step07.6: Verify number of circles", "#"+parent_run_css)
        chart_obj.verify_map_scale_in_run_window(parent_run_css, preview_run_map_scale, 'Step07.8: Verify map scale', custom_css=".esriScalebarLabel")
        
        """
        Step08: Click IA > Save as> Select "SmokeTest" > My Content folder > Enter title as "Store Sales by Region1" > Click Save
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
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Store_Sales_by_Region1.fex&tool=Chart
        Verify it restored successfully without any error
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 1, long_wait)
        
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, legend_title, 'Step10.1. Verify Legend title', custom_css="[class*='legend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, preview_legend_list, 'Step10.2: Verify Legend List', custom_css="[class*='legend-labels']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, sizelegend_title, 'Step10.3: Verify Size Legend title', custom_css="[class*='sizeLegend-title']", same_group=True)
        chart_obj.verify_riser_pie_labels_and_legends(parent_preview_css, preview_sizelegend_list, 'Step10.4: Verify Size Legend List', custom_css="[class*='sizeLegend-labels']", same_group=True)
        chart_obj.verify_chart_color(parent_preview_css, preview_riser_css, 'bar_blue', 'Step10.5 Verify map color')
        chart_obj.verify_number_of_circles_in_run_window(1,2,"Step10.6: Verify number of circles", "#"+parent_preview_css)
        
        """
        Step11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()