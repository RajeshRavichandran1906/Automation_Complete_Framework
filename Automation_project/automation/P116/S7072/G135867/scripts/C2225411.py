'''
Created on Feb 2, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2225411

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2225411_TestClass(BaseTestCase):

    def test_C2225411(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 1. Execute the AR-RP-001.fex
        
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        
        utillobj._validate_page((By.ID,'ITableData0'))
        
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.a: Verified the Page Summary')
        column_list=['Category', 'Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verified Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001.xlsx','Step 01.c : Data set verified')
        
        """"
        Step 2 :Right click on the report.
        
        Verify Context menu pop up is opened. That shows these sub menus: 
        - Comments 
        - Highlight Value 
        - Highlight Row 
        - Unhighlight All 
        - Filter Cell.
        
        """
        miscelanousobj.verify_field_menu_items("ITableData0", 19, 1, ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell'], "Step 02 :Verified Context menu pop up is opened and sub menus are shown as expected")
        
        """
        Step 3. Select cell value and click Filter cell option on column value. Eg: Latte
        
        Verify all the values where Product = Latte are displayed on the report.
            
        """
        miscelanousobj.select_field_menu_items('ITableData0', 19, 1,'Filter Cell')
        miscelanousobj.verify_page_summary(0, '11of107records,Page1of1', 'Step 03.a: Verified the Page Summary')
        column_list=['Category', 'Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03.b: Verified Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001_DS01.xlsx','Step 03.c: Verify all the values where Product = Latte are displayed on the report')
        

if __name__=='__main__' :
    unittest.main()