'''
Created on Dec 18, 2017

@author: Magesh/ Updated by : Bhagavathi

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227791
TestCase Name = Report-Filter: Verify that multiple Filter conditions can be added individually and each condition may be removed separately.
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2511580_TestClass(BaseTestCase):

    def test_C2511580(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        Test_Case_ID="C2511580"
        
        """
        Step 01: Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
        Step 02: Expand folder P292_S10032_G157266
        Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141") 
        
        """
        Step 03: Verify the report is generated.
        Expect to see the following 107 line report.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 03.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
        Step 04: Select State > Filter > Equals
        From the State drop down, select MA.
        Click the Filter button.
        """ 
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Filter', option, 'Step 04: Verify Filter menu shows all the filter options mentioned in the Test Description.')
        time.sleep(4)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Equals")
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04.1: Verify Filter that the selection menu appears:',['State', 'Equals'])
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 04.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(1, 'Equals', value1='MA')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
         
        """ 
        Expect to see the first Filter produce 10 rows of State MA.
        """
        miscelanousobj.verify_page_summary('0','10of107records,Page1of1', 'Step 04.3: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds02.xlsx', 'Step 04.4: Verify that report containing 10 rows of State MA.')
#         utillobj.create_data_set('ITableData0','I0r','C2227791_Ds02.xlsx')
        time.sleep(5)
         
         
        """
        Step 05: Select Add Condition and select the Product field.
        Make sure the Operator is set to AND.
        Change the operator to Not Equal
        From the Product drop down, select Coffee Grinder and Coffee Pot.
        Click the Filter button. 
        """ 
        filterselectionobj.add_condition_field('Product')
        time.sleep(4)
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 05.1: Verify Filter that the selection menu appears:',['Product', 'Equals'],row_num=3)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 05.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(2, 'Not equal', value1='Coffee Grinder', value2='Coffee Pot')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
         
        """ 
        Expect to see the second Filter produce 8 rows, eliminating Coffee Grinder and Coffee Pot from the first Filter.
        """
        miscelanousobj.verify_page_summary('0','8of107records,Page1of1', 'Step 05.3: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx', 'Step 05.4: Verify that report now with 8 records, eliminating Coffee Grinder and Coffee Pot from the first Filter.')
#         utillobj.create_data_set('ITableData0','I0r','C2227791_Ds03.xlsx')
        time.sleep(4)
        
        """
        Step 06: Select Add Condition and select the Unit Sales field.
        Make sure the Operator is set to AND.
        Change the Condition to Greater Than.
        From the Unit Sales drop down, select value 19698.
        Click the Filter button.
        """ 
        filterselectionobj.add_condition_field('Unit Sales')
        time.sleep(4)
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 06.1: Verify Filter that the selection menu appears:',['Unit Sales', 'Equals'],row_num=4)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 06.2: Verify Filter that the selection menu appears:")
        filterselectionobj.create_filter(3, 'Greater than', 'large', value1='19698')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
         
        """ 
        Expect to see the third Filter produce 5 rows, eliminating Unit Sales of 19698 and above form the first two Filters.
        """
        miscelanousobj.verify_page_summary('0','5of107records,Page1of1', 'Step 06.3: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx', 'Step 06.4: Verify that report now with 5 rows, eliminating Unit Sales of 19698 and above form the first two Filters.')
#         utillobj.create_data_set('ITableData0','I0r','C2227791_Ds04.xlsx')
        time.sleep(4)
         
        """
        Step 07: Now remove the first Filter by clicking the "X" next to State and click Filter button.
        """ 
        filterselectionobj.delete_filter(1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Expect to see 71 rows. Scroll to the last page of the report to verify that Coffee Grinder and Coffee Pot are still not shown for Category Gifts.
        """
        miscelanousobj.verify_page_summary('0','71of107records,Page1of2', 'Step 07.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds05.xlsx', 'Step 07.2: Expect to see 71 rows. Scroll to the last page of the report to verify that Coffee Grinder and Coffee Pot are still not shown for Category Gifts')
#         utillobj.create_data_set('ITableData0','I0r','C2227791_Ds05.xlsx')
        time.sleep(4)
        
        
        """
        Step 08: Now remove the second Filter by clicking the "X" next to Product and click Filter button.
        """ 
        filterselectionobj.delete_filter(1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Expect to see 73 rows, with Coffee Grinder and Coffee Pot added. Scroll to the last page of the report to verify that Coffee Grinder and Coffee Pot are now shown shown for Category Gifts.
        """
        miscelanousobj.verify_page_summary('0','73of107records,Page1of2', 'Step 07.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds06.xlsx', 'Step 07.2: Expect to see 73 rows, with Coffee Grinder and Coffee Pot added. Scroll to the last page of the report to verify that Coffee Grinder and Coffee Pot are now shown shown for Category Gifts')
#         utillobj.create_data_set('ITableData0','I0r','C2227791_Ds06.xlsx')
        time.sleep(4)
        
        """
        Step 09: Now remove the last Filter by clicking the "X" next to Unit Sales and click Filter button.
        """ 
        filterselectionobj.delete_filter(1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        """ 
        Expect to see the fill 107 row report as all Filters have now been removed.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', 'Step 09.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 09.2: verify report data")
        
        """ 
        Step 10: Dismiss the window and logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()