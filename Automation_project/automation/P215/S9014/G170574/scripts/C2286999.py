'''
Created on Aug 3, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2286999&group_by=cases:section_id&group_id=170574&group_order=asc
TestCase_Name : Verify to Run and Edit Category Sales
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2286999_TestClass(BaseTestCase):

    def test_C2286999(self):
        
        "Test Case Objects"
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "Test Case Variables"
        medium_wait= 30
        long_wait= 60
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Category_Sales'
        new_fex_name='Category Sales1'
        reopen_fex_name= 'Category_Sales1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        pie_label= ['Revenue']
        pie_totallabel= ['1.1B']
        pie_totallabel_preview= ['94,233']
        pie_legend_list= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Metric', 'Measure', 'Revenue', 'Color', 'Product,Category', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'pfjTableChart_2'
        pie_label_css= "text[class*='pieLabel']"
        pie_segment_preview_css = "[class*='riser!s']"
        pie_totallabel_css= "text[class^='totalLabel!']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
                
        """
        Step01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Category_Sales.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password)
#         chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,home_page='old')
        
        """
        Verify the output:
        """
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, pie_label, "Step02.1:",custom_css=pie_label_css) 
        chart_obj.verify_legends_in_run_window(pie_legend_list, "#"+chart_parent_run_css, 5, 'Step02.2: Verify pie Legend List in run window')
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, pie_totallabel, "Step02.3: Verify pie total label values in run window",custom_css=pie_totallabel_css,same_group=True)
        chart_obj.verify_chart_color(chart_parent_run_css, "riser!s0!g0!mwedge", "bar_blue1", "Step02.4: Verify first pie segment color in run window")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 7, "Step02.5: Verify number of pie segments in run window")
        
        """
        Step03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(pie_totallabel_css, 1, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 7, "Step03: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(pie_totallabel_css, 1, medium_wait)
                
        """
        Step04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step05: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Category_Sales.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(pie_totallabel_css, 1, long_wait)
        """
        Step06: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step06: Verify the Query panel in preview")
        
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_preview_css, pie_label, "Step06.1:",custom_css=pie_label_css) 
        chart_obj.verify_legends_in_run_window(pie_legend_list, "#"+chart_parent_preview_css, 5, 'Step06.2: Verify pie Legend List in preview')
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_preview_css, pie_totallabel_preview, "Step06.3: Verify pie total label values in preview",custom_css=pie_totallabel_css,same_group=True) 
        chart_obj.verify_chart_color(chart_parent_preview_css, "riser!s0!g0!mwedge", "bar_blue1", "Step06.4: Verify first pie segment color in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step06.5: Verify number of pie segments in preview", custom_css=pie_segment_preview_css)
        
        """
        Step07: Click Run inside IA tool
        Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, long_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(pie_totallabel_css, 1, medium_wait)
        
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, pie_label, "Step07.1:",custom_css=pie_label_css) 
        chart_obj.verify_legends_in_run_window(pie_legend_list, "#"+chart_parent_run_css, 5, 'Step07.2: Verify pie Legend List in run window')
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_run_css, pie_totallabel, "Step07.3: Verify pie total label values in run window",custom_css=pie_totallabel_css,same_group=True)
        chart_obj.verify_chart_color(chart_parent_run_css, "riser!s0!g0!mwedge", "bar_blue1", "Step07.4: Verify first pie segment color in run window")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 7, "Step07.5: Verify number of pie segments in run window")
        
        """
        Step08: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Category Sales1" > Click Save
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
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/~rsadv/Category_Sales1.fex&tool=Chart
        Verify it restored successfully without any error
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(pie_totallabel_css, 1, long_wait)
        
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_preview_css, pie_label, "Step10.1:",custom_css=pie_label_css) 
        chart_obj.verify_legends_in_run_window(pie_legend_list, "#"+chart_parent_preview_css, 5, 'Step10.2: Verify pie Legend List in preview')
        chart_obj.verify_riser_pie_labels_and_legends(chart_parent_preview_css, pie_totallabel_preview, "Step10.3: Verify pie total label values in preview",custom_css=pie_totallabel_css,same_group=True) 
        chart_obj.verify_chart_color(chart_parent_preview_css, "riser!s0!g0!mwedge", "bar_blue1", "Step10.4: Verify first pie segment color in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step10.5: Verify number of pie segments in preview", custom_css=pie_segment_preview_css)
        
        """
        Step11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()