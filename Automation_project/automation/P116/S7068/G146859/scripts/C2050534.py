'''
Created on Aug 1, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050534
Test case Name = Verify Pivot Table status for problem - Filter/Equals options are not accessible.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,active_pivot_comment
from common.lib import utillity
import unittest,time
from selenium.webdriver import ActionChains

class C2050534_TestClass(BaseTestCase):

    def test_C2050534(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050534'
        """
        Step 01: Execute AR-RP-204 for the report to drive Pivot.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        active_pivot = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-204.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '2000of2000records,Page1of36', "Step 01: Execute AR-RP-204.fex verify Page Summary 2000of2000")
        """Expect to see a report containing 1000 rows. The first column, Order Number INTEGER will be used for this test."""
        column=['Order Number INTEGER', 'ALPHA ORDER', 'ALPHA ANV', 'ALPHA TEXT', 'ALPHA A80', 'ALPHA Edit', 'ALPHA Store Code', 'ALPHA Vendor Code', 'ALPHA Vendor Name', 'ALPHA Product Code', 'ALPHA Product Descr.']
        active_misobj.verify_column_heading('ITableData0',column, "Step 02: Expect to see two columns for Order Number INTEGER")
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-204_page1.xlsx', "Step 01: Verify AR-RP-204.fex data set")
        
        """
        Step 02: For the Order Number INTEGER field, select Filter, then select Equals.     
        """
        active_misobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        """Expect to see the Filter selection box appear for Order Number INTEGER."""
        active_filter.verify_filter_selection_dialog(True,'Step 02: Verify Order Number INTEGER Equals condition is on the top',['Order Number INTEGER','Equals'])
        
        """
        Step 03: From the drop-down list of values, navigate to the bottom by using the scroll bar
        Expect to see the final set of values, ending with 2000.        
        """
        self.driver.find_element_by_css_selector("#ftp1_1_0 img").click()
        utillobj.verify_popup_data_set('wall2','FiltSel2','C2050534_Ds01.xlsx', "Step 03: verify data set, final set of values, ending with 2000")
        
        """
        Step 04: Attempt to select the value of 2000.
        Expect that the scroll bar can access the end of the value list for Order Number INTEGER, i.e. value 2000.
        """
        active_filter.create_filter(1, 'Equals', 'large',value1='2000')
        active_filter.verify_filter_selection_dialog(True,'Step 04.1: Verify Order Number INTEGER Equals 2000 condition ',['Order Number INTEGER','Equals','2000'])
        
        
        """If the value of 2000 appears, click it to add it to the Filter/Equals selection panel.
        Click the Filter button."""
        active_filter.filter_button_click('Filter')
        
        """Expect to see a single row appear, the row containing Order Number INTEGER = 2000."""
        utillobj.verify_data_set('ITableData0','I0r','C2050534_Ds02.xlsx', "Step 04.2: Verify data set contains single row containing Order Number INTEGER = 2000. ")
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        