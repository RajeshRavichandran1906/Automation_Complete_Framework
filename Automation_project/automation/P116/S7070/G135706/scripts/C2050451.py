
'''
Created on Aug 18, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050451
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


class C2050451_TestClass(BaseTestCase):

    def test_C2050451(self):

        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2050451'
        
        """Step 01: Run the attached 150768.fex"""
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('150768.fex','S7070','mrid','mrpass')      
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18 of 18')
        column=['COUNTRY','CAR','MODEL','SEATS']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 150768")
        utillobj.verify_data_set('ITableData0','I0r','150768.xlsx',"Step 01.3: Verify 150768 dataset")
                
        """
        Step 02: From SEATS Column drop-down menu, select option Filter->Equal
        """ 
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', '3', 'Filter', 'Equals')
       
        """ 
        Step 03: From Filter Selection click arrow in value edit box and from drop-down menu select value 2
        """
        time.sleep(5)
        filterobj.create_filter(1, 'Equals', value1='2')
        
        """
        Step 04: Click Filter Button
        """
        filterobj.filter_button_click('Filter')
        time.sleep(3)        
        filterobj.verify_filter_selection_dialog(True,'Step 04: Verify filter row.',['SEATS', 'Equals', '2'])
        active_misobj.verify_page_summary('0','5of18records,Page1of1', 'Step 04.1: Verify Page summary 5 of 18')   
        utillobj.verify_data_set('ITableData0','I0r','C2050451_Ds01.xlsx',"Step 04.2: Verify filtered dataset")
        
        """
        Step 05: Click Highlight Button
        """
        time.sleep(5)
        filterobj.filter_button_click('Highlight')
        time.sleep(2)
        utillobj.verify_data_set_old('ITableData0','bgcolor','C2050451_Ds02.xlsx',"Step 05.1: Verify highlighted page1 dataset",color='navy')
        
            
        

if __name__ == '__main__':
    unittest.main()

