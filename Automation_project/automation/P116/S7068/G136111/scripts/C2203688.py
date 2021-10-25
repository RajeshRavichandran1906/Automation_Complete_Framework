'''
Created on Aug 2, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050563
Description : 

AHTML:

Verify that only filtered records are printed



'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages import active_pivot_comment  
from common.lib import utillity
import unittest
import time


class C2203688_TestClass(BaseTestCase):

    def test_C2203688(self):
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2203688'
        
        """
            Step 01: Execute the AR-RP-001.fex
        """
        #Verify correct output displayed on run. Pagination toolbar is present on the top.
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
       
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01:  Expect to see the following Active Report. - page summary verification")
         
         
        """Step 02 :  Click on the arrow for Unit_sales and from the popup menu select Filter->Greater than  """
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than")
        time.sleep(4)
        #Verify Filter Selection pop up opened
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02: Select Filter > Greater than',['Unit Sales', 'Greater than'])
        
        """Step 03: Click the down arrow in the value edit box and select 45,355 value and click on Filter button."""
        
        filterselectionobj.create_filter(1, 'Greater than','large', value1='45355')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        #Verify correct records are filtered.
        miscelanousobj.verify_page_summary(0, '27of107records,Page1of1', "Step 03:  Expect to see the following Active Report. - page summary verification after filter applied ")
        
        utillobj.verify_data_set('ITableData0','I0r','C2203688_Ds01.xlsx',"Step 03.3: Verify entire Data set in Page")
        #utillobj.create_data_set('ITableData0','I0r','C2203688_Ds01.xlsx')
        
        miscelanousobj.move_active_popup("1", "600", "200")
        time.sleep(3)
        
        """Step 04: Click on the down arrow for any field and from the popup menu select Print->Filtered only"""
        
        #Verify that the filtered data opens as plain html output in a new window and the print dialogue pops up with the configured printers.
        miscelanousobj.select_menu_items("ITableData0", "4", "Print","Filtered only")
        time.sleep(10)
        
        """Step 05: Click Print"""
        
        #Verify filtered records are printed.
        utillobj.autoit_print("Step 04: Expect to see a confirmation message from the Printer services menu")
        
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        