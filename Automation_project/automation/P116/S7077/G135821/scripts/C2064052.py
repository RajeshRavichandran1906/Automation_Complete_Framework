
'''
Created on Nov 2, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064052
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


class C2064052_TestClass(BaseTestCase):

    def test_C2064052(self):

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2064052'
        
        """
        Step 02:  In the WebFOCUS folder, create a new fex with Text Editor, copying the attachment 11273579.fex.
        Run the fex.
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj.active_run_fex_api_login("11273579.fex", "S7077", 'mrid', 'mrpass')
        time.sleep(10)
        utillobj.verify_data_set('ITableData0','I0r','11273579.xlsx',"Step 02.3: Verify entire Data set of 11273579.fex ran from text editor")
                  
        """
        Step 03: In the Active Report, click on any drop-down arrow, and select Export -> XML (Excel) -> All records.
        Step 04: Close the report in Excel, and close the blank IE window.
        """ 
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', '0', 'Export', 'XML (Excel)','All records')
        time.sleep(7)
        utillobj.save_window('C2064052_Actual_1')
        time.sleep(5)
        utillobj.create_excel('C2064052_Actual_1.xls','C2064052_Actual_1.xlsx')
        time.sleep(5)
        utillobj.verify_excel_sheet('C2064052_Base_1.xlsx', 'C2064052_Actual_1.xlsx', 'Sheet1', 'Step 03: Verify excel same as that of saved C2064052_Base_1.xls')
         
        
        """
        Step 05:In the Active Report again, click on any drop-down arrow, and select Export -> CSV (comma delim) -> All records.
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', '0', 'Export', 'CSV (comma delim)','All records')
        
        """ Window handling"""
        time.sleep(5)  
        print(driver.window_handles)

        for handle in driver.window_handles:
            driver.switch_to_window(handle)
            driver.get_window_position(handle)
            if self.driver.title=="":
                active_misobj.compare_active_csv(-1,'C2064052.csv',"Step05: Verify csv file")
                print(driver.title)
        driver.close()
        win=driver.window_handles
        driver.switch_to.window(win[0])



if __name__ == '__main__':
    unittest.main()

