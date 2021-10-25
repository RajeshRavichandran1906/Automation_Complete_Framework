'''
Created on Jan 17, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331298
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 5)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331298_TestClass(BaseTestCase):

    def test_C8331298(self):

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
        Step 2: For the following DECIMAL fields, select Filter, then Not equal and use these multiple values:
        D10.2 Unit Price - 13.00 & 17.00
        D10.2LM Unit Price - $0,000,125.00 & $0,000,140.00
        
        D10.2E Unit Price - 0.26D+02 & 0.28D+02 
        D10.2B Unit Price - (76.00) & (58.00) & (28.00)
        D10.2R Unit Price - 140.00CR & 13.00CR
        D10.2% Unit Price - 13.00% & 76.00%
        
        Verify that the report contains only those rows that match the selected multiple values.
        
        Expect 817 rows - values not 13.00 or 17.00
        Expect 867 rows - values not $0,000,125.00 or $0,000,140.00
        Expect 718 rows - values not 0.26D+02 or 0.28D+02 
        Expect 735 rows - values not (76.00) or (58.00) or (28.00)
        Expect 849 rows - values not 140.00CR or 13.00CR
        Expect 883 rows - values not 13.00% or 76.00%
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal', value1='13.00',value2='17.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 817 rows - values not 13.00 or 17.00"""
        active_report_obj.verify_page_summary('0','817of1000records,Page1of15', 'Step 06.1: Verify Page summary 817of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.2: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2LM Unit Price - $0,000,125.00 & $0,000,140.00"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='$0,000,125.00',value2='$0,000,140.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 867 rows - values not $0,000,125.00 or $0,000,140.00"""
        active_report_obj.verify_page_summary('0','867of1000records,Page1of16', 'Step 06.3: Verify Page summary 867of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.4: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2E Unit Price - 0.26D+02 & 0.28D+02 """
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='0.26D+02',value2='0.28D+02')
        active_report_obj.filter_button_click('Filter')
        """Expect 718 rows - values not 0.26D+02 or 0.28D+02 """
        active_report_obj.verify_page_summary('0','718of1000records,Page1of13', 'Step 06.5: Verify Page summary 718of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.6: Verify Page summary 1000of1000records after close dialog')
           
        """D10.2B Unit Price - (76.00) & (58.00) & (28.00))"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='(76.00)',value2='(58.00)',value3='(28.00)')
        active_report_obj.filter_button_click('Filter')
        """Expect 735 rows - values not (76.00) or (58.00) or (28.00)"""
        active_report_obj.verify_page_summary('0','735of1000records,Page1of13', 'Step 06.7: Verify Page summary 735of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.8: Verify Page summary 1000of1000records after close dialog')
                  
        """D10.2R Unit Price - 140.00CR & 13.00CR"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='140.00 CR',value2='13.00 CR')
        active_report_obj.filter_button_click('Filter')
        """Expect 849 rows - values not 140.00CR or 13.00CR"""
        active_report_obj.verify_page_summary('0','849of1000records,Page1of15', 'Step 06.9: Verify Page summary 849of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.10: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2% Unit Price - 13.00% & 76.00%"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Not equal')
        active_report_obj.create_filter(1, 'Not equal',value1='13.00%',value2='76.00%')
        active_report_obj.filter_button_click('Filter')
        """Expect 883 rows - values not 13.00% or 76.00%"""
        active_report_obj.verify_page_summary('0','883of1000records,Page1of16', 'Step 06.11: Verify Page summary 883of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.12: Verify Page summary 1000of1000records after close dialog')
        

if __name__ == "__main__":
    unittest.main()