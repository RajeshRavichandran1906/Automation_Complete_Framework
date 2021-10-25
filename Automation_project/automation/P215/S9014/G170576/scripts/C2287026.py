'''
Created on Aug 20, 2018

@author: KS13172
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287026
TestCase_Name : Verify to Run 'Standard Autofit Off'
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C2287026_TestClass(BaseTestCase):

    def test_C2287026(self):
        
        driver = self.driver
        report_obj = report.Report(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID = 'C2287026'
        short_wait = 2
        medium_wait= 30
        long_wait= 60
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Top_10_Autofit_Off'
        folder_name='Retail_Samples/Portal/Responsive_Tables'
        row1_text_val="Subcategory"
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        row_val_css="table[summary] > tbody > tr:nth-child({0}) > td:nth-child({1})"
        table_css="table[summary]"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step01: Sign to WebFocus using rsbas
        http://machine:port/ibi_apps
        Step02: Run the Report using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables&BIP_item=Top_10_Autofit_Off.fex
        """ 
#         report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, home_page='old', run_table_css=row_val_css.format(1,1))
        report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_table_css=row_val_css.format(1,1))
        
        """
        Verify the background color for Subcategory
        Verify the first row value of Report output
        Verify Data bars are displayed in green color
        """
        
        report_obj.wait_for_visible_text(row_val_css.format(1,1), row1_text_val, medium_wait)
        
        report_obj.verify_table_cell_property(1, 1, table_css=row_val_css.format(1,1),text_value=row1_text_val, bg_color='manatee', msg="Step02.01:Verify the background color for Subcategory")
        report_obj.verify_visualize_bar_added_in_htmlreport('Gross Profit', 'green', 14, "Step02.02: Verify Data bars are displayed in green color", table_css=table_css)
        
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step02.03: Verify Report Output")
        
        """
        Step03: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        '''Will be acheived in teardown'''
#         report_obj.api_logout()

if __name__ == "__main__":
    unittest.main()