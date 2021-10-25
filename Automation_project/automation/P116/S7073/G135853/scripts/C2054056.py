'''
Created on Aug 08, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054056
TestCase Name = This test case adds and removes data visualization of numeric columns in an Active Report.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2054056_TestClass(BaseTestCase):

    def test_C2054056(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - Visualize.fex
        """
        utillobj.active_run_fex_api_login("visualize.fex", "S7073", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', 'Step 01.a: Verify the Report Heading')
        column_list=['Product Category', 'Product Subcategory', 'Discount', 'Gross Profit', 'Quantity Sold']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2054056_Ds_01.xlsx',"Step 01.c: Verify entire Data set in Page 1")
         
        """
        Step 02a: From the drop down arrow for Discount, select Visualize.
        Step 02b: From the drop down arrow for Gross Profit, select Visualize.
        Step 02c: From the drop down arrow for Quantity Sold, select Visualize.Click drop down menu for Unit Sales column > Visualize option
            Verify on selecting this option bars that reflect the value of the data display in a column to the right of the data.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Visualize')  
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 3, 'Visualize')  
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Visualize')  
        time.sleep(2)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 2, 'green', 'Step 02a: Verify visualization added')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'green', 'Step 02b: Verify visualization added')  
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 6, 'green', 'Step 02c: Verify visualization added')           
        time.sleep(5)        
        
        """
        Step 03a: From the drop down arrow for Discount, select Visualize.
        Step 03b: From the drop down arrow for Quantity Sold, select Visualize.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Visualize')  
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Visualize')  
        time.sleep(2)
        bar_col_count = driver.find_elements_by_css_selector("[id='ITableData0'] tr[id^='I0r7'] table table td")
        len(bar_col_count)
        bars = (len(bar_col_count) == 1)
        utillity.UtillityMethods.asequal(self,True, bars, 'Step 03a: Verify visualization column has been removed for Discounts and Gross_Profit')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'green', 'Step 03b: Verify visualization remains for Quantity Sold') 
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
