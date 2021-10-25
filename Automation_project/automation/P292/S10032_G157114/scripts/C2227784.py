'''
Created on Dec 14, 2017

@author: Pavithra / Updated by : Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227784
TestCase Name : Repor-Sort: Verify Restore Original correctly reproduces report after Sorting. (ACT-478)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2227784_TestClass(BaseTestCase):

    def test_C2227784(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227784'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="cacheOFF_Restorea.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """        
            Step 01:Sign in to WebFOCUS as a Basic user 

            Step 02:Execute the following URL:
                    
                    http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=cacheOFF_Restore.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03:Verify the AHTML formatted report is generated.

        """
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03:03: verify report data")   

        """
            Step 04: From the drop down control for Unit Sales, click Sort Descending.
                    
                    Expect to see the Active Report re-sorted in descending order of Unit Sales values.
        """
        miscelanousobj.select_menu_items("ITableData0", 4, "Sort Descending")
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 04.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 04.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx", "Step 04.3: Active Report re-sorted in descending order of Unit Sales values", desired_no_of_rows=20)   
        
        """
            Step 05:From the drop down list for Unit Sales, click Restore Original, at the bottom of the menu list.
                    
                    Expect to see the original report, from step 1 re-appear.
        """
        miscelanousobj.select_menu_items("ITableData0", 0, "Restore Original")
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 05.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 05.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 05:03: verify report data")
        
        """
            Step 06:Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
        time.sleep(5)   
                
if __name__ == '__main__':
    unittest.main()
        