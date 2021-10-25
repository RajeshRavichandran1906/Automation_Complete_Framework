
'''
Created on Aug 10, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050548
Test CaseName = AHTML_Cache:HIGHLIGHT not working in Filter window(Project 90018)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity


class C2050548_TestClass(BaseTestCase):

    def test_C2050548(self):

        
        """
        Step 01: Execute AR_RP_001.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR_RP_001.fex','S7068','mrid','mrpass')
        element_css="table .arGridBar table table > tbody"
        utillobj.synchronize_with_number_of_element(element_css, 1, 50, 1)
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary 107of107 records')
        """
        Step 02: Click on UNIT SALES and select Filter
        """ 
        active_misobj.select_menu_items('ITableData0', '4', 'Filter', 'Greater than')
         
        """
        Step 03: From Filter click on Greater than and select value as 15313, then click on Highlight
        """
        utillobj.synchronize_with_number_of_element("#wall1", 1, 25, 1)
        filterobj.create_filter(1, 'Greater than','large','wall1',value1='15313')        
        filterobj.filter_button_click('Highlight')
        """
        Step 04: Verify values are displayed as expected using WEBVIEWER = ON
        """
        filterobj.verify_filter_selection_dialog(True,'Step 04.1: Verify filter menu Unit Sales appears',['Unit Sales','Greater than','15313'])
        time.sleep(1)
        utillobj.verify_data_set_old('ITableData0','rgb','C2050548_Ds01_page1.xlsx',"Step 04.2: Verify data set page1 after filter")
        time.sleep(1)
        active_misobj.move_active_popup("1", "600", "200")
        time.sleep(2)
        active_misobj.navigate_page('next_page')
        time.sleep(1)
        utillobj.verify_data_set_old('ITableData0','rgb','C2050548_Ds01_page2.xlsx',"Step 04.3: Verify data set page2 after filter")
          
        
if __name__ == '__main__':
    unittest.main()
    
