'''
Created on Nov 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203734

verify filtered ahtml report could be able to expandable with out any error

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time

class C2203734_TestClass(BaseTestCase):

    def test_C2203734(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        """
        Step 01: Execute the 96254.fex

        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("96254.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the act-886-report.fex and Verify the Report Heading')
        column_list=['COUNTRY','SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the act-886-report.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '96254.xlsx', 'Step 01.3: Execute the 97564.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '96254.xlsx')

        """
        Step 02:Select country drop down filter--> EQUALS-->FRANCE
        """
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Filter","Equals")
        
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Equals',value1='FRANCE')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        miscelanousobj.move_active_popup('1', 800, 150)
        time.sleep(4)
        miscelanousobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 02.1:Verify the Report Heading')
            
        """Step 03: Now click on the + sign next to france"""
        
        time.sleep(3)
        
        driver.find_element_by_css_selector("[id^='I0r0'][id$='C0'] span").click()
        time.sleep(5)
        
        #verify france value get expanded without any error
        
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203734_Ds01.xlsx', 'Step 03:verify report get displayed with france record in first page')
        
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2203734_Ds01.xlsx')
        
        
        
        
        
        
        

       
            
        
if __name__ == "__main__":
    unittest.main()