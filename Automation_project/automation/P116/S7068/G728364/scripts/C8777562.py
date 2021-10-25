'''
Created on Jan 18, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777562
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 9)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777562_TestClass(BaseTestCase):

    def test_C8777562(self):

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
        type_value = "Less than"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - before {2}"
        
        """
            CSS
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
        Step 2: For the following DATE fields, select Filter, then Less than and use these values:
                YYMD Order Date - 19960201
                MTRDYY Order Date - MARCH 1, 1996
                YYJUL Order Date - 1996/001
                JULIAN Order Date - 96/122
                QYY Order Date - Q2 1996 
                wrMtrYY Order Date - Thursday, February 1 1996
                Mtr Order Date - March
                Wtr Order Date - Saturday
                Verify that the report contains only those rows that are Less than the selected value.
                Expect 180 rows - before 19960201
                Expect 360 rows - before MARCH 1, 1996
                Expect 0 rows - before 1996/001
                Expect 720 rows - before 96/122
                Expect 540 rows - before Q2 1996
                Expect 180 rows - before Thursday, February 1 1996
                Expect 360 rows - before March
                Expect 900 rows - before Saturday
        """
        '''YYMD Order Date - 19960201'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='19960201')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 180 rows - before 19960201''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('180', '4'), page_summary_message.format('2', '180', '19960201'))
        active_report_obj.close_filter_dialog()
        
        ''' MTRDYY Order Date - MARCH 1, 1996'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='MARCH 1, 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 360 rows - before MARCH 1, 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('360', '7'), page_summary_message.format('2.1', '360', 'MARCH 1, 1996'))
        active_report_obj.close_filter_dialog()
        
        '''YYJUL Order Date - 1996/001'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='1996/001')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 0 rows - before 1996/001''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('0', '1'), page_summary_message.format('2.2', '0', '1996/001'))
        active_report_obj.close_filter_dialog()
        
        '''JULIAN Order Date - 96/122'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='96/122')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 720 rows - before 96/122'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('720', '13'), page_summary_message.format('2.3', '720', '96/122'))
        active_report_obj.close_filter_dialog()
        
        '''QYY Order Date - Q2 1996 '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Q2 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 540 rows - before Q2 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('540', '10'), page_summary_message.format('2.4', '540', 'Q2 1996'))
        active_report_obj.close_filter_dialog()
                
        '''wrMtrYY Order Date - Thursday, February 1 1996'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Thursday, February 1 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 180 rows - before Thursday, February 1 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('180', '4'), page_summary_message.format('2.5', '180', 'Thursday, February 1 1996'))
        active_report_obj.close_filter_dialog()
        
        '''Mtr Order Date - March'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='March')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 360 rows - before March'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('360', '7'), page_summary_message.format('2.6', '360', 'March'))
        active_report_obj.close_filter_dialog()
        
        ''' Wtr Order Date - Saturday'''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Saturday')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 900 rows - before Saturday'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.7', '900', 'Saturday'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()