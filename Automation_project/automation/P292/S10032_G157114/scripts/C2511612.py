'''
Created on Jan 02, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227742
TestCase Name = Report-Other: Verify Visualize icon works as expected for numeric columns
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.wftools import active_report
from common.lib import utillity

class C2511612_TestClass(BaseTestCase):

    def test_C2511612(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID='C2511612'
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
            
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266
                Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001a.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="Category")
        
        """
             Step 03 : Verify the report is generated.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: Verify report data")
        
        """
             Step 04 : Click the down arrow for Dollar Sales, to display the available options.
                Expect to see the following option available for Dollar Sales.
        """
        expected_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Export', 'Print', 'Window', 'Restore Original']
        miscelanousobj.verify_menu_items('ITableData0',5,None,expected_list,'Step 04.1 : Verify option available for Dollar Sales.')
        
        
        """
             Step 05 : Click the Visualize option.Verify that horizontal bars displayed for the column.
        """
        miscelanousobj.select_menu_items("ITableData0",5, "Visualize")
        time.sleep(4)
#         iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step01.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step01.xlsx', 'Step 05.1 : Verify Product column is no longer displayed on the report.')
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 05.2 : Verify page summary')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 5, 'light_gray', 'Step 05.3: Verify visualization added')
        
        """
             Step 06 :Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()
