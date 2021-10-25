
'''
Created on July 21, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/20550472
'''
__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from common.lib import utillity


class C2050489_TestClass(BaseTestCase):

    def test_C2050489(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050489'
        
        """Step 01: Execute the AR-RP-001.fex"""
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Verify output summary'
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', step01)
        """Step 02: Select Unit Sales > Calculate > Min""" 
        
        miscelanousobj.select_menu_items('ITableData0', '4', 'Calculate', 'Min')
        step02 = 'Step 02 : Verify Total Min is applied for Unit Sales column and same is displayed under the column heading Verify the value: Total Min 12,386'
        
        miscelanousobj.verify_calculated_value('2', '5', "Total Min 12386", True, step02) 

        time.sleep(4)#Static time given as needed
        #filterselectionobj.verify_filter_condition_menu_list(step02)
        
        """Step 03:Select Unit Sales > Filter > Greater than"""
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than")
                
        #Verify Filter selection pop up is opened.
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03: Select Unit Sales > Filter > Greater than',['Unit Sales', 'Greater than'])
         
        """Step 04 :Click Value dropdown menu and select "29746" Click Filter option"""
        
        filterselectionobj.create_filter(1, 'Greater than','large', value1='29746')

        
        _step04 = 'Step 04 :Verify that Unit Sales column heading shows : Filtered Min 30157(243.48%) Total Min 12,386 Pagination shows: SUB/TOT See attached screenshot.'
        
        time.sleep(4)#Static time given as needed
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)#static time given as needed
        miscelanousobj.verify_page_summary('0','SUB/TOT46of107records,Page1of1', _step04+"page summary")
        miscelanousobj.verify_summation(_step04+"Verifying summation present or not")
        #Verify that Unit Sales column heading shows : Filtered Min 30,157(243.48%) Total Min 12,386 Pagination shows: SUB/TOT See attached screenshot
        
        miscelanousobj.verify_calculated_value('2', '5', "Filtered Min 30157(243.48%)\nTotal Min 12386", True, _step04+"Filtered Min values") 
        utillobj.verify_data_set('ITableData0','I0r','C2050489_Ds01.xlsx',"Step04: Verify data set")
        



if __name__ == '__main__':
    unittest.main()

