'''
Created on Aug 02, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054134
TestCase Name = Verify Show all shows all the hidden columns
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2054134_TestClass(BaseTestCase):

    def test_C2054134(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the AR-AHTML-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
         
        """
        Step 02: Click drop down menu for Unit Sales column > Hide Column
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Hide Column')        
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 02.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.b: Verify that Unit Sales column is no more visible on the report')
        
        """
        Step 03: Click drop down menu for State column > Hide Column
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Hide Column')        
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 03.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03.b: Verify that State column is no more visible on the report')
          
        """
        Step 04: Click drop down menu for Dollar Sales column > Show Columns > Show All.
        """
        option=['Show All', 'State', 'Unit Sales']
        miscelanousobj.verify_menu_items('ITableData0',5,'Show Columns',option, 'Step 04: Verify show columns lists Show All, State and Unit Sales')
        ele = driver.find_element_by_css_selector("#TCOL_0_C_1")
        ele.click()
        time.sleep(3)
        miscelanousobj.select_menu_items('ITableData0', 5, 'Show Columns','Show All')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 04.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04.b: Verify that all the hidden columns (State and Unit Sales) are now visible')
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
