
'''
Created on Aug 11, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050549
Test CaseName = AHTML/Select Filter Values Check Sign is not shown correctly(Project 123584)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,wf_mainpage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050549_TestClass(BaseTestCase):

    def test_C2050549(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050549'
        
        """
        Step 01: Execute the attached repro - 123584.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj.active_run_fex_api_login('123584.fex','S7068','mrid','mrpass')
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18 records')
        column=['COUNTRY','CAR','MODEL','SEATS']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see 2 columns")
        utillobj.verify_data_set('ITableData0','I0r','123584.xlsx',"Step 01.3: Verify entire Data set of 123584.fex ran from text editor")
        
        """-
        Step 02: Click the drop down arrow in the heading of column Model , 
        select Filter, then select Equals option, from the submenu.
        """ 
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', '2', 'Filter', 'Equals')
         
        """
        Step 03: Select any model , from submenu.
        Step 04: Verify check sign is displayed correctly.
        """
        time.sleep(3)
        filterobj.create_filter(1, 'Equals',value1='100 LS 2 DOOR AUTO')
        filterobj.verify_filter_selection_dialog(True,'Step 04.1: Verify filter menu MODEL appears',['MODEL','Equals','100 LS 2 DOOR AUTO'])
        time.sleep(5)
        filterobj.verify_value_selection(1, ['100 LS 2 DOOR AUTO'], "Step 04.2: Verify value is selected")
               
        """
        Step 05: Deselect the value from submenu which is selected.
        """
        filterobj.create_filter(1, 'Equals',value1='100 LS 2 DOOR AUTO') 
        """
        Step 06: Verify when de-selecting check sign value should not be appeared on the value box.
        """
        filterobj.verify_filter_selection_dialog(False,'Step 06.1: Verify filter menu Unit Sales appears',['MODEL','Equals','100 LS 2 DOOR AUTO'])
        filterobj.verify_value_selection(1, [], "Step 06.2: Verify no value is selected")
         
                        
if __name__ == '__main__':
    unittest.main()
    
