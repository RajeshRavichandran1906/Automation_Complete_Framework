'''
Created on Jul 28, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050530
Test case Name = Verify Pivot Table status for Proj. 156755 - Multiple numeric fields cause bad display in Pivot Table.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest,time
from selenium.webdriver import ActionChains

class C2050530_TestClass(BaseTestCase):

    def test_C2050530(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050530'
        """
        Step 01: Execute AR-RP-201 for the report that drives the Pivot Table.
        Verify Data set
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-201.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute AR-RP-201.fex verify Page Summary 1000of1000")
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-201_page1.xlsx',"Step 01: Verify AR-RP-201.fex dataset")
        
        """
        Step 02: Select the first D10.2 Unit Price column and then pick Pivot(Cross Tab). 
        Select the first ALPHA Store Code field as the Group By field and then Product as the Across column.        
        """  
        active_misobj.select_menu_items('ITableData0', 1, 'Pivot (Cross Tab)','Store Code','Product')
        
        """If you see the following report, project 156755 has corrected the bad Pivot Table display"""
        utillobj.verify_pivot_data_set('piv1','C2050530_Ds01.xlsx',"Step 02: Verify data set of Order Number INTEGER")

if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        