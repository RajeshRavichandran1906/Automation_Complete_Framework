'''
Created on Dec 14, 2017

@author: Praveen Ramkumar/ Updated by : Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511572
TestCase Name : Report-Sort: Verify Sort is working correctly on report
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2511572_TestClass(BaseTestCase):

    def test_C2511572(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511572'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """        
            Step 01:Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02:Expand folder P292_S10032_G157266Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03:Verify the AHTML formatted report is generated.
        """
        
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")   

        """
            Step 04:Select Dollar Sales and select 'Ascending' filter optionExpect to see the report in Ascending order of Dollar Sales.
            Dollar sales range would go like this: 158995, 161352, 169908, 171319, 177940... 349300, 352161, 355447.
        """
        
        miscelanousobj.select_menu_items("ITableData0", 5, "Sort Ascending")       
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 04.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 04.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx", "Step 04.3: verify Count of all records ", desired_no_of_rows=20)
        
        """
            Step 05:Select Dollar Sales again and reverse the sort by selecting 'Descending'.
            Expect to see the report, now in descending Dollar Sales order.
        """
        
        miscelanousobj.select_menu_items("ITableData0", 5, "Sort Descending")       
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 05.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 05.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx", "Step 05.3: verify Count of all records ", desired_no_of_rows=20)
        
        """
            Step 06:Select the dropdown for Product, then select 'Descending'.
            Expect to see the report in descending sort on alphanumeric field - Product.
        """
        miscelanousobj.select_menu_items("ITableData0", 2, "Sort Descending")       
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 06.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 06.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds04.xlsx", "Step 06.3: verify Count of all records ", desired_no_of_rows=20)
        
        
        """
            Step 07:Select the dropdown again for Product and reverse the sort by selecting 'Ascending'.
            Expect to see the report, now sorted in ascending Product name order.
        """
        miscelanousobj.select_menu_items("ITableData0", 2, "Sort Ascending")       
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 07.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 07.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds05.xlsx", "Step 07.3: verify Count of all records ", desired_no_of_rows=20)
        
        """
            Step 08:Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
                
if __name__ == '__main__':
    unittest.main()