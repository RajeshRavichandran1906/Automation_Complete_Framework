
'''
Created on July 29, 2016
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7069
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055525
'''
__author__ = "Nasir"
__copyright__ = "IBI"

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity


class C2055525_TestClass(BaseTestCase):

    def test_C2055525(self):

        step1="""Step 01:  Execute the attached repro - 92382.fex """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('92382.fex','S7069','mrid','mrpass')
        time.sleep(10)
        utillobj.capture_screenshot('01.00', step1)  
        active_misobj.verify_page_summary('0','12of12records,Page1of1', 'Step 01a: Verify Page summary')
        column=['CURR_SAL','HIRE_DATE', 'EFFECT_DATE', 'LAST_NAME', 'LAST_NAME']
        miscelanousobj.verify_column_heading('ITableData0',column, "Step 01b: Expect to see five columns")
        miscelanousobj.verify_calculated_value('1', '4', "DEPARTMENT", True, "Step 01c: Verify Department displayed on heading") 
        miscelanousobj.verify_calculated_value('2', '4', "MIS", True, "Step 01d: Verify MIS displayed on heading")
        miscelanousobj.verify_calculated_value('2', '5', "PRODUCTION", True, "Step 01e: Verify PRODUCTION displayed on heading")  
        utillobj.verify_data_set('ITableData0','I0r','C2055525.xlsx',"Step 01f: Verify entire Data set in Page 1")
        utillobj.capture_screenshot('01.01', step1)
        step2="""Step 02: Select Calculate option using any dropdown from report.""" 
        step3="""Step 03: Select Min from the calculate option."""
        miscelanousobj.select_menu_items('ITableData0', '1', 'Calculate', 'Min')
        utillobj.capture_screenshot('02.00', step2)
        utillobj.synchronize_until_element_is_visible('td span.arGridAgg', 190)
        step03 = 'Step 03 : Verify Total Min is applied for HIRE_DATE column and same is displayed under the column heading Verify the value: Total Min 80/06/02'
        miscelanousobj.verify_calculated_value('4', '2', "Total Min 80/06/02", True, step03)  
        utillobj.capture_screenshot('03.00', step3)
        
        step4="""Step 04: Select Calculate option using any dropdown from report.""" 
        step5="""Step 05: Select Min from the calculate option."""
        miscelanousobj.select_menu_items('ITableData0', '2', 'Calculate', 'Max')
        utillobj.capture_screenshot('04.00', step4)
        utillobj.synchronize_until_element_is_visible('td span.arGridAgg', 190)
        step05 = 'Step 05 : Verify Total Max is applied for EFFECT_DATE column and same is displayed under the column heading Verify the value: Total Max 84/09/01'
        miscelanousobj.verify_calculated_value('4', '3', "Total Max 84/09/01", True, step05) 
        utillobj.capture_screenshot('05.00', step5)

if __name__ == '__main__':
    unittest.main()

