'''
Created on Aug 20, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287020
TestCase_Name : Verify to Run and Interact with 'Accordion DataTable'
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C2287020_TestClass(BaseTestCase):

    def test_C2287020(self):
        
        "-------------------------------------------------------------------CLASS OBJECTS--------------------------------------------------------------------------"
        report_obj = report.Report(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = 'C2287020'
        medium_wait= 30
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Top_10_DataTables_Accordion'
        folder_name='Retail_Samples/Portal/Responsive_Tables'
        row1_text_val="Subcategory"
        expanded_text_val="Handheld"
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        header_css="table[summary] > thead > tr:nth-child({0}) > th:nth-child({1})"
        row_val_css="table[summary] > tbody > tr:nth-child({0}) > td:nth-child({1})"
        expanded_row_text_css="table[summary] > tbody > tr:nth-child({0}) > td:nth-child({1})"
        table_css="table[summary]"
        run_table_css="#DataTables_Table_0 > tbody > tr"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to WebFocus using rsbas
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables&BIP_item=Top_10_DataTables_Accordion.fex
        """ 
        report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_table_css=run_table_css, no_of_element=13)
        
        """
        Verify the background color for Subcategory
        Verify the first row value of Report output
        """
        report_obj.wait_for_visible_text(header_css.format(1,1), row1_text_val, medium_wait)
        report_obj.verify_table_cell_property(1, 1, table_css=header_css.format(1,1),text_value=row1_text_val, bg_color='manatee', msg="Step 02.01: Verify the background color for Subcategory")
        
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 02.02: Verify Report Output")
        
        """
        Step03: Resize the browser window to small size
        Verify now it display the Accordion symbol "+"
        """
        report_obj.set_browser_window_size(x='408')
        report_obj.wait_for_visible_text(header_css.format(1,1), row1_text_val, medium_wait)
        report_obj.verify_accordion_symbol(row_val_css.format(1,1), "Step 03.01: Verify Accordion Symbol + is displayed")
        
        """
        Step04: Expand "+" symbol and Collapse
        Verify the output:
        """
        report_obj.select_accordion_row(row_val_css.format(4,1))
        report_obj.wait_for_visible_text(expanded_row_text_css.format(4,1), expanded_text_val, medium_wait)
#         report_obj.create_table_data_set("#DataTables_Table_0", Test_Case_ID+"_Ds02.xlsx")
        report_obj.verify_table_data_set("#DataTables_Table_0", Test_Case_ID+"_Ds02.xlsx", "Step 04.01: Verify Expanded Accordion Report Output")
        report_obj.select_accordion_row(row_val_css.format(4,1))
        
        """
        Step05: Maximize the browser window
        Verify the same output as displayed in step 2
        """
        report_obj.maximize_browser()
        report_obj.wait_for_visible_text(header_css.format(1,1), row1_text_val, medium_wait)
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 05.01: Verify the same output as displayed in step 2")
        
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()