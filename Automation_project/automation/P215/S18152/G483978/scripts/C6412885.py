'''
Created on Aug 23, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6417164&group_by=cases:section_id&group_id=483978&group_order=asc
Testcase Name : Verify to Run and Edit 'Enhanced_Accordion'

'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C6412885_TestClass(BaseTestCase):

    def test_C6412885(self):
        
        driver = self.driver
        report_obj = report.Report(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = 'C6412885'
        short_wait = 25
        medium_wait= 90
        long_wait= 400
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Enhanced_Accordion_styled'
        new_fex_name='Enhanced Accordion with Inline Styling_1'
        reopen_fex_name='Enhanced_Accordion_with_Inline_Styling_1'
        folder_name='Retail_Samples/Portal/Responsive_Tables'
        fex_folder_after_save="SmokeTest/~rsadv"
        
        report_heading_val="Gross Profit"
        node_path="North America->Camcorder->Handheld"
        title_popup1="Store Business Region"
        title_popup2="Product Category"
        title_popup3="Subcategory"
        node_path_to_colapse="North America"
        visible_text="Oceania"

        no_of_table_elements=658
        bg_color="vivid_violet1"
        font_color="white"
        
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'Gross Profit', 'Discount', 'MSRP', 'Cost of Goods', 'Quantity,Sold', 'By', 'Store,Business,Region', 'Product,Category', 'Product,Subcategory', 'Model', 'Across']
        filter_pane_field_value="Product,Subcategory Not equal to Home Theater Systems"
        expected_heading='Gross Profit  Discount  MSRP  COGS  Qty'
        preview_parent_id='TableChart_1'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        
        table_css="#treetable"
        parent_table_css="#divTreeTable"
        row_val_css=table_css+".treetable > tbody > tr[data-tt-id='{0}'] td:nth-child({1})"
        report_heading_css="#divTreeTable #treetable.treetable thead"
        gross_profit_heading_css=report_heading_css+" >tr>th:nth-child({0})"
        handheld_row_val_css=parent_table_css+" "+table_css+".treetable > tbody > tr[data-tt-id='{0}-{1}-{2}'] td:nth-child({3})"
        camcorder_row_val_css=table_css+".treetable > tbody > tr[data-tt-id='{0}-{1}'] td:nth-child({2})"
        no_of_table_elements_css=table_css+".treetable > tbody > tr"
        
        preview_report_css="TableChart_1"
        preview_report_data_css="#"+preview_report_css+" div[class^='x']"
        accordion_btn_css="#FormatAccordion"
        report_frame_css="#resultArea [id^=ReportIframe-]"
        application_css="#applicationButton"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
                
        """
            Step 01 : Sign to Webfocus using "rsadv" user
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables&BIP_item=Enhanced_Accordion_styled.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_table_css=no_of_table_elements_css, no_of_element=no_of_table_elements)
           
        """
            Verify the output
        """
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", desired_no_of_rows=25)
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 02.01: Verify Report Output", desired_no_of_rows=25)
        report_obj.verify_column_heading(report_heading_css, expected_heading, "Step 02:02:Verify report column heading")
        msg='Step 02:03 ['+report_heading_val+'] ['+bg_color+'] ['+font_color+']'
        report_obj.verify_table_cell_property(1, 2, gross_profit_heading_css.format(2), text_value=report_heading_val, bg_color=bg_color,font_color=font_color, msg=msg)
           
        """
            Step 03 : Expand North America > Camcorder > Handheld 
        """
        report_obj.expand_colapse(node_path, "expand")
           
        """
           Verify the following Report is expanded
        """
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx", desired_no_of_rows=50)
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx", "Step 02.01: Verify report is expanded", desired_no_of_rows=50)
           
        """
            Step 04 : Hover over "North America"
            Verify the title pop up "Store Business Region" is displayed
        """
        report_obj.verify_table_cell_property(2, 1, table_css=row_val_css.format(2,1), title_popup=title_popup1, msg='Step 04:')
          
        """
            Step 05 : Hover over "Camcorder" 
            Verify the title pop up "Product Category" is displayed
        """
        report_obj.verify_table_cell_property(2, 1, table_css=camcorder_row_val_css.format(2,2,1), title_popup=title_popup2, msg='Step 05:')
           
        """
            Step 06 : Hover over "Handheld"
            Verify the title pop up "Subcategory" is displayed
        """
        report_obj.verify_table_cell_property(2, 1, table_css=handheld_row_val_css.format(2,2,1,1), title_popup=title_popup3, msg='Step 06:')
          
        """
            Step 07 : Collapse North America
        """
        report_obj.expand_colapse(node_path_to_colapse, "collapse")
           
        """
            Step 08 : Resize the browser window and verify it does not throws any error message
        """
        report_obj.set_browser_window_size()
        report_obj.wait_for_visible_text(row_val_css.format(3,1), visible_text, medium_wait)
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 08.01: Verify Report Output", desired_no_of_rows=25)
        report_obj.maximize_browser()
        report_obj.wait_for_visible_text(row_val_css.format(3,1), visible_text, medium_wait)
        report_obj.api_logout()
         
        """
            Step 09 : Edit the Report using the below API URL
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables/Enhanced_Accordion_styled.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name=fex_name, folder_name = folder_name, mrid=username, mrpass=password)
        report_obj.wait_for_number_of_element(preview_report_data_css, 439, long_wait)
         
        """
            Verify the following Report
        """
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:01: Verify the Query panel in preview")
#         report_obj.create_report_data_set_in_preview('TableChart_1', 25, 9, Test_Case_ID+"_Ds03.xlsx")
        report_obj.verify_report_data_set_in_preview(preview_report_css,25, 9, Test_Case_ID+"_Ds03.xlsx", "Step 09:02: Verify report data in preview")
        report_obj.verify_filter_pane_field(filter_pane_field_value, 1, "Step 09:03: Verify Filterpane field value")
        report_obj.verify_report_cell_property(preview_parent_id, 28, bg_color=bg_color, bg_cell_no=28,text_value='North America', msg="Step 09:04: Verify font color shows in violet color")
         
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
        report_obj.wait_for_number_of_element(no_of_table_elements_css, no_of_table_elements, medium_wait)
         
        msg='Step 11: ['+report_heading_val+'] ['+bg_color+'] ['+font_color+']'
        report_obj.verify_table_cell_property(1, 2, gross_profit_heading_css.format(2), text_value=report_heading_val, bg_color=bg_color,font_color=font_color, msg=msg)
         
        """
            Verify the same output is displayed as mentioned in step 2
        """
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 11:01: Verify Report Output is displayed at step 2", desired_no_of_rows=25)
         
        """
            Step 12 : Click IA > Save > Select "SmokeTest > Enter title as "Enhanced Accordion with Inline Styling_1.fex" > Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.wait_for_number_of_element(application_css, 1, long_wait)
        report_obj.save_as_from_application_menu_item(file_name = new_fex_name, target_table_path = 'SmokeTest->My Content')
         
        """
            Step 13 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
            Step 14 : Edit the saved Report using "rsadv" user with the below API URL
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Enhanced Accordion with Inline Styling_1.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name = reopen_fex_name, folder_name = fex_folder_after_save, mrid=username, mrpass=password)
        report_obj.wait_for_number_of_element(preview_report_data_css, 439, long_wait)
        
        """
            Verify restore successfully
        """
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 14:01: Verify the Query panel in preview")
#         report_obj.create_report_data_set_in_preview('TableChart_1', 25, 9, Test_Case_ID+"_Ds03.xlsx")
        report_obj.verify_report_data_set_in_preview(preview_report_css,25, 9, Test_Case_ID+"_Ds03.xlsx", "Step 14:02: Verify report data in preview")
        report_obj.verify_filter_pane_field(filter_pane_field_value, 1, "Step 14:03: Verify Filterpane field value")
        report_obj.verify_report_cell_property(preview_parent_id, 28, bg_color=bg_color, bg_cell_no=28,text_value='North America', msg="Step 14:04: Verify font color shows in violet color")
        
        """
            Step 15 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
       
        
if __name__ == "__main__":
    unittest.main()

