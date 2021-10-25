'''
Created on Jan 21, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777569
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 16)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777569_TestClass(BaseTestCase):

    def test_C8777569(self):

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
        type_value = "Omits (match case)"
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
        Step 2: For the following DATE fields, select Filter, then Omits(case match), then enter the strings below.
                Case matters for these tests, the string must match exactly.
                Only fields containing multiple alphanumeric characters are included.
                MTRDYY Order Date - April
                MTRDYY Order Date - APRIL
                wrMtrYY Order Date - june
                wrMtrYY Order Date - June
                Mtr Order Date - JAN
                Mtr Order Date - Jan
                Wtr Order Date - sAT
                Wtr Order Date - Sat
                Verify that the report contains only those rows that Omit the exact Case string value entered.
                Expect 1000 rows - no dates omit 'April'
                Expect 820 rows - all dates that omit 'APRIL'
                Expect 1000 rows - no dates that omit 'june'
                Expect 900 rows - all dates that omit 'June'
                Expect 1000 rows - no dates that omit 'JAN'
                Expect 820 rows - all dates that omit 'Jan'
                Expect 1000 rows - no dates omit 'sAT'
                Expect 900 rows - all dates that omit 'Sat'
        """
        ''' MTRDYY Order Date - April '''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='April')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 1000 rows - no dates omit 'April' ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2', '1000', 'April'))
        active_report_obj.close_filter_dialog()
        
        ''' MTRDYY Order Date - APRIL '''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='APRIL')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 820 rows - all dates that omit 'APRIL' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.1', '820', 'APRIL'))
        active_report_obj.close_filter_dialog()
                 
        ''' wrMtrYY Order Date - june '''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='june')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 1000 rows - no dates that omit 'june' ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.2', '1000', 'june'))
        active_report_obj.close_filter_dialog()
        
        ''' wrMtrYY Order Date - June '''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='June')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 900 rows - all dates that omit 'June' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.3', '900', 'June'))
        active_report_obj.close_filter_dialog()
        
        ''' Mtr Order Date - JAN '''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='JAN')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 1000 rows - no dates that omit 'JAN' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.4', '1000', 'JAN'))
        active_report_obj.close_filter_dialog()
                           
        ''' Mtr Order Date - Jan '''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Jan')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 820 rows - all dates that omit 'Jan' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('820', '15'), page_summary_message.format('2.5', '820', 'Jan'))
        active_report_obj.close_filter_dialog()
        
        ''' Wtr Order Date - sAT '''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='sAT')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 1000 rows - no dates omit 'sAT' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.6', '1000', 'sAT'))
        active_report_obj.close_filter_dialog()
        
        ''' Wtr Order Date - Sat  '''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='Sat')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 900 rows - all dates that omit 'Sat' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('900', '16'), page_summary_message.format('2.7', '900', 'Sat'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()