'''
Created on Aug 10, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050521
Description : AHTML Total Calculation DEFINE w decimal values. 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest, time

class C2050545_TestClass(BaseTestCase):

    def test_C2050545(self):
        """
            Step 01: Run 90480.fex from repro location
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("90480.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(8)
        
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01: Execute the 90480.fex - Top Head line verification")
        
        
        utillobj.verify_data_set('ITableData0','I0r','90480.xlsx',"Step 01: Verify table loaded data correctly")
        
        #utillobj.create_data_set('ITableData0','I0r','90480.xlsx')
         
        
        """Step 02 : select Unit Sales--> calculate--> sum"""
        
        miscelanousobj.select_menu_items('ITableData0', "4", "Calculate","Sum")
        time.sleep(8)
        
        miscelanousobj.verify_calculated_value(2, 5, "Total Sum 3688991",True, "Step 02: Verify Total Sum - TOT displayed on pagination bar")
           
        
        """Step 03: select Dollar Sales--> filter--> greater then"""
        #select value 212057
        miscelanousobj.select_menu_items('ITableData0', "3", "Filter","Greater than")
        time.sleep(3) 
        filterselectionobj.create_filter(1, 'Greater than', 'large',value1='212057' )
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        miscelanousobj.verify_calculated_value(2, 5, "Filtered Sum 3292732(89.26%)\nTotal Sum 3688991",True, "Step 03: Verify Total Sum - TOT displayed on pagination bar")
        
        #filterselectionobj.close_filter_dialog()
        
        time.sleep(2)
        
        
        miscelanousobj.verify_page_summary(0, '81of107records,Page1of2', "Step 03:Expect to see the original 1000 line report. - Top Head line verification")
        
        time.sleep(5)
        
        filterselectionobj.close_filter_dialog() 
        
        """Step 04: select Dollar Sales-->filter--> less then  select value 212057"""
        #verify filter sum value get changed according to filter
        
        miscelanousobj.select_menu_items('ITableData0', "3", "Filter","Less than")
        time.sleep(3) 
        filterselectionobj.create_filter(1, 'Less than', 'large',value1='212057' )
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        miscelanousobj.verify_calculated_value(2, 5, "Filtered Sum 380114(10.3%)\nTotal Sum 3688991",True, "Step 04: Verify Total Sum - TOT displayed on pagination bar")
        
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '25of107records,Page1of1', "Step 03:Expect to see the original 1000 line report. - Top Head line verification")
        
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        