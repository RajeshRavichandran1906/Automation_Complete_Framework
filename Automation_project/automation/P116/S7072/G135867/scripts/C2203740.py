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

class C2203740_TestClass(BaseTestCase):

    def test_C2203740(self):
        
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
        
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 122283.fex and Verify the Report Heading')
        
        column_list=['COUNTRY','CAR', 'MODEL', 'SEATS']
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 122283.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '122283.xlsx', 'Step 01.3: Execute the 122283.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '122283.xlsx')

        """
        Step 02:Click on SEAT column drop down menu and select FILTER -> Equals
        """
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
        
        time.sleep(4)
        miscelanousobj.move_active_popup('1', 450, 450)
        
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 02.1:Verify the Report Heading')
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02.2: Verify filter window opened cascade mode')
        """Step 03: click on SEAT column drop down menu and select Windows -> Tabs """
        
        time.sleep(3)
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Window","Tabs")
        
        
        time.sleep(4)
        tabs=['Report', 'Filter']
        verify_tabs(tabs, "Step 03")
    
        """Step 04: Once again click on SEAT column drop down menu and select Windows -> Cascade"""
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Window","Cascade")
        
        time.sleep(4)
        
        #Verify Filter selection pop up is opened.
        
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04: Verify filter window opened cascade mode', ['SEATS', 'Equals'])
        time.sleep(5)
        
        """Step 05: Again click on SEAT column drop down menu and select Windows -> Tabs"""
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Window","Tabs")
        time.sleep(5)
        tabs=['Report', 'Filter']
        verify_tabs(tabs, "Step 05")
        
        
        
            
        
if __name__ == "__main__":
    unittest.main()