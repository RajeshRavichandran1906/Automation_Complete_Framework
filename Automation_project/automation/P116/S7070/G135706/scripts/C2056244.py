'''
Created on Aug 19, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2056244
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2056244_TestClass(BaseTestCase):

    def test_C2056244(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the attached repro - cacheON_Restore.fex.
        Expect to see the following Active Report, with Cache On.
        """
        utillobj.active_run_fex_api_login("cacheON_Restore.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the cacheON_Restore.fex and Verify the Report Footing')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the cacheON_Restore.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'cacheON_Restore.xlsx', 'Step 01.3: Execute the cacheON_Restore.fex and Verify the entire data for Cache on.')
        """
        2. From the drop down for Unit Sales, click the Sort Descending option.
        Expect to see the Active Report, now in descending order of Unit Sales. 
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Sort Descending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2056244_Ds01.xlsx', 'Step 02.1: After Sort Descending verify entire table and make sure the descending order of Unit Sales.')
        """
        3. From the drop down for Unit Sales, click the Restore Original option.
        Expect to see the original report from step 1.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 4, 'Restore Original')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2056244_Ds02.xlsx', 'Step 03.1: Verify that report is set back to original state.')
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
        4. Execute the attached repro - cacheOFF_Restore.fex.
        Expect to see the following Active Report, with Cache Off.
        """
        utillobj.active_run_fex_api_login("cacheOFF_Restore.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 04.1: Execute the cacheOFF_Restore.fex and Verify the Report Footing')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04.2: Execute the cacheOFF_Restore.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'cacheOFF_Restore.xlsx', 'Step 04.3: Execute the cacheOFF_Restore.fex and Verify the entire data for Cache on.')
        """
        5. From the drop down for State, click the Sort Descending option.
        Expect to see the Active Report, now in descending order of State abbreviation.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 3, 'Sort Descending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2056244_Ds03.xlsx', 'Step 05.1: After Sort Descending verify entire table and make sure the descending order of State field.')
        
        """
        6. From the drop down for State, click the Restore Original option
        Expect to see the original report from step 4.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 3, 'Restore Original')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2056244_Ds04.xlsx', 'Step 06.1: Verify that report is set back to original state.')
        
if __name__ == '__main__':
    unittest.main()
        
