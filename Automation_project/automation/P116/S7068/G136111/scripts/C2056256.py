'''
Created on Aug 4, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2056256


No project.
HotTrack case 21112531.

When choosing to do a filter on an active report, if you choose more than one item to filter, the second item isnt filtered out of the report.

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages import active_pivot_comment  
from common.lib import utillity
import unittest
import time
import re

class C2056256_TestClass(BaseTestCase):

    def test_C2056256(self):
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2056256'
        
        """
            Run the attached act-81.fex. Note that the 3rd row has values of $7,513.00, ENGLAND, and JENSEN, and there are 4 rows with ITALY. 
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(45) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("act-81.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
       
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01:  Expect to see the following Active Report. - page summary verification")
        
         
        utillobj.verify_data_set('ITableData0','I0r','act-81.xlsx',"Step 01: Verify Page data loaded correctly ")
        
        #utillobj.create_data_set('ITableData0','I0r','act-81.xlsx')
        
        """Step 02 : Click on the Compute_1 drop down arrow, select Filter, click on Not Equal. 
        """
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Filter","Not equal")
        time.sleep(3)
        
        """Step 03: Click on drop down arrow for values (empty box), click on $7,513.00."""
        
        filterselectionobj.create_filter(1, 'Not equal', value1='$7,513.00')
        
        
        """Step 04: Click on Filter. If necessary to see the result, move the filter box away from the report. 
        The row with $7,513.00 should not be there.."""
        
        filterselectionobj.filter_button_click('Filter')
        time.sleep(5)
        
        utillobj.verify_data_set('ITableData0','I0r','C2056256_Ds01.xlsx',"Step 04: Verify Page data loaded correctly The row with $7,513.00 should not be there.")
        
        #utillobj.create_data_set('ITableData0','I0r','C2056256_Ds01.xlsx')
        
        miscelanousobj.verify_page_summary(0, '17of18records,Page1of1', "Step 04:  Expect to see the following Active Report. - page summary verification")
        
       
        """Step 05: Go back to the filter box, click on Add Condition, click on COUNTRY, click on the left drop down arrow for the new condition,
         click on Not Equal, click on the right drop down arrow for the new condition, and click on ITALY. """
        
        filterselectionobj.add_condition_field("COUNTRY")
        
        filterselectionobj.create_filter(2, 'Not equal', value1='ITALY')
        
        
        """Step 06: Click on Filter. If necessary to see the result, move the filter box away from the report. 
        The rows with ITALY should not be there."""
        
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        utillobj.verify_data_set('ITableData0','I0r','C2056256_Ds02.xlsx',"Step 06: Verify Page data loaded correctly The rows with ITALY should not be there.")
        
        #utillobj.create_data_set('ITableData0','I0r','C2056256_Ds02.xlsx')
        
        miscelanousobj.verify_page_summary(0, '13of18records,Page1of1', "Step 06:  Expect to see the following Active Report. - page summary verification")
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        