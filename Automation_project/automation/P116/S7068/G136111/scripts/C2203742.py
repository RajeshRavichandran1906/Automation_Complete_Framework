'''
Created on Aug 11, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203742
Description : AHTML Total Calculation DEFINE w decimal values. 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from selenium.webdriver import ActionChains
from common.lib import utillity
import unittest
import time


class C2203742_TestClass(BaseTestCase):

    def test_C2203742(self):
        """
            Step 01:  Execute the attached repro - 129369.fex

        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("129369.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(8)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01: Execute the 129369.fex - Top Head line verification")
        
        utillobj.verify_data_set('ITableData0','I0r','129369.xlsx',"Step 01: Verify table loaded data correctly")
        
        column_list=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'DEALER_COST', 'RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 129369.fex and Verify the column heading')
        
        
        """Step 02 : In the report select a cell with value SEDAN and select  'Filter Cell' option."""
        
        miscelanousobj.select_field_menu_items('ITableData0', 1, 3,'Filter Cell')
        #Verify that Filter cell returned all SEDAN value.  
        time.sleep(6)
        utillobj.verify_data_set('ITableData0','I0r','C2050552_Ds01.xlsx',"Step 02: Verify Filtered value only shows SEDAN")
        
        time.sleep(3)
        
        """Step 03: select a any row in bodytype and select 'Highlight row'."""
        #Expect to see the Filtered SEDAN rows with the first row highlighted
       
        miscelanousobj.select_field_menu_items('ITableData0', 0, 3,'Highlight Row')
        time.sleep(3)
        
        action = ActionChains(driver)
        action.move_by_offset(300,450).perform()
        time.sleep(3)
        
        utillobj.verify_data_set('ITableData0','rgb','C2050552_Ds02.xlsx',"Step 02: Verify Filtered value only shows SEDAN")
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        