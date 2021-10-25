
'''
Created on Aug 18, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050449
'''

import unittest
import time,re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    wf_mainpage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.lib import utillity


class C2050449_TestClass(BaseTestCase):

    def test_C2050449(self):

        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2050449'
        
        """Step 01:  Run a Simple AHTML report by executing the attached 121513.fex. """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('121513.fex','S7070','mrid','mrpass')      
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18 of 18')
        column=['COUNTRY','CAR','MODEL','SEATS']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 138557")
        utillobj.verify_data_set('ITableData0','I0r','121513.xlsx',"Step 01.3: Verify 121513 dataset")
                
        """
        Step 02: Select any Filter option under any of the column eg:Model->Filter->Equals.
        """ 
        active_misobj.select_menu_items('ITableData0', '2', 'Filter', 'Equals')
       
        """ 
        Step 03: Under Filter Selection select 2002 2 DOOR AUTO under model->Equals and click filter
        """
        filterobj.create_filter(1, 'Equals', value1='2002 2 DOOR AUTO')
        filterobj.filter_button_click('Filter')
        time.sleep(2)
        
        """
        Step 04: Expect to see only the Filter dialogue box
        """
        filterobj.verify_filter_selection_dialog(True,'Step 04: Verify filter row.',['MODEL', 'Equals', '2002 2 DOOR AUTO'])
        
        """
        Step 05: Drag the Filter dialogue box to the middle of the screen.
        """
        active_misobj.move_active_popup("1", "600", "200")
        time.sleep(2)
        """Expect to see both the Filtered Repot above and the Filter dialogue box below."""
        utillobj.verify_data_set('ITableData0','I0r','C2050449_Ds01.xlsx',"Step 05.1: Verify Filtered dataset")
        filterobj.verify_filter_selection_dialog(True,'Step 05.2: Verify filter row.',['MODEL', 'Equals', '2002 2 DOOR AUTO'])
        
        

if __name__ == '__main__':
    unittest.main()

