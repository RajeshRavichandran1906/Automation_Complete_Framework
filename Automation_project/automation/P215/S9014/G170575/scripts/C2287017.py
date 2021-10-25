'''
Created on Aug 14, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2287012&group_by=cases:section_id&group_id=170575&group_order=asc
Testcase Name : Verify to Run and Edit Store Sales by Region
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287017_TestClass(BaseTestCase):

    def test_C2287017(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 50
        long_wait= 300
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Units_Profit_Treemap'
        new_fex_name='Units_Profit_Treemap1'
        folder_name='Retail_Samples/Portal/Large_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Group', 'Grouping', 'Product,Category', 'Product,Subcategory', 'Metric', 'Size', 'Quantity,Sold', 'Color', 'Gross Profit', 'Tooltip', 'Multi-graph', 'Animate'] 
        expected_legend_list=['Gross Profit', '0.3M', '13.1M', '26M', '38.9M', '51.8M']
        expected_x_axis_labels=['Stereo Systems', 'Media Player', 'Accessories', 'Camcorder', 'Computers', 'Video Production', 'Televisions', 'Home Theater Systems', 'iPod Docking Station', 'Speaker Kits', 'Receivers', 'Boom Box', 'Blu Ray', 'Streaming', 'DVD Players', 'DVD Player...', 'Headphones', 'Universal Remote Controls', 'Charger', 'Handheld', 'Standard', 'Professional', 'Smartphone', 'Tablet', 'Video Editing', 'Flat Panel TV']
        preview_expected_labels=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Video Production', 'Computers', 'Televisions', 'Home Theater Systems', 'iPod Docking Station', 'Receivers', 'Speaker Kits', 'Blu Ray', 'DVD Players', 'Streaming', 'Standard', 'Handheld', 'Charger', 'Headphones', 'Universal R...', 'Video Editing', 'Smartphone', 'Flat Panel TV', 'Gross Profit']
        expected_tooltip_list=['Product Category:Media Player', 'Product Subcategory:Blu Ray', 'Quantity Sold:679,495', 'Gross Profit:$51,771,195.13']
#         visible_text="HomeTheaterSystems"
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_2'
        total_riser_css= "svg g>rect[class^='riser!s']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        riser_css='riser!sMedia Player-_-Blu Ray!g0!mnode'
#         visible_text_css="#"+chart_parent_run_css+".chart g.chartPanel g g text:nth-child(1)"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets&BIP_item=Units_Profit_Treemap.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css="#"+chart_parent_run_css+" "+total_riser_css,no_of_element=21)
        
        """
            Verify the output
        """
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 21, "Step 02:01: Verify number of riser segments in run window", custom_css=total_riser_css)
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'elf_green', "Step 02:02: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 02:03: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=2,msg="Step 02:04: Verify Treemap labels at runtime")
         
        """
        Step 03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 21, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 21, "Step 03: Verify number of riser segments in run window", custom_css=total_riser_css)
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 21, medium_wait)
                 
        """
        Step 04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 05: Edit the Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Large_Widgets/Units_Profit_Treemap.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 15, long_wait)
        
        """
        Step 06: Verify the Chart launched in IA tool
        Verify the following Query panel and Heatmap in Live Preview
        """        
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 06:01: Verify the Query panel in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 15, "Step 06:02: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_preview(preview_expected_labels, parent_css="#"+chart_parent_preview_css,  xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=6, msg='Step 06:03 Verify preview x_axis label in preview')
        chart_obj.verify_chart_color(chart_parent_preview_css, riser_css, 'elf_green', "Step 06:04: Verify chart color")
        
        """
        Step 07: Click Run, Hover anywhere on area chart verify tooltip
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 21, long_wait)
        chart_obj.verify_tooltip_in_run_window(riser_css, expected_tooltip_list, "Step 07:01:Verify tooltip at runtime", parent_css="#"+chart_parent_run_css)
        
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 21, "Step 07:02: Verify number of riser segments in run window", custom_css=total_riser_css)
        chart_obj.verify_chart_color(chart_parent_run_css, riser_css, 'elf_green', "Step 07:03: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 07:04: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 07:05: Verify Treemap labels at runtime")
        
        """
        Step 08: Click IA > Save as> Select "SmokeTest" > My Content folder > Enter title as "Units Profit Treemap1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 10: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Units_Profit_Treemap1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=new_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(total_riser_css, 15, long_wait)
        
        """
        Verify it restored successfully without any error
        """ 
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 10:01: Verify the Query panel in preview")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 15, "Step 10:02: Verify number of riser segments in run window",custom_css=total_riser_css)
        chart_obj.verify_x_axis_label_in_preview(preview_expected_labels, parent_css="#"+chart_parent_preview_css,  xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=6, msg='Step 10:03 Verify preview x_axis label in preview')
        chart_obj.verify_chart_color(chart_parent_preview_css, riser_css, 'elf_green', "Step 10:04: Verify chart color")
        
        """
        Step 11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''


if __name__ == "__main__":
    unittest.main()