'''
Created on Aug 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050523
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_pivot_comment
from common.lib import utillity
import unittest
import time
class C2050523_TestClass(BaseTestCase):

    def test_C2050523(self):
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
        select ALPHA Store Code and lastly, for ACROSS, select Date YYMD.
        """
        miscelanousobj.select_menu_items('ITableData0', "0", "Pivot (Cross Tab)","ALPHA Store Code","Date YYMD")
        
        """Expect to see a Grid(Matrix) Report with Order Number INTEGER"""
        
        utillobj.verify_pivot_data_set("piv1", "C2050523_Ds01.xlsx", "Step 02: Expect to see a Grid(Matrix) Report with Order Number INTEGER")
        
        """
        Step 03: From the options bar, click the first icon and select Group By(X) and select D10.2 Unit Price from the field list.
        """
        time.sleep(7)
        pivotobj.create_new_item('wall1', 0, "Group By (X)->D10.2 Unit Price")
        
        """
        Expect to see sort column D10.2 Unit Price to the right of ALPHA Store Code. 
        Each Store Code will be broken out by the values of Unit Price.
        """
        utillobj.verify_pivot_data_set("piv1", "C2050523_Ds02.xlsx", "Step 03: Expect to see sort column D10.2 Unit Price to the right of ALPHA Store Code")
        
if __name__ == '__main__':
    unittest.main()   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    