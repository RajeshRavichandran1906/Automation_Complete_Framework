'''
Created on Aug 3, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2071388
Test case Name = AHTML_CACHE:VAL:Values are not displayed fully from filter value dropdown (ACT-611)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time,unittest
from selenium.webdriver import ActionChains

class C2071388_TestClass(BaseTestCase):

    def test_C2071388(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2071388'
        """
        Step 01: Execute the act-611.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("act-611.fex", "S7068", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
        active_misobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01: Execute act-611.fex verify Page Summary 107of107")
        column=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.1: Expect to see column headings for act-611.fex")
        
        """
        Step 02: From the drop down control for Unit Sales, select Filter, then Not Equal.
        """ 
        active_misobj.select_menu_items('ITableData0', 4, "Filter","Not equal")
        utillobj.synchronize_with_number_of_element("#wall1", 1, 15, pause_time=1)
        """Expect to see the following Filter menu appear."""
        active_filter.verify_filter_selection_dialog(True,'Step 02: Verify filter menu Unit Sales appear',['Unit Sales', 'Not equal'])
        
        """
        Step 03: Click the drop down in the Filter menu.
        Expect to see the Filter menu values appear.
        Also expect to see the value of Unit Sales on the second row of the report as 22482
        """
        utillobj.verify_data_set('ITableData0','I0r','act-611_page1.xlsx', "Step 03: Verify act-611 page1 second row of the report has 22482")
        
        """
        Step 04: Select value 22482. 
        Click Filter.
        """
        
        active_filter.create_filter(1, 'Not equal', 'large', value1='22482')
        utillobj.synchronize_with_number_of_element("#wall1", 1, 15, pause_time=1)
        active_filter.filter_button_click('Filter')
        """Expect to see the second row of the report removed."""
        utillobj.verify_data_set('ITableData0','I0r','C2071388_Ds01.xlsx', "Step 04: Verify second row of the report removed.")
        
        """
        Step 05: In the drop down Filter menu, drag the scroll bar all the way down, to the end of the list.
        Expect to see the following Filter values, at the end of the list.
        """
        self.driver.find_element_by_css_selector("#ftp1_1_0 img").click()
        browser = utillobj.parseinitfile('browser')
        if browser=='IE':
            utillobj.verify_popup_data_set('wall2','FiltSel2','C2071388_Ds02_ie.xlsx', "Step 05: Verify the filter values using dataset comparision")
        else:
            utillobj.verify_popup_data_set('wall2','FiltSel2','C2071388_Ds02.xlsx', "Step 05: Verify the filter values using dataset comparision")
        
if __name__ == '__main__':
    unittest.main()