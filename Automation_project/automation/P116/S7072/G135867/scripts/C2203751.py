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

class C2203751_TestClass(BaseTestCase):

    def test_C2203751(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
            
        """
        Step 01: Run the attached repro - 120720.fex 

        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("120720.fex", "S7072", 'mrid', 'mrpass')
        
        time.sleep(8)
        
        
        
        """
        Step 02: Check that the report throws prompt for password
        
        """
        prompt_title = driver.find_element_by_css_selector("#wtitle1").text
        utillobj.asin("Report is Password Protected", prompt_title, "Step 02:Check that the report throws prompt for password")
        
        
        """Step 03: Enter the string 'test' in the Password box.Click Ok."""
        
        input_field = driver.find_element_by_css_selector("#PromptTable1 input[type='password']")
        input_field.send_keys("test")
        time.sleep(4)
        driver.find_element_by_css_selector("div.arPromptButton").click()
        
        """Step 04: Now report gets displayed successfully."""
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 04.1: Execute the 120720.fex and Verify the Report Heading')
        
        column_list=['SALES', 'CAR', 'COUNTRY', 'DEALER_COST', 'RETAIL_COST']
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04.2: Execute the 120720.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '120720.xlsx', 'Step 04.3: Execute the 120720.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '120720.xlsx')
        
        
            
        
if __name__ == "__main__":
    unittest.main()