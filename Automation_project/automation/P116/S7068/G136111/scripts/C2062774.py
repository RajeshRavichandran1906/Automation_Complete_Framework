'''
Created on Aug 3, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2062774
Test case Name = AHTML: Dialogs display out of viewable area for wide reports (ACT-460, 170)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time,unittest
from selenium.webdriver import ActionChains

class C2062774_TestClass(BaseTestCase):

    def test_C2062774(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2062774'
        """
        Step 01: Create a new fex and copy the attachment act-460.fex into it.
        Step 02: Run the new fex.
        The result is a wide report.
        Step 03: Use the scroll bar to move to the extreme right of the report.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("act-460.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute act-460.fex verify Page Summary 18of18")
        column=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see column headings for aact-460.fex")
        utillobj.verify_data_set('ITableData0','I0r','act-460.xlsx',"Step 03: Verify act-460.fex dataset")
        
        """
        Step 04: Click on the pulldown for BHP and select Filter and Equals.
        While selecting the filter, all dialog boxes should appear in the visible right part of the report.
        """ 
        active_misobj.select_menu_items('ITableData0', 14, "Filter","Equals")
        """Expect to see the following Filter menu appear."""
        active_filter.verify_filter_selection_dialog(True,'Step 04: Verify filter menu BHP appears',['BHP', 'Equals'])
        
        """
        Step 05: In the right input box, select 0, and then select the Filter button.
        """
        active_filter.create_filter(1, 'Equals', value1='0')
        active_filter.filter_button_click('Filter')
        
        """ 
        Step 06: Move the filter selection dialog to the bottom part of the report so that all of the 
        filtered report is visible.
        Only data with BHP=0 should appear.
        Step 07: Scroll to the left of the report.
        The left part of the report appears. Currently the filter dialog stays on the right and disappears.
        It would also be acceptable for it to move to the left.    
        """
        active_misobj.verify_page_summary(0, '10of18records,Page1of1', "Step 06.1: Verify Page Summary 10of18")
        utillobj.verify_data_set('ITableData0','I0r','C2062774_Ds01.xlsx', "Step 06.2: Verify BHP=0 dataset")
        
        """
        Step 07: Close the report.
        """      
        
if __name__ == '__main__':
    unittest.main()