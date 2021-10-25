'''
Created on Nov 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203740

Verify user can switch AHTML report from windows Cascade to Tab view for the second time

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time

class C2203743_TestClass(BaseTestCase):

    def test_C2203743(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        
        def verify_tabs(tabs_text,msg):
            otab_val=driver.find_elements_by_css_selector("#MAINTABLE_wmenu0 [id^='tab_']")
            actual1 = [x.text for x in otab_val]
            actual = [y.strip() for y in actual1]
            print(actual)
            utillobj.asequal(actual, tabs_text, msg + ": verifying Report and filter Tabs displayed on top of the Run Report")
            
            
            
        """
        Step 01: Execute the attached 122283.fex

        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("122283.fex", "S7072", 'mrid', 'mrpass')
        
        time.sleep(8)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 122283.fex and Verify the Report Heading')
        
        column_list=['COUNTRY','CAR', 'MODEL', 'SEATS']
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 122283.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '122283.xlsx', 'Step 01.3: Execute the 122283.fex and Verify the entire data')
        
    
        """
        Step 02:Select Filter option under any column.
        """
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
        
        time.sleep(4)
        miscelanousobj.move_active_popup('1', 450, 450)
        
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 02.1:Verify the Report Heading')
        
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.2: Verify filter window opened cascade mode')
        
        """Step 03: Select windows option and choose tabs."""
        
        time.sleep(3)
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Window","Tabs")
        
        time.sleep(4)
        
    
        """Step 04: Verify filter window is created in report without any overlap after applying tab option."""
        
        tabs=['Report', 'Filter']
        
        verify_tabs(tabs, "Step 04")
        
        
        
        
        
        
     
        
        
        
        
            
        
if __name__ == "__main__":
    unittest.main()