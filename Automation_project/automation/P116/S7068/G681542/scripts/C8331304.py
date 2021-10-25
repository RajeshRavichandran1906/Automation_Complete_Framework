'''
Created on Jan 18, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331304
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 11)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331304_TestClass(BaseTestCase):

    def test_C8331304(self):

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
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary, "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DECIMAL fields, select Filter, then Between the selected pair of values:
        D10.2 Unit Price - 17.00 & 26.00
        D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        D10.2E Unit Price - 0.13D+02 & 0.17D+02
        D10.2B Unit Price - (81.00) & (58.00)
        D10.2R Unit Price - 140.00CR & 125.00CR
        D10.2% Unit Price - 76.00% & 96.00%
        
        Verify that the report contains only those rows that are Between the selected pair of values.
        Expect 233 rows - values 17.00 & 26.00
        Expect 282 rows - values $0,000,026.00 & $0,000,028.00
        Expect 183 rows - values 0.13D+02 & 0.17D+02
        Expect 335 rows - values (81.00) & (58.00)
        Expect 133 rows - values 140.00CR & 125.00CR
        Expect 318 rows - values 76.00% & 96.00%
        """
        '''D10.2 Unit Price - 17.00 & 26.00'''
        active_report_obj.select_menu_items("ITableData0", "1", "Filter","Between")
        active_report_obj.create_filter(1, 'Between',value1='17.00', value2='26.00')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '233of1000records,Page1of5', "Step 2.1: Expect 233 rows - values 17.00 & 26.00")
        active_report_obj.close_filter_dialog()
        
        #D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        active_report_obj.select_menu_items("ITableData0", "2", "Filter" ,"Between")
        active_report_obj.create_filter(1, 'Between',value1='$0,000,026.00', value2='$0,000,028.00')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '282of1000records,Page1of5', "Step 2.2: Expect 282 rows - values $0,000,026.00 & $0,000,028.00")
        active_report_obj.close_filter_dialog()
        
        #D10.2E Unit Price - 0.13D+02 & 0.17D+02
        active_report_obj.select_menu_items("ITableData0", "3", "Filter","Between")
        active_report_obj.create_filter(1, 'Between',value1='0.13D+02', value2='0.17D+02')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '183of1000records,Page1of4', "Step 2.3: Expect 183 rows - values 0.13D+02 & 0.17D+02")
        active_report_obj.close_filter_dialog()
        
        #D10.2B Unit Price - (81.00) & (58.00)
        active_report_obj.select_menu_items("ITableData0", "4", "Filter","Between")
        active_report_obj.create_filter(1, 'Between',value1='(81.00)',value2='(58.00)')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '335of1000records,Page1of6', "Step 2.4: Expect 335 rows - values (81.00) & (58.00")
        active_report_obj.close_filter_dialog()
        
        #D10.2R Unit Price - 140.00CR & 125.00CR
        active_report_obj.select_menu_items("ITableData0", "5", "Filter","Between")
        active_report_obj.create_filter(1, 'Between',value1='140.00 CR', value2='125.00 CR')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '133of1000records,Page1of3', "Step 2.5: Expect 133 rows - values 140.00CR & 125.00CR")
        active_report_obj.close_filter_dialog()
        
        #D10.2% Unit Price - 76.00% & 96.00%
        active_report_obj.select_menu_items("ITableData0", "6", "Filter","Between")
        active_report_obj.create_filter(1, 'Between',value1='76.00%', value2='96.00%')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '318of1000records,Page1of6', "Step 2.6: Expect 318 rows - values 76.00% & 96.00%")
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()