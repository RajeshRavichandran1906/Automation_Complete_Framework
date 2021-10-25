'''
Created on Sep 1, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053844
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools
from common.lib import utillity

class C2053844_TestClass(BaseTestCase):

    def test_C2053844(self):
        """
            TESTCASE VARIABLES
        """
        
        """
        Step 01: Generate the initial report by executing fex.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR_RP_CALCULATE.fex','S7078','mrid','mrpass')      
        misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000')
        
        """
        Step 02: In the Active Report, select the Grid Tool from the drop down options of any field. 
        Drag the D10.2 Unit Price field to the top of the list.
        Expect to see the Grid Tool to display the fields in the following order of presentation.
        """
        time.sleep(5)
        misobj.select_menu_items('ITableData0', 0, 'Grid Tool')
        toolobj.pivot_tool_drag_drop_items('gridtoolt1', 'Column Order', 'D10.2 Unit Price', 1, 'Column Order', 1)
        toolobj.pivot_tool_drag_drop_items('gridtoolt1', 'Column Order', 'Order Number INTEGER', 1, 'Column Order', 2)
        toolobj.grid_tool_verify_columns('gridtoolt1', 1,['Column Order', 'D10.2 Unit Price', 'Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'P9.2M Unit Price', 'Datetime HYYMDSA'],"Step 02.1: Verfiy Grid Tool Columns")
        
        """
        Step 03: Select OK to see the reordered Active Report.
        Expect to see the D10.2 Unit Price now the first column.
        """
        toolobj.grid_tool_close('gridtoolt1', 'Ok')
        column=['D10.2 Unit Price', 'Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'P9.2M Unit Price', 'Datetime HYYMDSA']
        misobj.verify_column_heading('ITableData0', column, "Step 03.1: Verify Dataset title")
        
        utillobj.create_data_set('ITableData0','I0r','C2053844_Ds01a.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2053844_Ds01a.xlsx',"Step 03.2: Verify Dataset D10.2 Unit Price is now the first column")
        
        """
        Step 04: Select Pivot(Cross Tab) from the drop down options for D10.2 Unit Price, then select ALPHA as the 
        Group By field and lastly, select Date YYMD as the Across column.
        Expect to see a Pivot Table with Group By of ALPHA Store Code and Date YYMD as the Across sort. 
        Success or failure is determined in the next step.
        """
        misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','ALPHA Store Code','Date YYMD')
        
        """
        Step 05: Inspect the Pivot Report and examine the values of the Group By, Across & cell data.
        """
        utillobj.verify_pivot_data_set('piv1', 'C2053844_Ds02.xlsx', "Step 04.1: Verify Pivot dataset")
         

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
