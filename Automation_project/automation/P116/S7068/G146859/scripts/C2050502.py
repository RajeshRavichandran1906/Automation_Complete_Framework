'''
Created on Jul 25, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050502
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050502_TestClass(BaseTestCase):

    def test_C2050502(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050502'
        """
            Step 01: Execute the AR-RP-141CA.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Step 01: Execute the AR-RP-141CA.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')


        """
            Step 02: For each field, including INTEGER, D10.2 and P9.2M, 
            click the down arrow in the heading, then select CALCULATE. 
            Then select SUM from the drop down options
            Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        """
        option = ['Clear','Clear All','Sum','Avg','Min','Max','Count','Distinct','% of Total']
        miscelanousobj.verify_menu_items('ITableData0', 0, "Calculate", option,"Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total")
        
        miscelanousobj.select_menu_items('ITableData0', "0", "Calculate","Sum")
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", True, "Step 02: Expect to see Total Sum 500500")
        
        miscelanousobj.select_menu_items('ITableData0', "5", "Calculate","Sum")
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 59,503.00", True, "Step 02: Expect to see Total Sum 59,503")
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", True, "Step 02: Expect to see Total Sum 500500 after adding 2nd sum field")
        
        miscelanousobj.select_menu_items('ITableData0', "6", "Calculate","Sum")
        miscelanousobj.verify_calculated_value(4, 7, "Total Sum $560,003.00", True, "Step 02: Expect to see Total Sum $560003.00")
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 59,503.00", True, "Step 02: Expect to see Total Sum 59503 after adding the 3rd sum field")
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500",True, "Step 02: Expect to see Total Sum 500500 after adding the 3rd sum field")
        """
            Step 03: End the Filter panel in preparation for the next field in the GROUP.
            Make sure the report is positioned at Page 1.
            Expect full report to be displayed again. 1000 rows
        """
        miscelanousobj.select_menu_items('ITableData0', "0", "Calculate","Clear All")
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", False, "Step 03: Verify Calculated value cleared in INTEGER column")
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 500500", False, "Step 03: Verify Calculated value cleared in D10.2 column")
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 500500", False, "Step 03: Verify Calculated value cleared in P9.2M column")
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03: Expect full report to be displayed again. 1000 rows')
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        