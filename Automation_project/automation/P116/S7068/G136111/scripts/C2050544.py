'''
Created on Aug 10, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050544
Description : With Cache set ON, Filtering on DATE/DATETIME fields produce Fex or looping errors.
This does not occur with Cache set OFF. 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest
import time


class C2050544_TestClass(BaseTestCase):

    def test_C2050544(self):
        """
            Step 01: Run 153599.fex from the repro
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("153599.fex", "S7068", 'mrid', 'mrpass')
        header_css="table[id='IWindowBody0'] .arGridBar table>tbody table tbody tr td:nth-child(2)"
        utillobj.synchronize_with_visble_text(header_css, "1000of1000records,Page1of18", 45, 1)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the 153599.fex - Top Head line verification")
        
         
        utillobj.verify_data_set('ITableData0','I0r','153599.xlsx',"Step 01: Verify table loaded data correctly")
         
        #utillobj.create_data_set('ITableData0','I0r','153599.xlsx')
          
         
        """Step 02 : Select the Date YYMD field, then Filter and Not Equal."""
         
        miscelanousobj.select_menu_items('ITableData0', "2", "Filter","Not equal")
        utillobj.synchronize_with_number_of_element("#wall1", 1, 25, 1)
         
        #From the value box, select the first value - 1996/01/01 and click Filter.
         
        filterselectionobj.create_filter(1, 'Not equal', value1='1996/01/01' )
         
        filterselectionobj.filter_button_click('Filter')
        utillobj.synchronize_with_visble_text(header_css, "820of1000records,Page1of15", 45, 1)
 
        #Expect to see the report starting with 1996/02/01 and containing 820 lines.
        
         
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 01: Expect to see the report starting with 1996/02/01 and containing 820 lines")
         
        utillobj.verify_data_set('ITableData0','I0r','C2050544_Ds01.xlsx',"Step 01: Verify table loaded data correctly")
        #utillobj.create_data_set('ITableData0','I0r','C2050544_Ds01.xlsx')        
         
        """Step 03: Exit the Filter menu"""
 
        filterselectionobj.close_filter_dialog()
         
        #Expect to see the original 1000 line report.
        utillobj.synchronize_with_visble_text(header_css, "1000of1000records,Page1of18", 45, 1)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03:Expect to see the original 1000 line report. - Top Head line verification")
         
         
        utillobj.verify_data_set('ITableData0','I0r','153599.xlsx',"Step 03: Expect to see the original 1000 line report.")
         
        """Step 04: Select the DATETIME HYYMDSA field, then Filter and Not Equal."""
#         Expect to see the report starting with 5 rows of 2007/08/08 12:13:14PM, 5 rows of 2011/03/30 10:23:24PM, 
#         then transitioning to 2013/10/04 1:02:03AM, for a total of 995 lines.
         
        miscelanousobj.select_menu_items('ITableData0', "7", "Filter","Equals")
        utillobj.synchronize_with_number_of_element("#wall1", 1, 25, 1)
        
        #From the value box, select the first value - 2002/12/31 11:59:59PM, then click Filter.
        
        filterselectionobj.create_filter(1, 'Not equal', value1='2002/12/31 11:59:59PM' )
        
        filterselectionobj.filter_button_click('Filter')
        
        '''Actual issue http://172.19.2.43:8080/browse/ACT-1294. this is fixed in 82xx and 8203 builds. Hence enabling this verification point.'''
        
        utillobj.synchronize_with_visble_text(header_css, "995of1000records,Page1of18", 45, 1)
        miscelanousobj.verify_page_summary(0, '995of1000records,Page1of18', "Step 04:Expect to see the 995 line report. - Top Head line verification")
        #utillobj.create_data_set('ITableData0','I0r','C2050544_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2050544_Ds02.xlsx',"Step 04: Verify table loaded data correctly")
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        