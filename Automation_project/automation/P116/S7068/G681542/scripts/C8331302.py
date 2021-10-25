'''
Created on Jan 18, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331302
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 9)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331302_TestClass(BaseTestCase):

    def test_C8331302(self):

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
        expected_page_summary = '1000of1000records,Page1of18'
        page_summary_number = '0'
        selection_type = 'Filter'
        type_value = "Less than"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - value {2}"
        
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
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary, "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DECIMAL fields, select Filter, then and use these values:
                D10.2 Unit Price - 17.00
                D10.2LM Unit Price - $0,000,026.00
                D10.2E Unit Price - 0.13D+02
                D10.2B Unit Price - (81.00)
                D10.2R Unit Price - 125.00CR
                D10.2% Unit Price - 28.00%
                Verify that the report contains only those rows that are Less than the selected value.
                Expect 84 rows - value 17.00
                Expect 183 rows - value $0,000,026.00
                Expect 0 rows - value 0.13D+02
                Expect 200 rows - value (81.00)
                Expect 67 rows - value 125.00CR
                Expect 317 rows - value 28.00%
        """
        '''D10.2 Unit Price - 17.00'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='17.00')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 84 rows - value 17.00''' 
        active_report_obj.verify_page_summary(page_summary_number, '84of1000records,Page1of2', page_summary_message.format('2', '84', '17.00'))
        active_report_obj.close_filter_dialog()
        
        '''D10.2LM Unit Price - $0,000,026.00'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='$0,000,026.00')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 183 rows - value $0,000,026.00'''
        active_report_obj.verify_page_summary(page_summary_number, '183of1000records,Page1of4', page_summary_message.format('2.1', '183', '$0,000,026.00'))
        active_report_obj.close_filter_dialog()
        
        '''D10.2E Unit Price - 0.13D+02'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='0.13D+02')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 0 rows - value 0.13D+02''' 
        active_report_obj.verify_page_summary(page_summary_number, '0of1000records,Page1of1', page_summary_message.format('2.2', '0', '0.13D+02'))
        active_report_obj.close_filter_dialog()
        
        
        '''D10.2B Unit Price - (81.00)'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='(81.00)')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 200 rows - value (81.00)'''
        active_report_obj.verify_page_summary(page_summary_number, '200of1000records,Page1of4', page_summary_message.format('2.3', '200', '(81.00)'))
        active_report_obj.close_filter_dialog()
        
        '''D10.2R Unit Price - 125.00CR'''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='125.00 CR')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 67 rows - value 125.00CR'''
        active_report_obj.verify_page_summary(page_summary_number, '67of1000records,Page1of2', page_summary_message.format('2.4', '67', '125.00CR'))
        active_report_obj.close_filter_dialog()
        
        '''D10.2% Unit Price - 28.00%'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='28.00%')
        active_report_obj.filter_button_click(selection_type)
        '''Expect 317 rows - value 28.00%'''
        active_report_obj.verify_page_summary(page_summary_number, '317of1000records,Page1of6', page_summary_message.format('2.5', '317', '28.00%'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()