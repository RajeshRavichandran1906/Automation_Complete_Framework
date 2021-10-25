'''
Created on Aug 4, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050529
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools
from common.lib import utillity
import unittest

class C2050529_TestClass(BaseTestCase):

    def test_C2050529(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050529'
        """
            Step 01: Execute the AR-RP-193.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        activeToolsobj = active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-193.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-193.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
        Step 02: In the Active Report, select the Grid Tool from the drop down options of any field. 
        Drag the D10.2 Unit Price field to the top of the list.
        """
        miscelanousobj.select_menu_items('ITableData0', "0", "Grid Tool")
        activeToolsobj.grid_tool_drag_drop_items("gridtoolt1", "D10.2 Unit Price", 1, 0)
        """
        Step 03: Select OK to see the reordered Active Report.
        """
        activeToolsobj.grid_tool_close('gridtoolt1', 'Ok')
        utillobj.verify_data_set('ITableData0','I0r' ,"C2050529_Ds01.xlsx", "Step 03: Expect to see the reordered Active Report")
        
        """
        Step 04: Select Pivot(Cross Tab) from the drop down options for D10.2 Unit Price, 
        then select ALPHA Store Code as the Group By field and lastly, select Date YYMD as the Across column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Pivot (Cross Tab)","ALPHA Store Code","Date YYMD")
        """
        Expect to see a Pivot Table with Group By of ALPHA Store Code and Date YYMD as the Across sort.
        Success or failure is determined in the next step.
        """
        utillobj.verify_pivot_data_set('piv1', "C2050529_Ds02.xlsx","Step 04: Expect to see a Pivot Table with Group By of ALPHA Store Code and Date YYMD as the Across sort")
        
if __name__ == '__main__':
    unittest.main()   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        