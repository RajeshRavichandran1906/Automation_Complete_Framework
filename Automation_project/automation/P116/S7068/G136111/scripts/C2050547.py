
'''
Created on Aug 9, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050547
Test CaseName = AHTML_Cache:Filter Between:the 2nd edit box not enable(Project 90148)
'''

import unittest
import subprocess,os
import time,re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,wf_mainpage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.lib import utillity


class C2050547_TestClass(BaseTestCase):

    def test_C2050547(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(1) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050547'
        
        """
        Step 01: Execute the attached repro - 90148.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj.active_run_fex_api_login('90148.fex','S7068','mrid','mrpass')
        active_misobj.verify_page_summary('0','4306of4306records,Page1of76', 'Step 01.1: Verify Page summary 4306of4306 records')
        column=['Date', 'Product', 'Region', 'Unit Sales', 'Budget Dollars', 'Budget Units']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Verify Column heading")
        utillobj.verify_data_set('ITableData0','I0r','90148_page1.xlsx',"Step 01.3: Verify entire Data set of 90148.fex ")
        """
        Step 02: Click on Budget Dollars column and select Filter
        """ 
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', '4', 'Filter', 'Between')
         
        """
        Step 03: From Filter select values From:700 To:900 and click on filter.
        """
        time.sleep(5)
        filterobj.create_filter(1, 'Between','large','wall1',1,value1='700',value2='900')
        filterobj.filter_button_click('Filter')
        """Verify values are filtered as expected with WEBVIEWER= ON"""
        active_misobj.verify_page_summary('0','23of4306records,Page1of1', 'Step 03.1: Verify Page summary 23of4306 records')
        filterobj.verify_filter_selection_dialog(True,'Step 03.2: Verify filter menu Budget Dollars appears',['Budget Dollars','Between','[','700','900'])
        utillobj.verify_data_set('ITableData0','I0r','C2050547_Ds01.xlsx',"Step 03.4: Verify data set after filter")
          
        
if __name__ == '__main__':
    unittest.main()
    
