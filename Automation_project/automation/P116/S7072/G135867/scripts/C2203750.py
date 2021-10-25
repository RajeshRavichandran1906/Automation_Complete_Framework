'''
Created on Nov 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203750

Verify subfoot is displayed on AHTML report with the following conditions:

    The sort field value is D format.
    The value of the sort field is above 999.


'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time

class C2203750_TestClass(BaseTestCase):

    def test_C2203750(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
            
        """
        Step 01: Execute the attached repro - 108514.fex

        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("108514.fex", "S7072", 'mrid', 'mrpass')
        
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '1of1records,Page1of1', 'Step 01.1: Execute the 108514.fex and Verify the Report Heading')
        
        column_list=['FIELD1', 'FIELD1']
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 108514.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '108514.xlsx', 'Step 01.3: Execute the 108514.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '108514.xlsx')
        
        """
        Step 02: Verify Subfoot is displayed for the report.
        
        """
        subfoot = driver.find_element_by_css_selector("[id^='THEAD_'] tt").text
        utillobj.asin("this subfoot doesn't print in AHTML", subfoot, "Step 02:Verify Subfoot is displayed for the report.")
        
        
       
        
        
        
            
        
if __name__ == "__main__":
    unittest.main()