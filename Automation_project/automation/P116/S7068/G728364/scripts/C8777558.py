'''
Created on Jan 21, 2019

@author: Magesh

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8777558
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 5)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777558_TestClass(BaseTestCase):

    def test_C8777558(self):

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
        expected_page_summary = '{0}of1000records,Page1of{1}'
        page_summary_number = '0'
        selection_type = 'Filter'
        type_value = "Not equal"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - not equal to {2} or later"
        
        """
        COMMON CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute AR-RP-141DE.fex from below API to produce the decimal output
        Expect to see the following Active Report.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='19960101', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DATE fields, select Filter, then Not equal and use these multi-selected values:
        YYMD Order Date - 19960201 & 1996061
        MTRDYY Order Date - MARCH 1, 1996 & APRIL 1, 1996
        YYJUL Order Date - 1996/001 & 1996/061 & 1996/122
        JULIAN Order Date - 96/032 & 96/061
        QYY Order Date - Q1 1996 & Q2 1996
        wrMtrYY Order Date - Thursday, February 1 1996 & Monday, April 1 1996
        Mtr Order Date - January & February
        Wtr Order Date - Thursday & Friday

        Verify that the report contains only those rows that do NOT match the multi-selected values.
        Expect 720 rows - values not 19960201 or 19960601
        Expect 640 rows - values notMARCH 1, 1996 or APRIL 1, 1996
        Expect 460 rows - values not 1996/001 or 1996/061 or 1996/122
        Expect 640 rows - values not96/032 or 96/061
        Expect 0 rows - values not Q1 1996 or Q2 1996
        Expect 640 rows - values not Thursday, February 1 1996 or Monday, April 1 1996
        Expect 640 rows - values not January or February
        Expect 640 rows - values not Thursday or Friday
        """
        '''YYMD Order Date - 19960201 & 1996061'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='19960201', value2='19960601')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 720 rows - values not 19960201 or 19960601''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('720', '13'), page_summary_message.format('2', '720', '19960201 or 19960601'))
        active_report_obj.close_filter_dialog()
        
        '''MTRDYY Order Date - MARCH 1, 1996 & APRIL 1, 1996'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='MARCH 1, 1996', value2='APRIL 1, 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 640 rows - values not MARCH 1, 1996 or APRIL 1, 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('640', '12'), page_summary_message.format('2.1', '640', 'MARCH 1, 1996 or APRIL 1, 1996'))
        active_report_obj.close_filter_dialog()
        
        '''YYJUL Order Date - 1996/001 & 1996/061 & 1996/122'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='1996/001', value2='1996/061', value3='1996/122')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 460 rows - values not 1996/001 or 1996/061 or 1996/122''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('460', '9'), page_summary_message.format('2.2', '460', '1996/001 or 1996/061 or 1996/122'))
        active_report_obj.close_filter_dialog()
        
        '''JULIAN Order Date - 96/032 & 96/061'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='96/032', value2='96/061')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 640 rows - values not 96/032 or 96/061'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('640', '12'), page_summary_message.format('2.3', '640', '96/032 or 96/061'))
        active_report_obj.close_filter_dialog()
        
        '''QYY Order Date - Q1 1996 & Q2 1996'''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='Q1 1996', value2='Q2 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 0 rows - values not Q1 1996 or Q2 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('0', '1'), page_summary_message.format('2.4', '0', 'Q1 1996 or Q2 1996'))
        active_report_obj.close_filter_dialog()
        
        '''wrMtrYY Order Date - Thursday, February 1 1996 & Monday, April 1 1996'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='Thursday, February 1 1996', value2='Monday, April 1 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 640 rows - values not Thursday, February 1 1996 or Monday, April 1 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('640', '12'), page_summary_message.format('2.5', '640', 'Thursday, February 1 1996 or Monday, April 1 1996'))
        active_report_obj.close_filter_dialog()
        
        '''Mtr Order Date - January & February'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='January',value2='February')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 640 rows - values not January or February'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('640', '12'), page_summary_message.format('2.6', '640', 'January or February'))
        active_report_obj.close_filter_dialog()
        
        '''Wtr Order Date - Thursday & Friday'''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Thursday',value2='Friday')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 640 rows - values not Thursday or Friday'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('640', '12'), page_summary_message.format('2.7', '640', 'Thursday or Friday'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()