'''
Created on Jan 21, 2019

@author: Magesh
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8777556
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 3)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777556_TestClass(BaseTestCase):

    def test_C8777556(self):

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
        fex_name="AR-RP-141DA.fex"
        case_id = 'C8777556'
        expected_page_summary = '{0}of1000records,Page1of{1}'
        page_summary_number = '0'
        selection_type = 'Filter'
        filter_button = 'Highlight'
        type_value = "Equals"
        popup_dialog_number = 1
        row_color_type = 'rgb'
        data_set_message = "Step {0}: Expect all rows equal to {1} to be Highlighted, page down to verify."
        page_summary_message = "Step {0}: Verify Page summary '1000of1000records,Page1of18' after close dialog."
                
        """
        COMMON CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141DA.
        Expect to see the following Active Report of DATE fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='19960101', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('1'))
        
        """
        Step 2: For the following DATE fields, select Filter, then Equals and use these values:
        Click the Highlight button instead of the Filter button.
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/092
        QYY Order Date - Q1 1996
        wrMtrYY Order Date - Wednesday, May 1 1996
        .
        .
        Mtr Order Date - June
        Wtr Order Date - Monday

        Verify that the report contains only Highlighted rows that match the selected value.
        Expect only rows with value 19960201 to be Highlighted, page down to verify.
        Expect only rows with value MARCH 1, 1996 to be Highlighted, page down to verify.
        Expect only rows with value 1996/001 to be Highlighted, page down to verify.
        Expect only rows with value 96/092 to be Highlighted, page down to verify.
        Expect only rows with value Q1 1996 to be Highlighted, page down to verify.
        Expect only rows with value Wednesday, May 1 1996 to be Highlighted, page down to verify.
        Expect only rows with value June to be Highlighted, page down to verify.
        Expect only rows with value Monday to be Highlighted, page down to verify.
        """
        '''YYMD Order Date - 19960201'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='19960201')
        active_report_obj.filter_button_click(filter_button)
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        '''Expect only rows with value 19960201 to be Highlighted, page down to verify.''' 
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds01.xlsx', data_set_message.format('2', '19960201'))
        active_report_obj.close_filter_dialog()
        active_report_obj.navigate_page('first_page')
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.1'))
        
        '''MTRDYY Order Date - MARCH 1, 1996'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='MARCH 1, 1996')
        active_report_obj.filter_button_click(filter_button)
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        '''Expect only rows with value MARCH 1, 1996 to be Highlighted, page down to verify.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds02.xlsx', data_set_message.format('2.2', 'MARCH 1, 1996'))
        active_report_obj.close_filter_dialog()
        active_report_obj.navigate_page('first_page')
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.3'))
        
        '''YYJUL Order Date - 1996/001'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='1996/001')
        active_report_obj.filter_button_click(filter_button)
        '''Expect only rows with value 1996/001 to be Highlighted, page down to verify.''' 
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds03.xlsx', data_set_message.format('2.4', '1996/001'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.5'))
        
        '''JULIAN Order Date - 96/092'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='96/092')
        active_report_obj.filter_button_click(filter_button)
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        '''Expect only rows with value 96/092 to be Highlighted, page down to verify.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds04.xlsx', data_set_message.format('2.6', '96/092'))
        active_report_obj.close_filter_dialog()
        active_report_obj.navigate_page('first_page')
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.7'))
        
        '''QYY Order Date - Q1 1996'''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Q1 1996')
        active_report_obj.filter_button_click(filter_button)
        '''Expect only rows with value Q1 1996 to be Highlighted, page down to verify.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds05.xlsx', data_set_message.format('2.8', 'Q1 1996'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.9'))
        
        '''wrMtrYY Order Date - Wednesday, May 1 1996'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='Wednesday, May 1 1996')
        active_report_obj.filter_button_click(filter_button)
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        '''Expect only rows with value Wednesday, May 1 1996 to be Highlighted, page down to verify.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds06.xlsx', data_set_message.format('2.10', 'Wednesday, May 1 1996'))
        active_report_obj.close_filter_dialog()
        active_report_obj.navigate_page('first_page')
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.11'))
                
        '''Mtr Order Date - June'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='June')
        active_report_obj.filter_button_click(filter_button)
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        active_report_obj.navigate_page('next_page')
        '''Expect only rows with value June to be Highlighted, page down to verify.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds07.xlsx', data_set_message.format('2.12', 'June'))
        active_report_obj.close_filter_dialog()
        active_report_obj.navigate_page('first_page')
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.13'))
        
        '''Wtr Order Date - Monday'''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Monday')
        active_report_obj.filter_button_click(filter_button)
        '''Expect only rows with value Monday to be Highlighted, page down to verify.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds08.xlsx', data_set_message.format('2.14', 'Monday'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.15'))
         
if __name__ == "__main__":
    unittest.main()