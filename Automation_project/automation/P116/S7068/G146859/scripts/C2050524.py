'''
Created on Aug 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050524
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_pivot_comment
from common.lib import utillity
import unittest

class C2050524_TestClass(BaseTestCase):

    def test_C2050524(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050524'
        """
            Step 01: Execute the AR-RP-193.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivotobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-193.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-193.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
        Step 02: Select Order Number INTEGER, select PIVOT(Cross Tab), then for Group By(SUM),
        select D10.2 Unit Price and lastly, for ACROSS, select the ALPHA Store Code field.
        """
        miscelanousobj.select_menu_items('ITableData0', "0", "Pivot (Cross Tab)","D10.2 Unit Price","ALPHA Store Code")
        utillobj.verify_pivot_data_set("piv1", "C2050524_Ds01.xlsx", "Step 02: Expect to see te Pivot Table.")
        
        """
        Step 03: In the box for D10.2 Unit Price, click the up arrow.
        """
        pivotobj.click_groupby_across_button("piv1", 2, 1, 1)
        utillobj.verify_pivot_data_set("piv1", "C2050524_Ds02.xlsx", "Step 03: Expect to see the D10.2 Unit Price sort column converted to a second Across")
        
        """
        Step 04: In the box for ALPHA Store Code, click the last icon indicated by 'X', to remove Date YYMD as an Across sort.
        """
        pivotobj.click_groupby_across_button("piv1", 1, 1, 4)
        utillobj.verify_pivot_data_set("piv1", "C2050524_Ds03.xlsx", "Step 04: Expect to see the report now sorting Across only by the D10.2 Unit Price values")
        
        
if __name__ == '__main__':
    unittest.main()   
        
        
        
        
        
        
        
        
        
        