'''
Created on Nov 03, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203748
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
from selenium.webdriver.support.color import Color
import unittest,time,re

class C2203748_TestClass(BaseTestCase):

    def test_C2203748(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        #below code only for 8105 - applicable to 8105 
    
#         """Step 04: Execute 130277-Eniad, that uses the older ENIADefault_combine stylesheet.
#         Click on Dealer_Cost and select Calculate->% of total """
#             
#         
#         utillobj.active_run_fex_api_login("130277-Eniad.fex", "S7072", 'mrid', 'mrpass')
#         time.sleep(10)
#         miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 04.1: Verify Page Summary 10of10records")
#         
#         utillobj.verify_data_set('ITableData0', 'I0r', '130277.xlsx','Step 04.2: Verify data set of 130277-Eniad')
#         
#         miscelanousobj.select_menu_items('ITableData0', 2, 'Calculate','% of Total')
#         time.sleep(7)
#         col= self.driver.find_element_by_css_selector("td.IBIS0_1").value_of_css_property('color')
#         
#         rgb = Color.from_string(col).rgba
#        
#         utillobj.asequal('rgba(0, 128, 0, 1)',rgb,'Step 04: Verify Color green added in %of total ')
#         
#         utillobj.verify_data_set('ITableData0', 'I0r', '130277-Eniad_Ds01.xlsx', "Step 04.3: Verify data set 130277-Eniad % of Total")
#         
#         #rgb(0, 128, 0)
#         
#         utillobj.infoassist_api_logout()
        
       
        
        """Step 05: Execute 130277-Enwarm, that uses the current Enwarm stylesheet.
        Click on Dealer_Cost and select Calculate->% of total """
         
        utillobj.active_run_fex_api_login("130277-Enwarm.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 05.1: Verify Page Summary 10of10records")
         
        utillobj.verify_data_set('ITableData0', 'I0r', '130277.xlsx','Step 05.2: Verify data set of 130277-Enwarm')
         
        miscelanousobj.select_menu_items('ITableData0', 2, 'Calculate','% of Total')
        time.sleep(7)
         
        col= self.driver.find_element_by_css_selector("td.IBIS0_1").value_of_css_property('color')
         
        rgb = Color.from_string(col).rgba
         
        utillobj.asequal('rgba(192, 192, 192, 1)',rgb,'Step 05: Verify Color grey added in %of total ')
         
        #rgb(192, 192, 192)
         
        utillobj.verify_data_set('ITableData0', 'I0r', '130277-Enwarm_Ds01.xlsx',  "Step 05.3: Verify data set 130277-Enwarm % of Total")
         
         
        utillobj.infoassist_api_logout()
        
        
if __name__ == '__main__':
    unittest.main()