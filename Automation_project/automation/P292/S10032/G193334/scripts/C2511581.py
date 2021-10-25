'''
Created on Dec 19, 2017

@author: mk14236/ Updated by : Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227775
TestCase Name = Report-Calculate: Verify user can use following Calculate menu options
'''

import unittest, time
from common.lib import utillity
from common.wftools import active_report
from common.pages import active_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2511581_TestClass(BaseTestCase):

    def test_C2511581(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        Test_Case_ID="C2511581"
        
        """
        Step 01: Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
        Step 02: Expand folder P292_S10032_G157266
        Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")  
        self.driver.set_page_load_timeout(100)
        """
        Step 03: Verify the report is generated.
        Expect to see the following 107 line report.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 03.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
        Step 04: Select Dollar Sales > Calculate
        Verify Calculate menu shows all the filter options mentioned in the Test Description
        """ 
        option=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        miscelanousobj.verify_menu_items('ITableData0', 5, 'Calculate', option, 'Step 04: Verify Calculate menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
         
        """
        Step 05: Select Calculate > Sum
        Verify Total Sum value is "46156290" displayed under column name.
        """ 
        miscelanousobj.select_menu_items("ITableData0", "5", "Calculate", "Sum")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 6, "Total Sum 46156290", True, "Step 05: Verify Total Sum value is '46156290' displayed under column name.")
        time.sleep(4)
         
        """
        Step 06: Select Calculate > Avg
        Expect to see the Total Sum replaced by a Total Avg of 431367
        """ 
        miscelanousobj.select_menu_items("ITableData0", "5", "Calculate", "Avg")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 6, "Total Avg 431367", True, "Step 06: Expect to see the Total Sum replaced by a Total Avg of 431367")
        time.sleep(4)
        
        """
        Step 07: Select Calculate > Min
        Expect to see the Total Avg replaced by a Total Min of 158995
        """ 
        miscelanousobj.select_menu_items("ITableData0", "5", "Calculate", "Min")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 6, "Total Min 158995", True, "Step 07: Expect to see the Total Avg replaced by a Total Min of 158995")
        time.sleep(4)
        
        """
        Step 08: Select Calculate > Max
        Expect to see the Total Min replaced by a Total Max of 1745509
        """ 
        miscelanousobj.select_menu_items("ITableData0", "5", "Calculate", "Max")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 6, "Total Max 1745509", True, "Step 08: Expect to see the Total Min replaced by a Total Max of 1745509")
        time.sleep(4)
        
        """
        Step 09: For Calculate options of Cnt & Cnt Dst, change the column used.
        Select State > Calculate > Count 
        Expect to see the Total Cnt of 107 under the State column.
        Total Max for Dollar Sales remains.       
        """ 
        miscelanousobj.select_menu_items("ITableData0", "3", "Calculate", "Count")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 4, "Total Cnt 107", True, "Step 09.1: Expect to see the Total Cnt of 107 under the State column.")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 6, "Total Max 1745509", True, "Step 09.2: Expect to see the Total Max for Dollar Sales remains.")
        time.sleep(4)
        
        """
        Step 10: Select State > Calculate > Cnt Dst
        Expect to see the Total Cnt replaced by a Total Cnt Dst of 11.
        """ 
        miscelanousobj.select_menu_items("ITableData0", "3", "Calculate", "Distinct")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 4, "Total Cnt Dist 11", True, "Step 10: Expect to see the Total Cnt replaced by a Total Cnt Dst of 11.")
        time.sleep(4)
        
        """
        Step 11: For Calculate option % of Total, change the column used.
        Select Unit Sales > Calculate > % of Total
        """ 
        miscelanousobj.select_menu_items("ITableData0", "4", "Calculate", "% of Total")
        time.sleep(4)
        
        """
        Expect to see a new column added to the right of Unit Sales. This represents the ratio of one Unit Sales row to the total for all Unit Sales.
        """
        miscelanousobj.verify_calculated_value(1, 6, "% of Total", True, "Step 11.1: Expect to see a new column added to the right of Unit Sales.")
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 11.2: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds02.xlsx', "Step 11.3: Expect to see a new column added to the right of Unit Sales")
#         utillobj.create_data_set('ITableData0','I0r','C2227775_Ds02.xlsx')
        time.sleep(4)
        
        """
        Step 12: Remove the % of Total column by Select Unit Sales > Calculate > Clear
        """ 
        miscelanousobj.select_menu_items("ITableData0", "4", "Calculate", "Clear")
        time.sleep(4)
        
        """
        Expect to see the % of Total column removed.
        """
        miscelanousobj.verify_calculated_value(1, 6, "% of Total", False, "Step 12.1: Expect to see the % of Total column removed.")
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 12.2: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx', "Step 12.3: verify report data shows 107 records")
        time.sleep(4)
        
        """
        Step 13: Remove the remaining Calculations by Select State > Calculate > Clear All
        """ 
        miscelanousobj.select_menu_items("ITableData0", "3", "Calculate", "Clear All")
        time.sleep(4)
        
        """
        Expect to see all Calculations removed from under all fields.
        """
        miscelanousobj.verify_calculated_value(2, 4, "Total Cnt Dist 11", False, "Step 13.1: Expect to see all Calculations removed from under all fields.")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(2, 6, "Total Max 1745509", False, "Step 13.2: Expect to see all Calculations removed from under all fields.")
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 13.3: Verify the page summary')
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds04.xlsx', "Step 13.4: verify report data")
        
        """ 
        Step 14: Dismiss the window and logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()