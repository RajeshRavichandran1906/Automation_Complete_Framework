'''
Created on Jan 17, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8331296
Testcase Name : AHTML: Verify Filter operators against various Decimal fields(Part 3)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
import time
from common.wftools.active_report import Active_Report

class C8331296_TestClass(BaseTestCase):

    def test_C8331296(self):

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
        Test_Case_ID="C8331296"
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
        Step 2: For the following ALPHA fields, select Filter, then Equals and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.
        
        D10.2 Unit Price - 13.00
        
        D10.2LM Unit Price - $0,000,125.00
        
        D10.2E Unit Price - 0.26D+02
        
        D10.2B Unit Price - (76.00)
        
        D10.2R Unit Price - 140.00CR
        
        D10.2% Unit Price - 17.00%
        
        Verify that the report Highlights only those rows that match the selected value.
        .
        .
        .
        Expect only rows with value 13.00 to be Highlighted, page down to verify.
        Expect only rows with value $0,000,125.00 to be Highlighted, page down to verify.
        Expect only rows with value 0.26D+_02 to be Highlighted, page down to verify.
        Expect only rows with value (76.00) to be Highlighted, page down to verify.
        Expect only rows with value 140.00CR to be Highlighted, page down to verify.
        Expect only rows with value 17.00% to be Highlighted, page down to verify.
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals', value1='13.00')
        active_report_obj.filter_button_click('Highlight')
        """Expect only rows with value 13.00 to be Highlighted, page down to verify."""
#         active_report_obj.create_data_set_using_table_rowid(table_css, 'rgb',Test_Case_ID+'_Ds01.xlsx')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds01.xlsx',"Step 04.1: Verify highlighted dataset of D10.2 Unit Price - 13.00")
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,125.00"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='$0,000,125.00')
        active_report_obj.filter_button_click('Highlight')
        """Expect only rows with value $0,000,125.00 to be Highlighted, page down to verify."""
#         active_report_obj.create_data_set_using_table_rowid(table_css, 'rgb',Test_Case_ID+'_Ds02.xlsx')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds02.xlsx',"Step 04.3: Verify highlighted dataset of D10.2LM Unit Price - $0,000,125.00")
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.26D+02"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='0.26D+02')
        active_report_obj.filter_button_click('Highlight')
        """Expect only rows with value 0.26D+_02 to be Highlighted, page down to verify."""
#         active_report_obj.create_data_set_using_table_rowid(table_css, 'rgb',Test_Case_ID+'_Ds03.xlsx')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds03.xlsx',"Step 04.5: Verify highlighted dataset of D10.2E Unit Price - 0.26D+02")
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (76.00)"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='(76.00)')
        active_report_obj.filter_button_click('Highlight')
        """Expect only rows with value (76.00) to be Highlighted, page down to verify."""
#         active_report_obj.create_data_set_using_table_rowid(table_css, 'rgb',Test_Case_ID+'_Ds04.xlsx')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds04.xlsx',"Step 04.7: Verify highlighted dataset of D10.2B Unit Price - (76.00)")
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='140.00 CR')
        active_report_obj.filter_button_click('Highlight')
        """Expect only rows with value 140.00CR to be Highlighted, page down to verify."""
#         active_report_obj.create_data_set_using_table_rowid(table_css, 'rgb',Test_Case_ID+'_Ds05.xlsx')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds05.xlsx',"Step 04.9: Verify highlighted dataset of D10.2R Unit Price - 140.00CR")
        time.sleep(5)
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 17.00%"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Equals')
        active_report_obj.create_filter(1, 'Equals',value1='17.00%')
        active_report_obj.filter_button_click('Highlight')
        """Expect only rows with value 17.00% to be Highlighted, page down to verify."""
#         active_report_obj.create_data_set_using_table_rowid(table_css, 'rgb',Test_Case_ID+'_Ds06.xlsx')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds06.xlsx',"Step 04.11: Verify highlighted dataset of D10.2% Unit Price - 17.00%")
        time.sleep(5)
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.12: Verify Page summary 1000of1000records after close dialog')
        

if __name__ == "__main__":
    unittest.main()