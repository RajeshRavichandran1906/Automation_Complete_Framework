'''
Created on Aug 19, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2061409
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2061409_TestClass(BaseTestCase):

    def test_C2061409(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the attached repro - act478_cacheON.fex. 
        Expect to see the following Active Report, Cache is On.
        Verify that there are no columns that display suppressed data, indicating the presence of a BY phrase. No BYs exist for this report.
        Also note that there is no logical sequence to the data in any column, it occurs with no specific sorting.
        """
        utillobj.active_run_fex_api_login("act478_cacheON.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the act478_cacheON.fex and Verify the Report Heading')
        column_list=['COUNTRY', 'CAR', 'BODYTYPE', 'RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the act478_cacheON.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act478_cacheON.xlsx', 'Step 01.3: Execute the act478_cacheON.fex and Verify the entire data, to make sure there is no suppressed data.')
        """
        2. From the drop down for Retail_Cost, click the Sort Descending option.
        Expect to see the Active Report, now in descending order of Retail_Cost. 
        """
        
        miscelanousobj.select_menu_items('ITableData0', 3, 'Sort Descending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2061409_Ds01.xlsx', 'Step 02.1: After Sort Descending verify entire table and make sure the descending order of Retail_Cost.')
        """
        3. From the drop down for Retail_Cost, click the Restore Original option.
        Expect to see the same report, sorted in descending order by Retail_Cost. 
        The warning message confirms that it cannot restore the original because the original report had no specific order.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Restore Original')
        time.sleep(9)
        utillobj.verify_js_alert('Warning: Original sort could not be determined', 'Step 03.1: Verify the warning message')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2061409_Ds02.xlsx', 'Step 03.2: After Restore Original verify entire table and make sure we still get the same data.')
        """
        4. Click the OK button in the warning message dialogue box.
        From the drop down for Country, click the Sort Ascending option.
        Expect to see the warning message removed.
        Expect to see the Active Report, now in ascending order of Country.
        Also note that the Retail_Costs are still in descending order but now within Country.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2061409_Ds03.xlsx', 'Step 04.1: Verify table after sort ascending on country and make sure the retail_cost is still in descending order.')
        """
        5. From the drop down for Country, click the Restore Original option.
        Expect to see the same report, sorted in ascending order by Country.
        The warning message confirms that it cannot restore the original because the original report had no specific order.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Restore Original')
        time.sleep(9)
        utillobj.verify_js_alert('Warning: Original sort could not be determined', 'Step 05.1: Verify the warning message')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2061409_Ds04.xlsx', 'Step 05.2: After Restore Original verify entire table and make sure we still get the same data.')
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
        6. Click the OK button in the warning message dialogue box.
        Execute the attached repro - act478_cacheOFF.fex.
        Expect to see the following Active Report, Cache is Off.
        Verify that there are no columns that display suppressed data, indicating the presence of a BY phrase. No BYs exist for this report.
        Also note that there is no logical sequence to the data in any column, it occurs with no specific sorting.
        """
        utillobj.active_run_fex_api_login("act478_cacheOFF.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 06.1: Execute the act478_cacheOFF.fex and Verify the Report Heading')
        column_list=['COUNTRY', 'CAR', 'BODYTYPE', 'RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06.2: Execute the act478_cacheOFF.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act478_cacheOFF.xlsx', 'Step 06.3: Execute the act478_cacheOFF.fex and Verify the entire data, to make sure there is no suppressed data.')
        """
        7. From the drop down for Retail_Cost, click the Sort Ascending option.
        Expect to see the Active Report, now in ascending order of Retail_Cost.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2061409_Ds05.xlsx', 'Step 07.1: After Sort Ascending verify entire table and make sure the Ascending order of Retail_Cost.')
        """
        8. From the drop down for Country, click the Restore Original option.
        Expect to see the original unordered report re-appear.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Restore Original')
        time.sleep(9)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2061409_Ds06.xlsx', 'Step 08.1: Expect to see the original unordered report re-appear.')
        
        
if __name__ == '__main__':
    unittest.main()
    