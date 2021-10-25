'''
Created on Jan 21, 2019

@author: Magesh

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8777557
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 4)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777557_TestClass(BaseTestCase):

    def test_C8777557(self):

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
        Step 2: For the following DATE fields, select Filter, then Not equal and use these values:
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/092
        QYY Order Date - Q1 1996
        wrMtrYY Order Date - Wednesday, May 1 1996
        Mtr Order Date - June
        Wtr Order Date - Monday

        Verify that the report contains only those rows that do NOT match the selected value.
        Expect 820 rows - values not 19960201
        Expect 820 rows - values not MARCH 1, 1996
        Expect 820 rows - values not 1996/001
        Expect 820 rows - values not 96/092
        Expect 460 rows - values not Q1 1996
        Expect 820 rows - values not Wednesday, May 1 1996
        Expect 900 rows - values not June
        Expect 640 rows - values not Monday
        """
        '''YYMD Order Date - 19960201'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='19960201')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - values not 19960201''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2', '820', '19960201'))
        active_report_obj.close_filter_dialog()
        
        '''MTRDYY Order Date - MARCH 1, 1996'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='MARCH 1, 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - values not MARCH 1, 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.1', '820', 'MARCH 1, 1996'))
        active_report_obj.close_filter_dialog()
        
        '''YYJUL Order Date - 1996/001'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='1996/001')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - values not 1996/001''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.2', '820', '1996/001'))
        active_report_obj.close_filter_dialog()
        
        '''JULIAN Order Date - 96/092'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='96/092')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - values not 96/092'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.3', '820', '96/092'))
        active_report_obj.close_filter_dialog()
        
        '''QYY Order Date - Q1 1996 '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Q1 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 460 rows - values not Q1 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('460', '9'), page_summary_message.format('2.4', '460', 'Q1 1996'))
        active_report_obj.close_filter_dialog()
        
        '''wrMtrYY Order Date - Wednesday, May 1 1996'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Wednesday, May 1 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - values not Wednesday, May 1 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.5', '820', 'Wednesday, May 1 1996'))
        active_report_obj.close_filter_dialog()
        
        '''Mtr Order Date - June'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='June')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 900 rows - values not June'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.6', '900', 'June'))
        active_report_obj.close_filter_dialog()
        
        '''Wtr Order Date - Monday'''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Monday')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 640 rows - values not Monday'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('640', '12'), page_summary_message.format('2.7', '640', 'Monday'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()