'''
Created on Nov 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203737

Verify underline get displayed in entire fields in report

'''

import unittest,re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time

class C2203737_TestClass(BaseTestCase):

    def test_C2203737(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        """
        Step 01: Execute 107543.fex from repro
        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("107543.fex", "S7072", 'mrid', 'mrpass')
        
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.1: Execute the 107543.fex and Verify the Report Heading')
        
        column_list=['COUNTRY','DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 107543.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '107543.xlsx', 'Step 01.3: Execute the 107543.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '107543.xlsx')

        #I0r0.0C0
        
        def verify_cell_underline(rownum, columnnum, msg):
            css_val = "[id^='I0r"+rownum+"'][id$='C"+columnnum+"']"
            css= driver.find_element_by_css_selector(css_val).value_of_css_property("text-decoration").lower()
            print(css)
            css_value=re.match('\S+',css)
            utillobj.asequal('underline', css_value.group(0), msg)
        
        verify_cell_underline("0","0", "Step 01: Verify underline ")
        verify_cell_underline("3","0", "Step 01: Verify underline ")
        verify_cell_underline("0","1", "Step 01: Verify underline ")
        verify_cell_underline("3","1", "Step 01: Verify underline ")
        
        if len(driver.find_elements_by_css_selector("[id^='TCOL_0_C_'] u")) ==2:
            print("Step 01: Title also underlined - PASSED")
        else:
            print("Step 01: Title aslo underlined - FAILED")
        
        
        
        
        
        
            
            
        
if __name__ == "__main__":
    unittest.main()