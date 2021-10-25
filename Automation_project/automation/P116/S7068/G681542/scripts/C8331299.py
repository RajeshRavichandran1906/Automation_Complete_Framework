'''
Created on Jan 17, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331299
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 6)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331299_TestClass(BaseTestCase):

    def test_C8331299(self):

        """
           CLASS OBJECTS
        """ 
        utillobj = utillity.UtillityMethods(self.driver)
        active_report_obj=Active_Report(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+"/"+suite_id
        
        """
            TESTCASE VARIABLES
        """
        fex_name="AR-RP-141DE.fex"
        case_id = 'C8331299'
        expected_page_summary = '1000of1000records,Page1of18'
        page_summary_number = '0'
        selection_type = 'Filter'
        type_value = 'Not equal'
        popup_dialog_number = 1
        button_name = 'Highlight'
        row_color_type = 'rgb'
        data_set_message = "Step {0}: Verify highlighted dataset of D10.{1} Unit Price - {2}"
        page_summary_message = "Step {0}: Verify Page summary '1000of1000records,Page1of18' after close dialog."
        
        """
            CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute AR-RP-141DE.fex from below API to produce the decimal output
                Expect to see the following Active Report.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='58.00', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, expected_page_summary, "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following ALPHA fields, select Filter, then Not equal and use these values:
                Select the Highlight option for this test.
                After each field Highlight, close the Filter panel for the next field.
                D10.2 Unit Price - 13.00
                D10.2LM Unit Price - $0,000,125.00 
                D10.2E Unit Price - 0.26D+02 
                D10.2B Unit Price - (76.00) 
                D10.2R Unit Price - 140.00CR
                D10.2% Unit Price - 17.00%
                Verify that the report Highlights only those rows that do NOT match the selected value.
                Expect rows Not equal to 13.00 to be Highlighted, page down to verify.
                Expect rows Not equal to $0,000,125.00 to be Highlighted, page down to verify.
                Expect rows Not equal to 0.26D+_02 to be Highlighted, page down to verify.
                Expect rows Not equal to (76.00) to be Highlighted, page down to verify.
                Expect rows Not equal to 140.00CR to be Highlighted, page down to verify.
                Expect rows Not equal to 17.00% to be Highlighted, page down to verify.
        """
        """D10.2 Unit Price - 13.00"""
        active_report_obj.select_menu_items(table_id, 1, selection_type,type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='13.00')
        active_report_obj.filter_button_click(button_name)
        """Expect only rows with value 13.00 to be Highlighted, page down to verify."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds01.xlsx', data_set_message.format('2', '2', '13.00'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number,expected_page_summary, page_summary_message.format('2.1'))
        
        """D10.2LM Unit Price - $0,000,125.00"""
        active_report_obj.select_menu_items(table_id, 2, selection_type,type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='$0,000,125.00')
        active_report_obj.filter_button_click(button_name)
        """Expect only rows with value $0,000,125.00 to be Highlighted, page down to verify."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds02.xlsx', data_set_message.format('2.2', '2LM', '$0,000,125.00'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number,expected_page_summary, page_summary_message.format('2.3'))
         
        """D10.2E Unit Price - 0.26D+02"""
        active_report_obj.select_menu_items(table_id, 3, selection_type,type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='0.26D+02')
        active_report_obj.filter_button_click(button_name)
        """Expect only rows with value 0.26D+_02 to be Highlighted, page down to verify."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds03.xlsx', data_set_message.format('2.4', '2E', '0.26D+02'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number,expected_page_summary, page_summary_message.format('2.5'))
         
        """D10.2B Unit Price - (76.00)"""
        active_report_obj.select_menu_items(table_id, 4, selection_type,type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='(76.00)')
        active_report_obj.filter_button_click(button_name)
        """Expect only rows with value (76.00) to be Highlighted, page down to verify."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds04.xlsx', data_set_message.format('2.6', '2B', '(76.00)'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number,expected_page_summary, page_summary_message.format('2.7'))
                 
        """D10.2R Unit Price - 140.00CR"""
        active_report_obj.select_menu_items(table_id, 5, selection_type,type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='140.00 CR')
        active_report_obj.filter_button_click(button_name)
        """Expect only rows with value 140.00CR to be Highlighted, page down to verify."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds05.xlsx', data_set_message.format('2.8', '2R', '140.00 CR'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number,expected_page_summary, page_summary_message.format('2.9'))
         
        """D10.2% Unit Price - 17.00%"""
        active_report_obj.select_menu_items(table_id, 6, selection_type,type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='17.00%')
        active_report_obj.filter_button_click(button_name)
        """Expect only rows with value 17.00% to be Highlighted, page down to verify."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds06.xlsx', data_set_message.format('2.10', '2%', '17.00%'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number,expected_page_summary, page_summary_message.format('2.11'))
         
if __name__ == "__main__":
    unittest.main()