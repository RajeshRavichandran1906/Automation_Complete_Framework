'''
Created on Jan 05, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227750
TestCase Name =Report-Other: Verify that hide/unhide column works in AHTML
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2511620_TestClass(BaseTestCase):

    def test_C2511620(self):
        
        """
            TESTCASE VARIABLES
        """        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name="AHTML_001.fex"
        Test_Case_ID="C2511620"
       
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G15726 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="COUNTRY")
        
        """
            Step 03 :Verify the report is generated.
            Verify correct output displayed on run.
            Pagination toolbar is present on the top.            
        """
        
        miscelaneousobj.verify_page_summary('0','5of5records,Page1of1','Step 03.1 : Verify Pagination toolbar is present on the top.')
#         utillobj.create_data_set('ITableData0','I0r','C2227750_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx', 'Step 03.2: Verify that report returns 29 of 107 records')
        
        """
            Step 04:Click on Sales and select Hide Column.Verify Sales column is not visible.          
        """
        miscelaneousobj.verify_page_summary('0','5of5records,Page1of1','Step 04.1 : Verify page summary')
        miscelaneousobj.select_menu_items("ITableData0", 3, "Hide Column")
#         utillobj.create_data_set('ITableData0','I0r','C2227750_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx', 'Step 04.2: Verify Sales column is not visible. ')
        
        """
            Step 05:Click on Dealer_Cost and select Hide Column.Verify Dealer_Cost column is not visible          
        """
        miscelaneousobj.verify_page_summary('0','5of5records,Page1of1','Step 05.1 : Verify page summary')
        miscelaneousobj.select_menu_items("ITableData0",2, "Hide Column")
#         utillobj.create_data_set('ITableData0','I0r','C2227750_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx', 'Step 05.2: Verify Dealer_Cost column is not visible')
        
        """
            Step 06:Click on Country and choose Show Columns >Sales Verify Sales column is visible.          
        """
        miscelaneousobj.verify_page_summary('0','5of5records,Page1of1','Step 06.1 : Verify page summary')
        miscelaneousobj.select_menu_items("ITableData0",0, "Show Columns","SALES")
#         utillobj.create_data_set('ITableData0','I0r','C2227750_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx', 'Step 06.2: Verify Sales column is visible.')
        
        """
            Step 07:Click on COUNTRY again and choose Show Columns > Show All Verify all the columns are visible now.    
        """
        miscelaneousobj.verify_page_summary('0','5of5records,Page1of1','Step 07.1 : Verify all the columns are visible now.')
        miscelaneousobj.select_menu_items("ITableData0",0, "Show Columns","Show All")
#         utillobj.create_data_set('ITableData0','I0r','C2227750_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds05.xlsx', 'Step 07.2: Verify Sales column is visible.')
        
        """
            Step 08:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()