'''
Created on Sept 01, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053847
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity


class C2053847_TestClass(BaseTestCase):

    def test_C2053847(self):
        
        """
        Step 01: Execute the attached repro - 131610a.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("131610a.fex", "S7078", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01: Execute the attached repro - 131610a.fex")
        columnslist=['COUNTRY', 'BODYTYPE', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", columnslist, 'Step 01a: Verify all columns listed on the report')
        utillobj.verify_data_set("ITableData0", "I0r", "C2053847_Ds01.xlsx", "Step 01b: Verify all columns data listed on the report")
        
        """
        Step 02: Create Sales > Pivot > Group By Country > Across Bodytype from active report menu
        """
        miscelanousobj.select_menu_items('ITableData0', "2", "Pivot (Cross Tab)","COUNTRY","BODYTYPE")
        utillobj.verify_pivot_data_set("piv1", "C2053847_Ds02.xlsx", "Step 02: Expect to see a Pivot Table")
        utillobj = utillity.UtillityMethods(self.driver)
        utillobj.infoassist_api_logout()
        driver.close    
        
        """
        Step 03: Execute the attached repro - 131610b.fex
        """
        utillobj.active_run_fex_api_login("131610b.fex", "S7078", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 03: Execute the attached repro - 131610a.fex")
        columnslist=['COUNTRY', 'BODYTYPE', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", columnslist, 'Step 03a: Verify all columns listed on the report')
        utillobj.verify_data_set("ITableData0", "I0r", "C2053847_Ds01.xlsx", "Step 03b: Verify all columns data listed on the report")
        
        """
        Step 04: Create Sales > Pivot > Group By Country > Across Bodytype from active report menu
        """
        miscelanousobj.select_menu_items('ITableData0', "2", "Pivot (Cross Tab)","COUNTRY","BODYTYPE")
        utillobj.verify_pivot_data_set("piv1", "C2053847_Ds03.xlsx", "Step 04: Expect to see the following Pivot table, displaying the missing data as 'n/a', provided by the SET NODATA = 'n/a' command in the Fex")
        #utillobj.create_pivot_data_set("piv1", "C2053847_Ds03.xlsx")
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
