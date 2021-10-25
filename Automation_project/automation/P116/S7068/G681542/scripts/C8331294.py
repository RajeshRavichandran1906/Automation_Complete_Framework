'''
Created on Jan 17, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331294&group_by=cases:section_id&group_order=asc&group_id=681542
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 1)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331294_TestClass(BaseTestCase):

    def test_C8331294(self):

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
        Test_Case_ID="C8331294"
        
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
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", "Step 1:02: Verify report data set", table_css="#"+table_css, desired_no_of_rows=8, starting_rownum=2)
        
        """
        Step 2: Step 2:For the following DECIMAL fields, select Filter, then Equals and use these values:
        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00CR
        D10.2% Unit Price - 28.00%
        
        Verify that the report contains only those rows that match the selected value.
        Expect 99 rows - value 17.00
        Expect 134 rows - value $0,000,026.00
        Expect 84 rows - value 0.13D+02
        Expect 218 rows - value (81.00)
        Expect 67 rows - value 140.00CR
        Expect 148 rows - value 28.00%
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals', value1='17.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 99 rows - value 17.00"""
        active_report_obj.verify_page_summary('0','99of1000records,Page1of2', 'Step 02.1: Verify Page summary 99of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,026.00"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='$0,000,026.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 134 rows - value $0,000,026.00"""
        active_report_obj.verify_page_summary('0','134of1000records,Page1of3', 'Step 02.3: Verify Page summary 134of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.13D+02"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='0.13D+02')
        active_report_obj.filter_button_click('Filter')
        """Expect 84 rows - value 0.13D+02"""
        active_report_obj.verify_page_summary('0','84of1000records,Page1of2', 'Step 02.5: Verify Page summary 84of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (81.00)"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='(81.00)')
        active_report_obj.filter_button_click('Filter')
        """Expect 218 rows - value (81.00)"""
        active_report_obj.verify_page_summary('0','218of1000records,Page1of4', 'Step 02.7: Verify Page summary 218of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='140.00 CR')
        active_report_obj.filter_button_click('Filter')
        """Expect 67 rows - value 140.00CR"""
        active_report_obj.verify_page_summary('0','67of1000records,Page1of2', 'Step 02.9: Verify Page summary 67of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 28.00%"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='28.00%')
        active_report_obj.filter_button_click('Filter')
        """Expect 148 rows - value 28.00%"""
        active_report_obj.verify_page_summary('0','148of1000records,Page1of3', 'Step 02.11: Verify Page summary 148of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.12: Verify Page summary 1000of1000records after close dialog')
        

if __name__ == "__main__":
    unittest.main()