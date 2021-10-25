'''
Created on Jul 23, 2018

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275845
TestCase Name : Verify to Run and Edit 'Margin_by_Product_Category'
'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C2275845_TestClass(BaseTestCase):

    def test_C2275845(self):
        
        Test_Case_ID = "C2275845"
        report_obj=report.Report(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        fex_name="Margin_by_Product_Category"
        save_fex="Margin by Product Category1"
        fex_name1="Margin_by_Product_Category1"
        folder_name="Retail_Samples/Reports"
        saved_fex_foldername="SmokeTest/~rsadv"
        
        long_time=240
        medium_time=90
        short_time=30
        
        "-------------------------------------------------------------------CSS-------------------------------------------------------------------------------------------"
        
        table_css="table[summary='Summary']"
        row_val_css=table_css+" > tbody > tr:nth-child({0}) > td:nth-child({1})"
        autodrill_css="#FormatAutoDrill"
        report_frame_css="#resultArea [id^=ReportIframe-]"
        frame_css="iframe[src]"
        
        text_val="40.41%"
        camcorder_row_text_val="Camcorder"
        tooltip_path1='Drill down to Product Subcategory'
        tooltip_path2='Drill down to Model'
        tooltip_path3='Reset'
        verify_tooltip1=['Drill down to Product Subcategory']
        verify_tooltip2=['Reset', 'Go up to Product Category', 'Drill down to Model']
        verify_tooltip3=['Reset', 'Go up to Product Subcategory']
        visible_GLXY1076_val='GLXYT10716'
        visible_smartphone_val="Smartphone"
        
        application_css="#applicationButton"
        preview_report_css1 =  "#TableChart_1"
        preview_report_css="TableChart_1"
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'AVE.Margin', 'Revenue', 'Cost of Goods', 'Gross Profit', 'By', 'AVE.Margin', 'Product,Category', 'Across']
        preview_expected_total_values=['34.46%', '$94,233.10', '$66,109.00', '$28,124.10']
        preview_expected_title_list=['ProductCategory', 'AVEMargin', 'Revenue', 'Cost of Goods', 'Gross Profit']
        
        """-----------------------------------------------------------------------Test Steps-----------------------------------------------------------------------------------------"""
        
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Reports&BIP_item=Margin_by_Product_Category.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', run_table_css=frame_css)
        report_obj.switch_to_frame(frame_css=frame_css)
        report_obj.wait_for_visible_text(row_val_css.format(2,2), text_val, medium_time)
         
        """
            Step 03 : Verify the output with Hyperlink
            Verify TL condition for AVE Margin
            Verify first row value of Report output
            Verify Total values
        """
        report_obj.verify_table_cell_property(2, 2, table_css=row_val_css.format(2,2),text_value=text_val, font_color='green', msg="Step 03:01:Verify second row first column value is shown in grren color")
        report_obj.verify_autolink_in_runtime(table_css, "Camcorder", 2, 1, 7, "Step 03:02: Verify number of hyper link in table")
        report_obj.verify_visualize_bar_added_in_htmlreport('AVEMargin', 'light_gray', 7, "Step 03:03: Verify visualization bar are added in the report")
        report_obj.verify_visualize_bar_added_in_htmlreport('Revenue', 'light_gray', 7, "Step 03:04: Verify visualization bar are added in the report")
        report_obj.verify_visualize_bar_added_in_htmlreport('Gross Profit', 'light_gray', 7, "Step 03:05: Verify visualization bar are added in the report")
         
#         report_obj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 03:07: Verify report data")
         
        """
            Step 04 : Click Computers, verify the "Autodrill" menu
            Step 05 : Click "Drill down to Product Subcategory "
        """
        report_obj.select_report_autolink_tooltip_runtime(table_css,4,1,tooltip_path1, verify_tooltip=verify_tooltip1, verify_type='asequal', msg="Step04:01:Verify tooltip value")
        report_obj.wait_for_visible_text(row_val_css.format(5,1), visible_smartphone_val, medium_time)
         
        """
            Step 06 : Verify it drills down to Product Subcategory
        """
#         report_obj.create_table_data_set("table[summary='Summary']",Test_Case_ID+"_Ds02.xlsx")
        report_obj.verify_table_data_set(table_css,Test_Case_ID+"_Ds02.xlsx", "Step 06:02: Verify it drilldown to product subcategory")
         
        """ 
            Step 07 : Click Tablet, verify the "Autodrill" menu
            Step 08 : Click "Drill down to Model"
            Step 09 : Verify it drills down to Model
        """
        report_obj.select_report_autolink_tooltip_runtime(table_css,4,1,tooltip_path2, verify_tooltip=verify_tooltip2, verify_type='asequal',msg="Step 07:01: Clicked on Tablet Verify tooltip value")
        report_obj.wait_for_visible_text(row_val_css.format(5,1), visible_GLXY1076_val, medium_time)
         
#         report_obj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds03.xlsx",)
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds03.xlsx", "Step 09:01: Verify it drilldown to product subcategory")
         
        """
            Step 10 : Click "GLXYT3B" > Restore Original
        """
        report_obj.select_report_autolink_tooltip_runtime(table_css,8,1, tooltip_path3, verify_tooltip=verify_tooltip3,verify_type='asequal',msg="Step 10:01: Clicked on GLXYT3B Verify tooltip value")
        report_obj.wait_for_visible_text(row_val_css.format(2,2), text_val, medium_time)
         
        """
            Step 11 : Verify the Report restored back to original
            Verify TL condition for AVE Margin
            Verify first row value of Report output
        """
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 11:01: Verify it drilldown to product subcategory")
         
        """
            Step 12 : Resize the browser window and verify it does not throws any error message
        """
        report_obj.set_browser_window_size()
        report_obj.wait_for_visible_text(row_val_css.format(2,2), text_val, medium_time)
         
        report_obj.verify_table_cell_property(2, 2, table_css=row_val_css.format(2,2), text_value=text_val, font_color='green', msg="Step 12:01:Verify second row first column value is shown in grren color")
        report_obj.maximize_browser()
        time.sleep(3)
         
        """
            Step 13 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
        """
            Step 14 :  Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Reports/Margin_by_Product_Category.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name=fex_name, folder_name=folder_name)
        report_obj.wait_for_visible_text(preview_report_css1, 'Revenue')
        
        """
            Step 15 : Verify the following Report output
            Verify the fields in Query panel are displayed same in Live Preview
            Verify Total values
        """
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 15:01: Verify the Query panel")
        report_obj.verify_field_in_querypane('By', "AVE.Margin", 1, msg="Step 15:02: Verify AVE.margin(By bucket)shown in gray color", color_to_verify='Trolley_Grey', font_to_verify='italic')
        report_obj.verify_column_total(preview_report_css,preview_expected_total_values, "Step 15:02:Verify row total values in the preview report")
        report_obj.verify_report_cell_property(preview_report_css, 12, font_color='green', text_value='42.46%', msg="Step 15:03: Verify font color shows in green and the value returns 42.46")
        report_obj.verify_report_cell_property(preview_report_css, 17, font_color='green', text_value='41.86%', msg="Step 15:04: Verify font color shows in green and the value returns 41.86")
        report_obj.verify_report_cell_property(preview_report_css, 22, font_color='green', text_value='40.17%', msg="Step 15:05: Verify font color shows in green and the value returns 40.17")
#         report_obj.create_report_data_set_in_preview('TableChart_1', 8, 5, Test_Case_ID+"_Ds04.xlsx")
        report_obj.verify_report_data_set_in_preview(preview_report_css, 8, 5, Test_Case_ID+"_Ds04.xlsx", "Step 15:06:Verify report data in preview")
        report_obj.verify_column_title_on_preview(5, 10, table_id=preview_report_css, expected_list=preview_expected_title_list, msg="Step 15:07: Verify column titles")
        report_obj.verify_visualize_bar_added_in_previewreport('light_gray', 28, "Step 15:08:Verify visualization bar")
        
        """
            Step 16 : Click Format tab > Verify "Autodrill"button is enabled
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_number_of_element(autodrill_css, 1, short_time)
        elem=self.driver.find_element_by_css_selector(autodrill_css)
        report_obj.verify_checked_class_property_for_selected_object(elem, "Step 16:01:Verify whether Format tab Autodrill is enabled")
        
        """
            Step 17 : Click Run inside IA tool
        """
        report_obj.select_ia_toolbar_item('toolbar_run')
        report_obj.wait_for_number_of_element(report_frame_css, 1, medium_time)
        report_obj.switch_to_frame()
        report_obj.switch_to_frame(frame_css=frame_css)
        report_obj.wait_for_visible_text(row_val_css.format(2,1), camcorder_row_text_val, medium_time)
        report_obj.verify_autolink_in_runtime(table_css, camcorder_row_text_val, 2, 1, 7, "Step 17:01:Verify number of hyper link in table")
        report_obj.verify_table_cell_property(2, 2, table_css=row_val_css.format(2,2),text_value=text_val, font_color='green', msg="Step 17:02:Verify second row first column value is shown in grren color")
        
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 17:03: Verify report data")
        
        report_obj.verify_visualize_bar_added_in_htmlreport("AVEMargin", 'light_gray', 7, "Step 17:04: Verify visualization bar are added in the report")
        report_obj.verify_visualize_bar_added_in_htmlreport("Revenue", 'light_gray', 7, "Step 17:05: Verify visualization bar are added in the report")
        report_obj.verify_visualize_bar_added_in_htmlreport("Gross Profit", 'light_gray', 7, "Step 17:06: Verify visualization bar are added in the report")
        
        """
            Step 18 : Click IA > Save As> Select "SmokeTest" > MYContent folder> Enter title as "Margin by Product Category1" > Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.wait_for_number_of_element(application_css, 1, long_time)
        report_obj.save_as_from_application_menu_item(file_name = save_fex, target_table_path= 'SmokeTest->My Content' )
         
        """
            Step 19 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
        """
            Step 20 : Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Margin_by_Product_Category1.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name=fex_name1, folder_name=saved_fex_foldername)
        report_obj.wait_for_visible_text(preview_report_css1, 'Revenue')
        report_obj.verify_report_cell_property(preview_report_css, 12, font_color='green', text_value='42.46%', msg="Step 20:01: Verify font color shows in green and the value returns 42.46")
        report_obj.verify_report_cell_property(preview_report_css, 17, font_color='green', text_value='41.86%', msg="Step 20:02: Verify font color shows in green and the value returns 41.86")
        report_obj.verify_report_cell_property(preview_report_css, 22, font_color='green', text_value='40.17%', msg="Step 20:03: Verify font color shows in green and the value returns 40.17")
        report_obj.verify_report_data_set_in_preview(preview_report_css, 8, 5, Test_Case_ID+"_Ds04.xlsx", "Step 20:04:Verify report data in preview")
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 20:05: Verify the Query panel")
        report_obj.verify_field_in_querypane('By', "AVE.Margin", 1, msg="Step 20:06: Verify AVE.margin(By bucket)shown in gray color", color_to_verify='Trolley_Grey', font_to_verify='italic')
        report_obj.verify_report_data_set_in_preview(preview_report_css, 8, 5, Test_Case_ID+"_Ds04.xlsx", "Step 20:07: Verify report data in preview")
        report_obj.verify_column_title_on_preview(5, 10, table_id=preview_report_css, expected_list=preview_expected_title_list, msg="Step 20:08: Verify column titles")
        report_obj.verify_column_total('TableChart_1',preview_expected_total_values, "Step 20:09: Verify row total values in the preview report")
        report_obj.verify_visualize_bar_added_in_previewreport('light_gray', 28, "Step 20:10:Verify visualization bar")
        
        """
            Step 21 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    

if __name__ == "__main__":
    unittest.main()