'''
Created on Aug 31, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053839
'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_tools
from common.lib import utillity


class C2053839_TestClass(BaseTestCase):

    def test_C2053839(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053839'
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
        misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','D10.2 Unit Price', 'ALPHA Store Code')     
        
        """"
        Execute the attached repro - AR_RP_CALCULATE.fex
        Select Order Number INTEGER, select PIVOT(Cross Tab), then for Group By(SUM), select D10.2 Unit Price and lastly, for ACROSS, select the ALPHA Store Code field.
        """
        pivobj.veryfy_pivot_table_title('piv1', 'OrderNumberINTEGERbyALPHAStoreCode,D10.2UnitPrice', 'Step 01.3: Verify pivot Title')
        utillobj.verify_pivot_data_set('piv1', 'C2053839_Ds01.xlsx','Step 01.4: Verify Pivot dataset')
               
        """
        Step 02:  In the box for D10.2 Unit Price, click the up arrow.
        Expect to see the D10.2 Unit Price sort column converted to a second Across sort under ALPHA Store Code. 
        Now each Store Code is broken out by Unit Price
        """
        pivobj.click_groupby_across_button('piv1', 2, 1, 1)
        utillobj.verify_pivot_data_set('piv1', 'C2053839_Ds02.xlsx','Step 02.1: Verify Pivot dataset Store Code is broken out by Unit Price')
        
        """
        Step 03: In the box for ALPHA Store Code, click the last icon indicated by 'X', to remove 
        ALPHA Store Code as an Across sort.
        Expect to see the report now sorting Across only by the D10.2 Unit Price values. Ther is no longer a Group By axis.
        """
        pivobj.click_groupby_across_button('piv1', 1, 1, 4)
        utillobj.verify_pivot_data_set('piv1', 'C2053839_Ds03.xlsx','Step 03.1: Verify Pivot dataset sorting Across only by the D10.2 Unit Price values')
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
