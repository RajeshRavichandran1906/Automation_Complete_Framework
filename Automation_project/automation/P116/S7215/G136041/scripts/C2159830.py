'''
Created on Sep 20, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2159830
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2159830_TestClass(BaseTestCase):

    def test_C2159830(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01. Execute the attached repro - ACT-172-works.fex
        Expect to see the following Active Report, with a green cell on the ENGLAND/JAGUAR XJ12 AUTO line for 
        column - TESTCOL.
        Also expect to see the Red in the TESTCOL column for DATSUN and TOYOTA rows. 
        Here Red has been established for negative numbers, then the additional condition allows Green to override 
        Red but only for the value of -100.
        """
        utillobj.active_run_fex_api_login("ACT-172-works.fex", "S7215", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18')
        column_list=['CAR','MODEL','SALES','TESTCOL']
        active_misobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','ACT-172-works.xlsx',"Step 01.3: Verify ACT-172-works.fex dataset")
        
        active_misobj.verify_cell_property('ITableData0',1,3,'-100.00','Step 01.3:Verify background & text color',text_color='black',bg_color='green') 
        active_misobj.verify_cell_property('ITableData0',4,3,'-43,000.00','Step 01.4:Verify background & text color',text_color='black',bg_color='red') 
        active_misobj.verify_cell_property('ITableData0',5,3,'-35,030.00','Step 01.5:Verify background & text color',text_color='black',bg_color='red') 
        
        """
        Step 02: Execute the attached repro - ACT-172-fails.fex
        Expect to see the following Active Report, with Red cells for 
        column - TESTCOL, all values are negative.
        The order forces Red to override Green.
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("ACT-172-fails.fex", "S7215", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 02.1: Verify Page summary 18of18')
        column_list=['CAR','MODEL','SALES','TESTCOL']
        active_misobj.verify_column_heading('ITableData0', column_list, 'Step 02.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','ACT-172-fails.xlsx',"Step 02.3: Verify ACT-172-fails.fex dataset")
        
        active_misobj.verify_cell_property('ITableData0',1,3,'-100.00','Step 02.3:Verify background & text color',text_color='black',bg_color='red') 
        active_misobj.verify_cell_property('ITableData0',4,3,'-43,000.00','Step 02.4:Verify background & text color',text_color='black',bg_color='red') 
        active_misobj.verify_cell_property('ITableData0',5,3,'-35,030.00','Step 02.5:Verify background & text color',text_color='black',bg_color='red') 
        
            
if __name__ == '__main__':
    unittest.main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            