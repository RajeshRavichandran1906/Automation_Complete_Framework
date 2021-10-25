'''
Created on Jul 28, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7069&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050642
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050642_TestClass(BaseTestCase):

    def test_C2050642(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - AR_calculate.fex
        Expect to see the following Active Report.
        """
        utillobj.active_run_fex_api_login("AR_calculate.fex", "S7069", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01: Execute the AR_calculate.fex and Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.1: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050642_Ds01.xlsx', 'Step 01.2: Verify the entire data set.')
        """
        Step 2. Click on the drop down for the State column. Select the Calculate option.
        Expect to see the available options for an alphanumeric field: Clear, Clear All, Count & Distinct
        """
        calculate_menu = ['Clear','Clear All', 'Count','Distinct']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Calculate', calculate_menu,'Step 02: Expect to see the available options for an alphanumeric field: Clear, Clear All, Count & Distinct')
        """
        Step 3. Select the Count option.
        Expect to see the Count aggregation for the State column.
        """
        temp_obj=driver.find_elements_by_css_selector("#ITableData0 td table td b span")
        temp_obj[-1].click()
        time.sleep(5)
        
        miscelanousobj.select_menu_items('ITableData0', 3, 'Calculate','Count')
        miscelanousobj.verify_calculated_value(2, 4, 'Total Cnt 107', True, 'Step 03: Expect to see Count aggregation for the State column as Total Cnt 107.')

if __name__ == '__main__':
    unittest.main()