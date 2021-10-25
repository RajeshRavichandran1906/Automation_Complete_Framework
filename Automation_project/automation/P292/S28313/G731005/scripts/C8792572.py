"""---------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 23-August-2019
---------------------------------------------------------------------------------------"""
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase

class C8792572_TestClass(BaseTestCase):

    def test_C8792572(self):
    
        """CLASS OBJECTS"""
        report = Report(self.driver)
       
        """COMMON VARIABLES"""
        case_id = "C8792572"
        preview_table_css = "#TableChart_1"
        grayout_filed_css = "#queryTreeColumn tr[style*='gray']"
        data_set1 = case_id + "_DataSet01.xlsx"
        data_set2 = case_id + "_DataSet02.xlsx"
        preview_table_id = 'TableChart_1'
        
        """
            STEP 01 : Launch the API to create new Report with CAR
            http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S28313/G671908
        """
        report.invoke_ia_tool_using_new_api_login(master='ibisamp/car')
        report.wait_for_visible_text(preview_table_css, "Drag", report.report_long_timesleep)
        
        """
            STEP 02 : Double click "CAR","DEALER_COST" and "SALES" in Data pane
        """
        report.double_click_on_datetree_item("CAR")
        report.wait_for_visible_text(preview_table_css, "CAR", report.report_short_timesleep)
        
        report.double_click_on_datetree_item("DEALER_COST")
        report.wait_for_visible_text(preview_table_css, "DEALER_COST", report.report_short_timesleep)
        
        report.double_click_on_datetree_item("SALES")
        report.wait_for_visible_text(preview_table_css, "SALES", report.report_short_timesleep)
        
        """
            STEP 03 : Right click "SALES" in Query pane and Select "Sort" > "Sort" > Descending
            Check the Query pane
        """
        expected_query_pane = ['Report (car)', 'Sum', 'DEALER_COST', 'SALES', 'By', 'SALES', 'CAR', 'Across']
        report.right_click_on_field_under_query_tree("SALES", 1, "Sort->Sort->Descending")
        report.wait_for_visible_text(grayout_filed_css, 'SALES', report.report_short_timesleep)
        report.verify_all_fields_in_query_pane(expected_query_pane, "Step 03.01 : Verify query pane fields")
        report.verify_grayedout_fields_in_query_pane(['SALES'], "03.02")
        report.verify_descending_fields_in_query_pane(['SALES'], "03.03")
        
        """
            STEP 04 : Right click "DEALER_COST" in Query pane and Select "Sort" > "Sort" > Descending.
            Check the Query pane
        """
        expected_query_pane = ['Report (car)', 'Sum', 'DEALER_COST', 'SALES', 'By', 'DEALER_COST', 'SALES', 'CAR', 'Across']
        report.right_click_on_field_under_query_tree("DEALER_COST", 1, "Sort->Sort->Descending")
        report.wait_for_visible_text(grayout_filed_css, 'DEALER_COST', report.report_short_timesleep)
        report.verify_all_fields_in_query_pane(expected_query_pane, "Step 04.01 : Verify query pane fields")
        report.verify_grayedout_fields_in_query_pane(['DEALER_COST', 'SALES'], "04.02")
        report.verify_descending_fields_in_query_pane(['DEALER_COST', 'SALES'], "04.03")
        
        """
            STEP 05 : Click "Save" in toolbar Enter "C8792572" and Click "Save" button
        """
        report.save_report_from_toptoolbar()
        report.wait_for_visible_text("#dlgIbfsOpenFile7", 'Save', report.report_short_timesleep)
        report.save_file_in_save_dialog(case_id)
        
        """
            STEP 06 : Logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        
        """
            STEP 07 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S28313/G671908/C8792572.fex&tool=Report
            Check the Live preview.
        """
        report.edit_fex_using_api_url(case_id)
        report.wait_for_visible_text(preview_table_css, "SALES", report.report_short_timesleep)
        #report.create_acrossreport_data_set_in_preview(preview_table_id, 1, 3, 10, 3, data_set1)
        report.verify_across_report_data_set_in_preview(preview_table_id, 1, 3, 10, 3, data_set1, "Step 07.01 : Verify live preview")
        
        """
            STEP 08 : Drag and drop "SALES" above "DEALER_COST" in the BY bucket.
            Check the Query pane and Live preview.
        """
        report.drag_query_filed_to_another_query_field("SALES", "DEALER_COST", 2, 2,  target_field_loc='top_middle')
        expected_query_pane = ['Report (car)', 'Sum', 'DEALER_COST', 'SALES', 'By', 'SALES', 'DEALER_COST', 'CAR', 'Across']
        report.verify_all_fields_in_query_pane(expected_query_pane, "Step 08.01 : Verify query pane fields")
        report.verify_grayedout_fields_in_query_pane(['SALES', 'DEALER_COST'], "08.02")
        report.verify_descending_fields_in_query_pane(['SALES', 'DEALER_COST'], "08.03")
        #report.create_acrossreport_data_set_in_preview(preview_table_id, 1, 3, 10, 3, data_set2)
        report.verify_across_report_data_set_in_preview(preview_table_id, 1, 3, 10, 3, data_set2, "Step 08.04 : Verify live preview")
        
        """
            STEP 09 : Click "Save" from toolbar and Click "OK" button
        """
        report.save_report_from_toptoolbar()
        
        """
            STEP 10 : Logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """