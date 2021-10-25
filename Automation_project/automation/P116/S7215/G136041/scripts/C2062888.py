'''
Created on Sep 20, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7125
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2062888
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest, time

class C2062888_TestClass(BaseTestCase):

    def test_C2062888(self):
        
        """
            Step 01:Execute the attached repro - ACT-430.fex.
            
            Expect to see the following Active Report, with Subhead text and Subtotals for each Car.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("ACT-430.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the ACT-430.fex page summary verification")
        column_list=['COUNTRY', 'CAR', 'MODEL', 'RETAIL_COST']
        
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT-430.xlsx','Step 01.3: Verify data set')
        
        #utillobj.create_data_set('ITableData0', 'I0r', 'ACT-430.xlsx')
        
        
        """
        Step 02: From the Active drop down control for Country, select Sort Descending..
        """
        #Expect to see the report now in descending sequence of Country.
        #Also expect to see the Subhead text and Subtotals remain.
        #The Subtotal amounts should not change from step1.
        
        miscelanousobj.select_menu_items("ITableData0", "2", "Sort Descending")
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2062888_Ds01.xlsx','Step 02: Verify data set')
        
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2062888_Ds01.xlsx')
        
        """
        Step 03: From the drop down list for Country, select Restore Original.
        From the drop down list for Car, select Sort Descending.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Restore Original')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT-430.xlsx','Step 03.1: Verify data set restore original')
        
        miscelanousobj.select_menu_items('ITableData0', 3, 'Sort Descending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2062888_Ds02.xlsx','Step 03.2: Expect to see the report in descending Car sequence., Expect to see the Subhead text and the Subtotals removed.')
        
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2062888_Ds02.xlsx')
         
        
        
        """Step 04: From the drop down list for Country, select Restore Original.
        From the drop down list for Retail_Cost, select Sort Ascending."""
        
        miscelanousobj.select_menu_items('ITableData0', 5, 'Restore Original')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'ACT-430.xlsx','Step 04.1: Verify data set restore original')
        
        miscelanousobj.select_menu_items('ITableData0', 5, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2062888_Ds03.xlsx','Step 04.2: Expect to see the report in Ascending Retail_Cost sequence., Expect to see the Subhead text and the Subtotals removed.')
        
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2062888_Ds03.xlsx')
        
    
        
        
if __name__ == '__main__':
    unittest.main()               
        
        
        