'''
Created on Nov 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203740

Noticed that heading font size dispalys bigger.

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time

class C2203754_TestClass(BaseTestCase):

    def test_C2203754(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
            
        """
        Step 01: Run the attached repro - 139177.fex 

        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("139177.fex", "S7072", 'mrid', 'mrpass')
        
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 139177.fex and Verify the Report Heading')
        
        column_list=['COUNTRY','CAR', 'MODEL', 'SEATS']
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 139177.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '139177.xlsx', 'Step 01.3: Execute the 139177.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '139177.xlsx')

        """
        Step 02:Select Pivot(Cross Tab) tool under country in drop down menu and select car under GroupBY(X) and Model from Across.
        """
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Pivot (Cross Tab)","CAR", "MODEL")
        
        time.sleep(5)
 
        
        """Step 03: Report heading font size for pivot/rollup table displays its normal size."""
        
        time.sleep(2)
        font = driver.find_element_by_css_selector("#piv1 div").value_of_css_property('font-size').lower()
        
        utillobj.asin('11px', font, "Step 03: Report heading font size for pivot/rollup table displays its normal size.")
        
        
        
        
                
            
        
if __name__ == "__main__":
    unittest.main()