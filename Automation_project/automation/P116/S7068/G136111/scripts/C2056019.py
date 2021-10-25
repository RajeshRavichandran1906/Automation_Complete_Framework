'''
Created on Aug 3, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2056019
Test case Name = AHTML: Basic Filtering with Cache=ON/OFF (ACT-496)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time,unittest
from selenium.webdriver import ActionChains

class C2056019_TestClass(BaseTestCase):

    def test_C2056019(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2056019'
        """
        Step 01: Execute the attached repro - act-496OFF.
        Expect to see the following report, Cache is OFF.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(25) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("act-496OFF.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute act-496OFF.fex verify Page Summary 18of18")
        column=['COUNTRY', 'CAR', 'SALES']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see column headings for act-496OFF")
        utillobj.verify_data_set('ITableData0','I0r','act-496OFF.xlsx',"Step 01.3: Verify act-496OFF.fex dataset")
        
        """
        Step 02: From the drop down icon for Sales, click Filter, then Equals.
        """ 
        active_misobj.select_menu_items('ITableData0', 2, "Filter","Equals")
        """Expect to see the following Filter menu appear."""
        active_filter.verify_filter_selection_dialog(True,'Step 02: Verify filter menu Sales appear',['SALES', 'Equals'])
        
        """
        Step 03: From the drop down for Sales, select value 12400.
        Click Filter.
        """
        active_filter.create_filter(1, 'Equals', value1='12400')
        active_filter.filter_button_click('Filter')
        """Expect to see one row with Sales = 12400."""
        utillobj.verify_data_set('ITableData0','I0r','C2056019_Ds01.xlsx', "Step 03: Verify Expect to see one row with Sales = 12400.")
        
        """
        Step 04: Execute the attached repro - act-496ON
        Expect to see the following report, Cache is ON.
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("act-496ON.fex", "S7068", 'mrid', 'mrpass')        
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', "Step 04.1: Execute act-611ON.fex verify Page Summary 18of18")
        column=['COUNTRY', 'CAR', 'SALES']
        active_misobj.verify_column_heading('ITableData0',column, "Step 04.2: Expect to see column headings for act-496OFF")
        utillobj.verify_data_set('ITableData0','I0r','act-496ON.xlsx',"Step 04.3: Verify act-496ON.fex dataset")
        
        """
        Step 05: From the drop down icon for Sales, click Filter, then Equals.
        """ 
        active_misobj.select_menu_items('ITableData0', 2, "Filter","Equals")
        """Expect to see the following Filter menu appear."""
        active_filter.verify_filter_selection_dialog(True,'Step 05: Verify filter menu Sales appear',['SALES', 'Equals'])
        
        """
        Step 06: From the drop down for Sales, select value 12400.
        Click Filter.
        """
        time.sleep(5)
        active_filter.create_filter(1, 'Equals', value1='12400')
        active_filter.filter_button_click('Filter')
        """Expect to see one row with Sales = 12400."""
        utillobj.verify_data_set('ITableData0','I0r','C2056019_Ds01.xlsx', "Step 06: Verify Expect to see one row with Sales = 12400.")
        
        
if __name__ == '__main__':
    unittest.main()