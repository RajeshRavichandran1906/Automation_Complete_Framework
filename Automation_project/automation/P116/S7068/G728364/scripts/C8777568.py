'''
Created on Jan 21, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777568
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 15)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777568_TestClass(BaseTestCase):

    def test_C8777568(self):

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
        type_value = "Omits"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - before {2}"
        
        """
            CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141DA.
                Expect to see the following Active Report containing DATE fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='19960101', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DATE fields, select Filter, then Omits, then enter the strings below.
                Case does NOT matter for these tests
                YYMD Order Date - 9602
                MTRDYY Order Date - April
                YYJUL Order Date - 6/15
                JULIAN Order Date - 96/00
                QYY Order Date - Q2 
                wrMtrYY Order Date - june
                Mtr Order Date - Feb
                Wtr Order Date - SAT
                Verify that the report contains only those rows that Contain the string value entered.
                Expect 820 rows - all dates except those containing '9602' 
                Expect 820 rows - all dates except those containing 'April'
                Expect 900 rows - all dates except those containing '6/15' 
                Expect 820 rows - all dates except those containing '96/00'
                Expect 540 rows - all dates except those containing 'Q2' 
                Expect 900 rows - all dates except those containing 'june'
                Expect 820 rows - all dates except those containing 'Feb'
                Expect 900 rows - all dates except those containing 'SAT'
        """
        '''YYMD Order Date - 9602'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='9602')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - all dates except those containing '9602' ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2', '820', '9602'))
        active_report_obj.close_filter_dialog()
        
        ''' MTRDYY Order Date - April'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='April')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - all dates except those containing 'April' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.1', '820', 'April'))
        active_report_obj.close_filter_dialog()
                 
        '''YYJUL Order Date - '6/15' '''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='6/15')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 900 rows - all dates except those containing 6/15''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.2', '900', '6/15'))
        active_report_obj.close_filter_dialog()
        
        '''JULIAN Order Date - '96/00' '''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='96/00')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - all dates except those containing 96/00'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.3', '820', '96/00'))
        active_report_obj.close_filter_dialog()
        
        ''' QYY Order Date - 'Q2' '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Q2')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 540 rows - all dates except those containing Q2'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('540', '10'), page_summary_message.format('2.4', '540', 'Q2'))
        active_report_obj.close_filter_dialog()
                
        '''wrMtrYY Order Date - 'june' '''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='june')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 900 rows - all dates except those containing june'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.5', '900', 'june'))
        active_report_obj.close_filter_dialog()
        
        '''Mtr Order Date - 'Feb' '''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Feb')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 820 rows - all dates except those containing Feb'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.6', '820', 'Feb'))
        active_report_obj.close_filter_dialog()
        
        '''Wtr Order Date - 'SAT' '''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='SAT')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 900 rows - all dates except those containing SAT'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.7', '900', 'SAT'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()