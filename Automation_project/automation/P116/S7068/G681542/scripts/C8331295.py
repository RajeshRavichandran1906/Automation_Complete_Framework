'''
Created on Jan 17, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331295
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 2) 
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8331295_TestClass(BaseTestCase):

    def test_C8331295(self):

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
        Step 2: For the following DECIMAL fields, select Filter, then Equals and use these multiple values:
        D10.2 Unit Price - 13.00 & 17.00
        D10.2LM Unit Price - $0,000,125.00 & $0,000,140.00
        D10.2E Unit Price - 0.26D+02 & 0.28D+02 
        D10.2B Unit Price - (76.00) & (58.00) & (28.00)
        D10.2R Unit Price - 140.00CR & 13.00CR
        D10.2% Unit Price - 13.00% & 76.00%
        
        Verify that the report contains only those rows that match the selected multiple values.
        
        Expect 183 rows - values 13.00 & 17.00
        Expect 133 rows - values $0,000,125.00 & $0,000,140.00
        Expect 282 rows - values 0.26D+02 & 0.28D+02 
        Expect 265 rows - values (76.00) & (58.00) & (28.00)
        Expect 151 rows - values 140.00CR & 13.00CR
        Expect 117 rows - values 13.00% & 76.00%
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals', value1='13.00',value2='17.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 183 rows - values 13.00 & 17.00"""
        active_report_obj.verify_page_summary('0','183of1000records,Page1of4', 'Step 02.1: Verify Page summary 183of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,125.00 & $0,000,140.00"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='$0,000,125.00',value2='$0,000,140.00')
        active_report_obj.filter_button_click('Filter')
        """Expect 133 rows - values $0,000,125.00 & $0,000,140.00"""
        active_report_obj.verify_page_summary('0','133of1000records,Page1of3', 'Step 02.3: Verify Page summary 133of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.26D+02 & 0.28D+02 """
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='0.26D+02',value2='0.28D+02')
        active_report_obj.filter_button_click('Filter')
        """Expect 282 rows - values 0.26D+02 & 0.28D+02"""
        active_report_obj.verify_page_summary('0','282of1000records,Page1of5', 'Step 02.5: Verify Page summary 282of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (76.00) & (58.00) & (28.00))"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='(76.00)',value2='(58.00)',value3='(28.00)')
        active_report_obj.filter_button_click('Filter')
        """Expect 265 rows - values (76.00) & (58.00) & (28.00)"""
        active_report_obj.verify_page_summary('0','265of1000records,Page1of5', 'Step 02.7: Verify Page summary 265of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR & 13.00CR"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='140.00 CR',value2='13.00 CR')
        active_report_obj.filter_button_click('Filter')
        """Expect 151 rows - values 140.00CR & 13.00CR"""
        active_report_obj.verify_page_summary('0','151of1000records,Page1of3', 'Step 02.9: Verify Page summary 151of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 13.00% & 76.00%"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='13.00%',value2='76.00%')
        active_report_obj.filter_button_click('Filter')
        """Expect 117 rows - values 13.00% & 76.00%"""
        active_report_obj.verify_page_summary('0','117of1000records,Page1of3', 'Step 02.11: Verify Page summary 148of1000records')
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.12: Verify Page summary 1000of1000records after close dialog')
        


if __name__ == "__main__":
    unittest.main()