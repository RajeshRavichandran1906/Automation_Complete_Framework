'''
Created on Aug 24, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6417164&group_by=cases:section_id&group_order=asc&group_id=483978
Testcase Name : Verify to Run and Edit 'Enhanced_Accordion'
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase


class C6417164_TestClass(BaseTestCase):

    def test_C6417164(self):
        
        driver = self.driver
        report_obj = report.Report(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = 'C6417164'
        short_wait = 40
        medium_wait= 90
        long_wait=300
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Enhanced_Accordion'
        folder_name='Retail_Samples/Portal/Responsive_Tables'
        
        node_path="South America->Camcorder->Computers->Media Player"
        title_popup1="Store Business Region"
        title_popup2="Product Category"
        title_popup3="Subcategory"
        visble_text="North America"
        
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'Gross Profit', 'Discount', 'MSRP', 'Cost of Goods', 'Quantity,Sold', 'By', 'Store,Business,Region', 'Product,Category', 'Product,Subcategory', 'Across']
        filter_pane_field_value="Product,Subcategory Not equal to Home Theater Systems"
        expected_heading='Gross Profit  Discount  MSRP  COGS  Qty'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
       
        table_css="#treetable"
        row_val_css=table_css+".treetable > tbody > tr[data-tt-id='{0}'] td:nth-child({1})"
        camcorder_val_css=table_css+".treetable > tbody > tr[data-tt-id='{0}-{1}'] td:nth-child({2})"
        handheld_val_css=table_css+".treetable > tbody > tr[data-tt-id='{0}-{1}']+tr>td:nth-child({2})"
        accordion_btn_css="#FormatAccordion"
        report_frame_css="#resultArea [id^=ReportIframe-]"
        report_heading_css="#divTreeTable #treetable thead"
        
        preview_report_css="TableChart_1"
        preview_report_data_css="#"+preview_report_css+" div[class^='x']"
                
        """------------------------------------------------------------------------Test Steps-----------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using "rsadv" user
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables&BIP_item=Enhanced_Accordion.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_table_css=row_val_css.format(4,1))
 
        """
            Verify the output
        """
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 02.01: Verify Report Output")
        report_obj.verify_column_heading(report_heading_css, expected_heading, "Step 02:02:Verify report column heading")
         
        """
            Step 03 : Expand South America > Camcorder > Computers > Media Player
        """
        report_obj.expand_colapse(node_path, "expand")
         
        """
            Verify the following Report is expanded
        """
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx")
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx", "Step 03:01: Verify expanded Report Output")
         
        """
            Step 04 : Hover over "North America"
            Verify the title pop up "Store Business Region" is displayed
        """
        report_obj.verify_table_cell_property(4, 1, table_css=row_val_css.format(4,1), title_popup=title_popup1, msg='Step 04:')
         
        """
            Step 05 : Hover over "Camcorder"
            Verify the title pop up "Product Category" is displayed
        """
        report_obj.verify_table_cell_property(4, 1, table_css=camcorder_val_css.format(4,1,1), title_popup=title_popup2, msg='Step 05:')
       
        """
            Step 06 :  Hover over "Handheld"
            Verify the title pop up "Subcategory" is displayed    
        """
        report_obj.verify_table_cell_property(4, 1, table_css=handheld_val_css.format(4,2,1), title_popup=title_popup3, msg='Step 06:')
         
        """
            Step 07 : Collapse Media Player > Computers > Camcorder > South America 
        """
        report_obj.expand_colapse(node_path, "collapse")
         
        """
            Step 08 : Resize the browser window and verify it does not throws any error message
        """
        report_obj.set_browser_window_size()
        report_obj.wait_for_visible_text(row_val_css.format(2,1), visble_text, medium_wait)
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 08.01: Verify Report Output")
        report_obj.maximize_browser()
        report_obj.wait_for_visible_text(row_val_css.format(2,1), visble_text, medium_wait)
        report_obj.api_logout()
        
        """
            Step 09 : Edit the Report using the below API URL
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables/Enhanced_Accordion.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name=fex_name, folder_name = folder_name, mrid=username, mrpass=password)
        report_obj.wait_for_number_of_element(preview_report_data_css, 116, long_wait)
        
        """
            Verify the following Query Pane,Filter and LivePreview
        """
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:01: Verify the Query panel in preview")
#         report_obj.create_report_data_set_in_preview('TableChart_1', 14,8, Test_Case_ID+"_Ds03.xlsx")
        report_obj.verify_report_data_set_in_preview(preview_report_css,14, 8, Test_Case_ID+"_Ds03.xlsx", "Step 09:02: Verify report data in preview")
        report_obj.verify_filter_pane_field(filter_pane_field_value, 1, "Step 09:03: Verify Filterpane field value")
        
        """
            Step 10 : Click Format tab
        """
        report_obj.switch_ia_ribbon_tab('Format')
        
        """
            Verify Accordion button is enabled under Format tab 
        """
        report_obj.wait_for_number_of_element(accordion_btn_css, 1, short_wait)
        elem=self.driver.find_element_by_css_selector(accordion_btn_css)
        report_obj.verify_checked_class_property_for_selected_object(elem, "Step 10:01: Verify whether Format tab Autodrill is enabled")
        
        """
            Step 11 : Click Run inside IA tool
        """
        report_obj.select_ia_toolbar_item('toolbar_run')
        report_obj.wait_for_number_of_element(report_frame_css, 1, long_wait)
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text(row_val_css.format(2,1), visble_text, medium_wait)
        
        
        """
            Verify the same output is displayed as mentioned in step 2
        """
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 11: Verify Report Output is displayed at step 2")


if __name__ == "__main__":
    unittest.main()