'''
Created on Sep 25, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6740521&group_by=cases:section_id&group_order=asc&group_id=171399
TestCase Name : Verifyto Run and Edit 'Treemap - Revenue and Average Margin for Models'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6740521_TestClass(BaseTestCase):

    def test_C6740521(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 90
        long_wait= 400
        username= 'mrid'
        password= 'mrpass'
        fex_name='Treemap_Revenue_and_Average_Margin_for_Models'
        new_fex_name='Treemap - Revenue and Average Margin for Models1'
        reopen_fex_after_save='Treemap_-_Revenue_and_Average_Margin_for_Models1'
        folder_name='Retail_Samples/Charts'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Group', 'Grouping', 'Product,Category', 'Model', 'Metric', 'Size', 'Revenue', 'Color', 'AVE.Margin', 'Tooltip', 'Multi-graph', 'Animate'] 
        expected_legend_list=['AVE Margin', '10.2', '50.3', '90.3', '130.4', '170.4']
        preview_expected_legend_list=['AVE Margin', '-6.5', '39.2', '84.9', '130.6', '176.2']
        
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Computers', 'Televisions', 'Video Production', 'BOSE AM10IV', 'ND8520', 'Pioneer HTZ-170', 'Onkyo SKSHT870', 'Harman Kardon HKTS30BQ', 'Onkyo SKSHT750B', 'Polk Audio RM705', 'Yamaha RXV465']
        expected_tooltip_list=['Product Category:Media Player', 'Model:Sony BDP-S370', 'Revenue:$12,226,985.31', 'AVE Margin:22.81']
        preivew_expected_labels=['Media Player', 'Stereo Systems', 'Camcorder', 'Televisions', 'Video Production', 'Accessories', 'Computers', 'Sony BDP-S370', 'Panasonic DMP-BD60', 'Panasonic DMP-BD70V', 'Panasonic DMP-BD80', 'JVC DR-MV150B', 'Samsung BD-P3600', 'SAMSUNG BD-C6500', 'Pioneer BDP-120']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_1'
        total_riser_css_with_tagname=" rect[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        preview_riser_css="#"+chart_parent_preview_css+total_riser_css_with_tagname
        riser_css='riser!sCamcorder-_-Sanyo VPCPD2BK!g0!mnode'
        tooltip_riser_css='riser!sMedia Player-_-Sony BDP-S370!g0!mnode'
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Treemap_Revenue_and_Average_Margin_for_Models.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,run_chart_css=total_riser_css_with_tagname, no_of_element=157)
         
        """
            Step 03 : Verify the following Treemap
        """
         
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 157, "Step 03:01: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'elf_green', "Step 03:02: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 03:03: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 03:04: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 157, 1, "Step 03:05: Verify number of risers")
         
        """
            Step 04 : Hover over on Treemap, Verify the tooltip
        """
        msg="Step 04: Verify tooltip values"
        chart_obj.verify_tooltip_in_run_window(tooltip_riser_css, expected_tooltip_list, msg=msg, parent_css="#"+chart_parent_run_css)
         
        """
           Step 05 : Resize the browser window and verify it does not throws any error message and then maximize the browser window 
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 157, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 157, "Step 05: Verify number of riser segments in run window", custom_css="[class^='riser!s']")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 157, medium_wait)
         
        """
            Step 06 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
            Step 07 :  Edit the Chart using the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Treemap_Revenue_and_Average_Margin_for_Models.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 79, long_wait)
        
        """
            Step 08 : Verify the following Query panel and Treemap in Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 08:01: Verify the Query panel in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 79, "Step 08:02: Verify number of riser segments in run window",custom_css=total_riser_css_with_tagname)
        chart_obj.verify_x_axis_label_in_preview(preivew_expected_labels, parent_css="#"+chart_parent_preview_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1, msg='Step 08:03 Verify preview x_axis label in preview')
        chart_obj.verify_chart_color(chart_parent_preview_css, riser_css, 'elf_green', "Step 08:04: Verify chart color")
        
        """
            Step 09 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 157, long_wait)
        
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 157, "Step 09:01: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'elf_green', "Step 09:02: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 09:03: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 09:04: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 157, 1, "Step 09:05: Verify number of risers")
        
        """
            Step 10 : Click IA > Save> Select "SmokeTest" > Mycontent folder > Enter title as "Treemap - Revenue and Average Margin for Models1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
            Step 11 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
            Step 12 : Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Treemap_-_Revenue_and_Average_Margin_for_Models1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_after_save, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 79, long_wait)
        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 12:01: Verify the Query panel in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 79, "Step 12:02: Verify number of riser segments in run window",custom_css=total_riser_css_with_tagname)
        chart_obj.verify_x_axis_label_in_preview(preivew_expected_labels, parent_css="#"+chart_parent_preview_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1, msg='Step 12:03 Verify preview x_axis label in preview')
        chart_obj.verify_chart_color(chart_parent_preview_css, riser_css, 'elf_green', "Step 12:04: Verify chart color")
        chart_obj.verify_legends_in_preview(preview_expected_legend_list, msg="Step 12:05: Verify legends in preview")
        
        """
            Step 13 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()