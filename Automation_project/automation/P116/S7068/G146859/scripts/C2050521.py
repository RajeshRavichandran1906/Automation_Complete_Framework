'''
Created on Jul 28, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050521
Description : AHTML Total Calculation DEFINE w decimal values. 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest
import time
import re

class C2050521_TestClass(BaseTestCase):

    def test_C2050521(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050521'
        """
            Step 01: Execute 10153568_fidelity.fex to produce the DEFINE field output.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(45) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("10153568_fidelity.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
        #Local Function to get values in table
        def loc(self, y, z,expected, msg):
            li = []
            for x in range(y, z):
                s=driver.find_element_by_css_selector(ActiveMiscelaneousLocators.itable_row.format(x)).text
                li.append(re.sub(r'\n', ' ',s.strip()))
            utillobj.asequal(li,expected,msg) 
            
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01: Execute the 10153568_fidelity.fex - Top Head line verification")
        
        """Verify that Total Sum for MYFIELD = 208,420.001008"""
        #Verify that user is able to put 6 place decimal points 
         
        utillobj.verify_data_set('ITableData0','I0r','10153568_fidelity.xlsx',"Step 01: Verify that user is able to put 6 place decimal points ")
        
        #utillobj.create_data_set('ITableData0','I0r','10153568_fidelity.xlsx')
        decimalsval = ['208420 208,420.001008', 'Total Sum 208420 Total Sum 208,420.001008']
        
        loc(self,21,23,decimalsval, "Step 02: Verify that user is able to put 6 place decimal points -Total Sum values verification ")
        utillobj.infoassist_api_logout()
        
        """Step 02 : Execute 10153568_a.fex As the fex code is set to MYFIELD/D20.6 = SALES + .1234567"""
        utillobj.active_run_fex_api_login("10153568_a.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 02: Execute the 10153568_a.fex - Top Head line verification")
        #Verify that Total Sum for MYFIELD = 208,422.222221
         
        utillobj.verify_data_set('ITableData0','I0r','10153568_a.xlsx',"Step 02: Verify that user is able to put 6 place decimal points only. If 7th place is added, it will show up to 6 places only.")
        
        #utillobj.create_data_set('ITableData0','I0r','10153568_a.xlsx')
        decimalsval = ['208420 208,422.222221', 'Total Sum 208420 Total Sum 208,422.222226']
        
        loc(self,21,23,decimalsval, "Step 02: Verify that Total Sum for MYFIELD = 208,422.222221 ")
        utillobj.infoassist_api_logout()
        
        """Step 03:Execute 10153568_b.fex As the fex code is set to MYFIELD/D20.4 = SALES + .12345"""
        
        utillobj.active_run_fex_api_login("10153568_b.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 03: Execute the 10153568_b.fex - Top Head line verification")
        #Verify that Total Sum for MYFIELD = 208,422.2221
         
        utillobj.verify_data_set('ITableData0','I0r','10153568_b.xlsx',"Step 03: Verify that user is able to put 4 place decimal points only. If 5th place is added, it will show upto 4 places only as we have code (D20.4)")
        
        #utillobj.create_data_set('ITableData0','I0r','10153568_b.xlsx')
        decimalsval = ['208420 208,422.2221', 'Total Sum 208420 Total Sum 208,422.2225']
        
        loc(self,21,23,decimalsval, "Step 03: Verify that Total Sum for MYFIELD = 208,422.2221 ")
        utillobj.infoassist_api_logout()
        
        
        """Step 04:Execute 10153568_c.fex As the fex code is set to MYFIELD/D32.30= SALES + .12345"""
        
        utillobj.active_run_fex_api_login("10153568_c.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 04: Execute the 10153568_c.fex - Top Head line verification")
        #Verify that Total Sum for MYFIELD = 0.620000000000000000000000000000
         
        utillobj.verify_data_set('ITableData0','I0r','10153568_c.xlsx',"Step 04: Verify that if user ask for too many decimals and not enough whole numbers you could see ***************************")
        
        #utillobj.create_data_set('ITableData0','I0r','10153568_c.xlsx')
        decimalsval = ['208420 ********************************', 'Total Sum 208420 Total Sum 208,422.222100000070000000000000000000']
        
        loc(self,21,23,decimalsval, "Step 04: Verify that Total Sum for MYFIELD = 0.620000000000000000000000000000 ")
         
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        