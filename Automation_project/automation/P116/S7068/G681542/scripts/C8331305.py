'''
Created on Jan 18, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331305
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 12)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331305_TestClass(BaseTestCase):

    def test_C8331305(self):

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
        Step 2: For the following DECIMAL fields, select Filter, then Not Between the selected pair of values:
        D10.2 Unit Price - 17.00 & 26.00
        D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        D10.2E Unit Price - 0.13D+02 & 0.17D+02
        D10.2B Unit Price - (81.00) & (58.00)
        D10.2R Unit Price - 140.00CR & 125.00CR
        D10.2% Unit Price - 76.00% & 96.00%
        
        Verify that the report contains only those rows that are Not Between the selected pair of values.
        Expect 767 rows - values 17.00 & 26.00
        Expect 718 rows - values $0,000,026.00 & $0,000,028.00
        Expect 817 rows - values 0.13D+02 & 0.17D+02
        Expect 665 rows - values (81.00) & (58.00)
        Expect 867 rows - values 140.00CR & 125.00CR
        Expect 682 rows - values 76.00% & 96.00%
        """
        #D10.2 Unit Price - 17.00 & 26.00
        active_report_obj.select_menu_items("ITableData0", "1", "Filter","Not Between")
        active_report_obj.create_filter(1, 'Not Between',value1='17.00', value2='26.00')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '767of1000records,Page1of14', "Step 02.01: Expect 767 rows - values 17.00 & 26.00")
        active_report_obj.close_filter_dialog()
        
        #D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        active_report_obj.select_menu_items("ITableData0", "2", "Filter" , "Not Between")
        active_report_obj.create_filter(1, 'Not Between',value1='$0,000,026.00', value2='$0,000,028.00')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '718of1000records,Page1of13', "Step 02.02: Expect 718 rows - values $0,000,026.00 & $0,000,028.00")
        active_report_obj.close_filter_dialog()
        
        #D10.2E Unit Price - 0.13D+02 & 0.17D+02
        active_report_obj.select_menu_items("ITableData0", "3", "Filter","Not Between")
        active_report_obj.create_filter(1, 'Not Between',value1='0.13D+02', value2='0.17D+02')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '817of1000records,Page1of15', "Step 02.03: Expect 817 rows - values 0.13D+02 & 0.17D+02")
        active_report_obj.close_filter_dialog()
        
        #D10.2B Unit Price - (81.00) & (58.00)
        active_report_obj.select_menu_items("ITableData0", "4", "Filter","Not Between")
        active_report_obj.create_filter(1, 'Not Between',value1='(81.00)',value2='(58.00)')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '665of1000records,Page1of12', "Step 02.04: Expect 665 rows - values (81.00) & (58.00)")
        active_report_obj.close_filter_dialog()
        
        #D10.2R Unit Price - 140.00CR & 125.00CR
        active_report_obj.select_menu_items("ITableData0", "5", "Filter","Not Between")
        active_report_obj.create_filter(1, 'Not Between',value1='140.00 CR', value2='125.00 CR')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '867of1000records,Page1of16', "Step 02.005: Expect 867 rows - values 140.00CR & 125.00CR")
        active_report_obj.close_filter_dialog()
        
        #D10.2% Unit Price - 76.00% & 96.00%
        active_report_obj.select_menu_items("ITableData0", "6", "Filter","Not Between")
        active_report_obj.create_filter(1, 'Not Between',value1='76.00%', value2='96.00%')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '682of1000records,Page1of12', "Step 02.06: Expect 682 rows - values 76.00% & 96.00%")
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()