'''
Created on Jan 18, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777563
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 10)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777563_TestClass(BaseTestCase):

    def test_C8777563(self):

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
        type_value = "Less than or equal to"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - on or before {2}"
        
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
        Step 2: For the following DATE fields, select Filter, then Less than or equal to and use these values:
                YYMD Order Date - 19960201
                MTRDYY Order Date - MARCH 1, 1996
                YYJUL Order Date - 1996/001
                JULIAN Order Date - 96/122
                QYY Order Date - Q2 1996 
                wrMtrYY Order Date - Thursday, February 1 1996
                Mtr Order Date - March
                Wtr Order Date - Saturday
                Verify that the report contains only those rows that are Less than or equal to the selected value.
                Expect 360 rows - on or before 19960201
                Expect 540 rows - on or before MARCH 1, 1996
                Expect 180 rows - on or before 1996/001
                Expect 900 rows - on or before 96/122
                Expect 1000 rows - on or before Q2 1996
                Expect 360 rows - on or before Thursday, February 1 1996
                Expect 540 rows - on or before March
                Expect 1000 rows - on or before Saturday
        """
        '''YYMD Order Date - 19960201'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='19960201')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 360 rows - on or before 19960201''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('360', '7'), page_summary_message.format('2', '360', '19960201'))
        active_report_obj.close_filter_dialog()
        
        ''' MTRDYY Order Date - MARCH 1, 1996'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='MARCH 1, 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 540 rows - on or before MARCH 1, 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('540', '10'), page_summary_message.format('2.1', '540', 'MARCH 1, 1996'))
        active_report_obj.close_filter_dialog()
       
        '''YYJUL Order Date - 1996/001'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='1996/001')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 180 rows - on or before 1996/001''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('180', '4'), page_summary_message.format('2.2', '180', '1996/001'))
        active_report_obj.close_filter_dialog()
        
        '''JULIAN Order Date - 96/122'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='96/122')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 900 rows - on or before 96/122'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.3', '900', '96/122'))
        active_report_obj.close_filter_dialog()
        
        '''QYY Order Date - Q2 1996  '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Q2 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 1000 rows - on or before Q2 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.4', '1000', 'Q2 1996'))
        active_report_obj.close_filter_dialog()
            
        '''wrMtrYY Order Date - Thursday, February 1 1996'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Thursday, February 1 1996')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 360 rows - on or before Thursday, February 1 1996'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('360', '7'), page_summary_message.format('2.5', '360', 'Thursday, February 1 1996'))
        active_report_obj.close_filter_dialog()
        
        '''Mtr Order Date - March'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='March')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 540 rows - on or before March'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('540', '10'), page_summary_message.format('2.6', '540', 'March'))
        active_report_obj.close_filter_dialog()
        
        ''' Wtr Order Date - Saturday '''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Saturday')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 1000 rows - on or before Saturday'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.7', '1000', 'Saturday'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()