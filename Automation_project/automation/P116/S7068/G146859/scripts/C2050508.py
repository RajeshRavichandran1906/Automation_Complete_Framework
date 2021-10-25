'''
Created on Jul 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050508
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2050508_TestClass(BaseTestCase):

    def test_C2050508(self):
        """
            Step 01: Execute the AR-RP-141CA.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Step 01: Execute the AR-RP-141CA.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
            Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        """
        option = ['Clear','Clear All','Sum','Avg','Min','Max','Count','Distinct','% of Total']
        miscelanousobj.verify_menu_items('ITableData0', 0, "Calculate", option,"Step 02: Step 02: Expect to see all options")
        
        """select INTEGER, then MAX"""
        miscelanousobj.select_menu_items('ITableData0', "0", "Calculate","Max")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1,000")
        
        """select Date YYMD , then MAX"""
        miscelanousobj.select_menu_items('ITableData0', "2", "Calculate","Max")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 3, "Total Max 1996/06/01", True, "Step 02: Expect to see Total Max 1996/06/01")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1,000 after adding 2nd calculate field")
        
        """select D10.2, then MAX"""
        miscelanousobj.select_menu_items('ITableData0', "5", "Calculate","Max")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 6, "Total Max 140.00", True, "Step 02: Expect to see Total Max 140.00")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1,000 after adding 3rd calculate field")
        miscelanousobj.verify_calculated_value(4, 3, "Total Max 1996/06/01", True, "Step 02: Expect to see Total Max 1996/06/01 after adding 3rd calculate field")
        
        """select P9.2M, then MAX"""
        miscelanousobj.select_menu_items('ITableData0', "6", "Calculate","Max")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 7, "Total Max $1,139.00",True,"Step 02: Expect to see Total Max $1,139.00")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1,000 after adding 4th calculate field")
        miscelanousobj.verify_calculated_value(4, 3, "Total Max 1996/06/01", True, "Step 02: Expect to see Total Max 1996/06/01 after adding 4th calculate field")
        miscelanousobj.verify_calculated_value(4, 6, "Total Max 140.00", True, "Step 02: Expect to see Total Max 140.00 after adding 4th calculate field")
        
        """select DATETIME, then MAX"""
        miscelanousobj.select_menu_items('ITableData0', "7", "Calculate","Max")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 8, "Total Max 2013/10/04 1:02:03AM",True,"Step 02: Expect to see Total Max 2013/10/04 1:02:03AM")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1,000 after adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 3, "Total Max 1996/06/01", True, "Step 02: Expect to see Total Max 1996/06/01 after adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 6, "Total Max 140.00", True, "Step 02: Expect to see Total Max 140.00 after adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 7, "Total Max $1,139.00",True,"Step 02: Expect to see Total Max $1,139.00 after adding 5th calculate field") 
        
        """
            Step 03: End the Filter panel in preparation for the next field in the GROUP.
            Make sure the report is positioned at Page 1.
        """
        miscelanousobj.select_menu_items('ITableData0', "0", "Calculate","Clear All")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",False,"Step 02: Verify Total Max 1,000 cleared")
        miscelanousobj.verify_calculated_value(4, 3, "Total Max 1996/06/01", False, "Step 02: VerifyTotal Max 1996/06/01 cleared")
        miscelanousobj.verify_calculated_value(4, 6, "Total Max 140.00", False, "Step 02: Verify Total Max 140.00 cleared")
        miscelanousobj.verify_calculated_value(4, 7, "Total Max $1,139.00",False,"Step 02: Verify Total Max $1,139.00 cleared")
        miscelanousobj.verify_calculated_value(4, 8, "Total Max 2013/10/04 1:02:03AM",False,"Step 02: Verify Total Max 2013/10/04 1:02:03AM cleared")
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03: Expect full report to be displayed again. 1000 rows')
        
if __name__ == '__main__':
    unittest.main()   
        
        
        
        
        