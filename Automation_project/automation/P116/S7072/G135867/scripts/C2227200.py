'''
Created on Feb 02, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2227200

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_run
from common.lib import utillity
from selenium.webdriver.common.by import By
import time


class C2227200_TestClass(BaseTestCase):

    def test_C2227200(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
        Step 7. Execute the attached act-181-host.fex.fex
        Expect to seed the following Active report with links for each CAR
        
        """
        utillobj.active_run_fex_api_login("act-181-host.fex", "S7072", 'mrid', 'mrpass')
        utillobj._validate_page((By.ID,'ITableData0'))
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 07.a: Verified the Page Summary')
        column_list=['CAR', 'BODYTYPE']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07.b: Verify Column Heading')
          
        ia_runobj.verify_table_cell_property("table[id='ITableData0']", 8, 1,underline=True,font_color='blue',msg='Step 07.c1 : ALFA ROMEO CAR')
        ia_runobj.verify_table_cell_property("table[id='ITableData0']", 14, 1,underline=True,font_color='blue',msg='Step 07.c2 : BMW CAR')
        ia_runobj.verify_table_cell_property("table[id='ITableData0']", 19, 1,underline=True,font_color='blue',msg='Step 07.c3 : PEUGEOT CAR')
          
        utillobj.verify_data_set('ITableData0','I0r','C2227200_DS01.xlsx','Step 07.d : Data Set verified')

        
        
        """
        Step 8. Click on JAGUAR and select Drill Down 1
        The result, in a new browser tab or window, is a small report with CAR and COUNTRY for ENGLAND
        
        """
        
        miscelanousobj.select_field_menu_items('ITableData0', 0, 0,'DrillDown 1')
        
        utillobj.switch_to_window(1)
        utillobj._validate_page((By.ID,'ITableData0'))
        
        miscelanousobj.verify_page_summary(0, '3of3records,Page1of1', 'Step 08.a: Verified the Page Summary')
        column_list=['CAR', 'COUNTRY']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 08.b: Verify Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','C2227200_DS02.xlsx','Step 08.c : The small report is displayed with CAR and COUNTRY for ENGLAND')
        
        driver.close()
        utillobj.switch_to_window(0)
        
        time.sleep(2)
        
        
        
        """
        Step 9. Return to the original report, click on DATSUN, and select Drill Down 2.
        The small report now contains CAR, COUNTRY, and MODEL.
        
        """
        
        miscelanousobj.select_field_menu_items('ITableData0', 4, 0,'DrillDown 2')
        
        utillobj.switch_to_window(1)
        utillobj._validate_page((By.ID,'ITableData0'))
        
        miscelanousobj.verify_page_summary(0, '2of2records,Page1of1', 'Step 09.a: Verified the Page Summary')
        column_list=['CAR', 'COUNTRY','MODEL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09.b: Verify Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','C2227200_DS03.xlsx','Step 09.c : The small report is displayed with CAR and COUNTRY and MODEL')
        
        driver.close()
        utillobj.switch_to_window(0)
        

if __name__=='__main__' :
    
    unittest.main()