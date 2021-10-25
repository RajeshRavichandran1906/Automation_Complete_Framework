'''
Created on Jul 9, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2275842&group_by=cases:section_id&group_order=asc&group_id=170568
TestCase_Name : 
'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C2275842_TestClass(BaseTestCase):

    def test_C2275842(self):
        
        Test_Case_ID = "C2275842"
        driver = self.driver
        report_obj=report.Report(self.driver)
        
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
        """
        report_obj.edit_retailsamples_using_api(tool='report',folder_name='Reports', subfolder_name='Auto_Link',fex_name='Report_Store_Product_Metrices', mrid='mrid', mrpass='mrpass')
        report_obj.run_retailsamples_report_using_api(folder_name='Reports', subfolder_name='Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass')
#         report_obj.run_retailsamples_using_api(folder_name='Reports', subfolder_name='Auto_Link', fex_name='Report_Store_Product_Metrices', mrid='mrid', mrpass='mrpass')
        
        """
            Step 02 : Run the Report using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Reports/Auto_Link&BIP_item=Report_Store_Product_Metrics.fex
        """
        """
            Step 03 :Verify the output
        """
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()