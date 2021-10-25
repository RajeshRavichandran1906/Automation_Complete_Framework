'''
Created on Jan 17, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331297
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 4)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331297_TestClass(BaseTestCase):

    def test_C8331297(self):

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
        """
            CSS
        """
        table_css="ITableData0"
        data_value_css="#"+table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        """
        Step 1:Execute AR-RP-141DE.fex from below API to produce the alphanumeric output
        Expect to see the following Active Report.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='58.00', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DECIMAL fields, select Filter, then Not equal and use these values:
        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00CR
        D10.2% Unit Price - 28.00%
        Verify that the report contains only those rows that match the selected value.
        Expect 901 rows - value 17.00
        Expect 866 rows - value $0,000,026.00
        Expect 916 rows - value 0.13D+02
        Expect 782 rows - value (81.00)
        Expect 933 rows - value 140.00CR
        Expect 852 rows - value 28.00%
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal', value1='17.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 901 rows - value 17.00"""
        active_report_obj.verify_page_summary('0','901of1000records,Page1of16', 'Step 05.1: Verify Page summary 901of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.2: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2LM Unit Price - $0,000,026.00"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='$0,000,026.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 866 rows - value $0,000,026.00"""
        active_report_obj.verify_page_summary('0','866of1000records,Page1of16', 'Step 05.3: Verify Page summary 866of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.4: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2E Unit Price - 0.13D+02"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='0.13D+02')
        active_report_obj.filter_button_click('Filter')
        """Expect 916 rows - value 0.13D+02"""
        active_report_obj.verify_page_summary('0','916of1000records,Page1of17', 'Step 05.5: Verify Page summary 916of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.6: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2B Unit Price - (81.00)"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Not equal',value1='(81.00)')
        active_report_obj.filter_button_click('Filter')
        """Expect 782 rows - value (81.00)"""
        active_report_obj.verify_page_summary('0','782of1000records,Page1of14', 'Step 05.7: Verify Page summary 782of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.8: Verify Page summary 1000of1000records after close dialog')
                  
        """D10.2R Unit Price - 140.00CR"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Not equal',value1='140.00 CR')
        active_report_obj.filter_button_click('Filter')
        """Expect 933 rows - value 140.00CR"""
        active_report_obj.verify_page_summary('0','933of1000records,Page1of17', 'Step 05.9: Verify Page summary 933of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.10: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2% Unit Price - 28.00%"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Not equal',value1='28.00%')
        active_report_obj.filter_button_click('Filter')
        """Expect 852 rows - value 28.00%"""
        active_report_obj.verify_page_summary('0','852of1000records,Page1of15', 'Step 05.11: Verify Page summary 852of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.12: Verify Page summary 1000of1000records after close dialog')

if __name__ == "__main__":
    unittest.main()