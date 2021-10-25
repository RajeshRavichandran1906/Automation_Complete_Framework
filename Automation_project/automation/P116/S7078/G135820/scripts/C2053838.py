'''
Created on Aug 31, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053838
'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_tools
from common.lib import utillity


class C2053838_TestClass(BaseTestCase):

    def test_C2053838(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053838'
        """
        Step 01: Execute the AR_RP_CALCULATE.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR_RP_CALCULATE.fex','S7078','mrid','mrpass')      
        misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000')
        misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)', 'ALPHA Store Code','Date YYMD')     
                
        pivobj.veryfy_pivot_table_title('piv1', 'OrderNumberINTEGERbyDateYYMD,ALPHAStoreCode', 'Step 01.3: Verify pivot Title')
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds01.xlsx','Step 01.4: Verify Pivot dataset')
        pivobj.verify_pivot_menu('wall1', 'Step 01.5: Verify pivot toolbar menus')          
               
        """
        Step 02:  From the options bar, click the first icon and select Group By(X) and select D10.2 Unit Price from the field list.
        Expect to see a second By column appear to the right of ALPHA Store Code. 
        The summed values for each Store Code are now broken out to the D10.2 Unit Price level.
        """
        pivobj.create_new_item('wall1', 0, 'Group By (X)->D10.2 Unit Price')
        utillobj.verify_pivot_data_set('piv1', 'C2053838_Ds01.xlsx','Step 02.1: Verify Pivot dataset Store Code are now broken out to the D10.2 Unit Price level')
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
