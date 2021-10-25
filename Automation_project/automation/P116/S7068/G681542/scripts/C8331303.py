'''
Created on Jan 18, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331303
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 10)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331303_TestClass(BaseTestCase):

    def test_C8331303(self):

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
        type_value = "Less than or equal to"
        popup_dialog_number = 0
        
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
        utillobj.wait_for_page_loads(10)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary, "Step 01.01: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DECIMAL fields, select Filter, then Less than or equal to the selected value:
        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00CR
        D10.2% Unit Price - 28.00%
        
        Verify that the report contains only those rows that are Less than or equal to the selected value.
        Expect 183 rows - value 17.00
        Expect 317 rows - value $0,000,026.00
        Expect 84 rows - value 0.13D+02
        Expect 418 rows - value (81.00)
        Expect 67 rows - value 140.00CR
        Expect 465 rows - value 28.00%
        """
        #D10.2 Unit Price - 17.00
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='17.00')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(popup_dialog_number, '183of1000records,Page1of4', "Step 02.01: Expect 183 rows - value 17.00")
        active_report_obj.close_filter_dialog()
        utillobj.synchronize_until_element_disappear(".arFilterButton", 5)
        
        #D10.2LM Unit Price - $0,000,026.00
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='$0,000,026.00')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(popup_dialog_number, '317of1000records,Page1of6', "Step 02.02: Expect 317 rows - value $0,000,026.00")
        active_report_obj.close_filter_dialog()
        utillobj.synchronize_until_element_disappear(".arFilterButton", 5)
        
        #D10.2E Unit Price - 0.13D+02
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(1, type_value,value1='0.13D+02')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(popup_dialog_number, '84of1000records,Page1of2', "Step 02.03: Expect 84 rows - value 0.13D+02")
        active_report_obj.close_filter_dialog()
        utillobj.synchronize_until_element_disappear(".arFilterButton", 5)
        
        #D10.2B Unit Price - (81.00)
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(1, type_value,value1='(81.00)')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(popup_dialog_number, '418of1000records,Page1of8', "Step 02.04: Expect 418 rows - value (81.00)")
        active_report_obj.close_filter_dialog()
        utillobj.synchronize_until_element_disappear(".arFilterButton", 5)
        
        #Expect 67 rows - value 140.00CR
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(1, type_value,value1='140.00 CR')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(popup_dialog_number, '67of1000records,Page1of2', "Step 02.05: Expect 67 rows - value 140.00CR")
        active_report_obj.close_filter_dialog()
        utillobj.synchronize_until_element_disappear(".arFilterButton", 5)
        
        #D10.2% Unit Price - 28.00%
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(1, type_value,value1='28.00%')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(popup_dialog_number, '465of1000records,Page1of9', "Step 02.06: Expect 465 rows - value 28.00%")
        active_report_obj.close_filter_dialog()
        utillobj.synchronize_until_element_disappear(".arFilterButton", 5)
         
if __name__ == "__main__":
    unittest.main()