'''
Created on January 25, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227755
TestCase Name =Report-Other: Verify that cells can be Filtered directly via the Report content.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity
from common.wftools import active_report

class C2511624_TestClass(BaseTestCase):

    def test_C2511624(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511624'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :   Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03 : Verify the report is generated
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
            
        """
            Step 04 :Click on report body for Category - 'Coffee'.
            Expect to see the following cell options for Category 'Coffee'.
        """
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell'], 'Step 04.1 : Verify Expect to see the following cell options for Category "Coffee"')
        
        """
            Step 05 : Click the Filter cell option.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 0, 'Filter Cell')
        time.sleep(3)
        
        """
            Step 05.1 : Verify that only values for Category = Coffee are displayed on the report.
        """
        miscelanousobj.verify_page_summary('0','30of107records,Page1of1','Step 05.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step05.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step05.xlsx', 'Step 05.2 : Verify that only values for Category = Coffee are displayed on the report.')
        
        """
            Step 06 : Click on the Filtered report body for Product - 'Latte'.
            Expect to see the following cell options for Product 'Latte'.
        """
        miscelanousobj.verify_field_menu_items('ITableData0', 11, 2, ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell', 'Remove Cell Filter'], 'Step 06.1 : Verify Expect to see the following cell options for Product "Latte"')
        
        """
            Step 07 : Click the Filter cell option.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 11, 2, 'Filter Cell')
        time.sleep(3)
        
        """
            Step 07.1 : Verify that only rows with Category = 'Coffee' and Product = 'Latte' are on the report.
        """
        miscelanousobj.verify_page_summary('0','11of107records,Page1of1','Step 07.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step07.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step07.xlsx', 'Step 07.2 : Verify that only rows with Category = "Coffee" and Product = "Latte" are on the report.')
        
        """
            Step 08 : Click on the first row for Category - 'Coffee'.
            Expect to see the following cell options for Category 'Coffee'.
        """
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell', 'Remove Cell Filter'], 'Step 08.1 : Expect to see the following cell options for Category "Coffee"')
        
        """
            Step 09 : Click the Filter cell option.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 0, 'Filter Cell')
        time.sleep(3)
        
        """
            Step 09.1 : Expect to see both sets of Filters removed, both for Category and Product.
        """
        miscelanousobj.verify_page_summary('0','30of107records,Page1of1','Step 09.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step09.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step09.xlsx', 'Step 09.2 : Verify Expect to see both sets of Filters removed, both for Category and Product.')
        
        """
            Step 10 : Click on the first row for Product - 'Espresso'. On context menu click Filter cell option.
            Verify all the values for Product = Espresso are displayed on the report.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 2, 'Filter Cell')
        time.sleep(3)
        miscelanousobj.verify_page_summary('0','11of107records,Page1of1','Step 10.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step10.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step10.xlsx', 'Step 10.2 : Verify all the values for Product = Espresso are displayed on the report.')
        
        """
            Step 11 : Click on the first row for State - 'CA'. On context menu click Filter cell option.
            Expect to see the previous Filter replaced by only rows containing CA, for all Categories and Products.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 3, 'Filter Cell')
        time.sleep(3)
        miscelanousobj.verify_page_summary('0','10of107records,Page1of1','Step 11.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step11.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds_Step11.xlsx', 'Step 11.2 : Verify Expect to see the previous Filter replaced by only rows containing CA, for all Categories and Products.')
        
        """
            Step 12 : Click on the first row for Product - 'Espresso'. On context menu click Remove Filter cell option.
            Expect to see the full report again.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 2, 'Remove Cell Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 12.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 12.2: verify report data")
        
if __name__=='__main__' :
    unittest.main()