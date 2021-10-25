'''
Created on Sep 8, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055498
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

import unittest
import time,re

class C2055498_TestClass(BaseTestCase):

    def test_C2055498(self):
        
        """
            Step 01: Execute 96554.fex form repro
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("96554.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the 96554.fex")
        column_list=['CAR','COUNTRY','DEALER_COST','RETAIL_COST','SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report 96554.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', '96554.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Select sort ascending step from sales column
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Sort Ascending')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2055498_Ds01.xlsx','Step 02: verify sales get sorted in ascending order')
        
        """
        Step 03: Select visualize option from sales column
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Visualize')
        time.sleep(3)
        
        def verify_visualization_black(table_id, tr_id, colnum, color_code, msg):
            expected_color_code=utillity.UtillityMethods.color_picker(self,color_code, 'rgba')
            occurence = 0
            total_rows=self.driver.find_elements_by_css_selector("[id='{0}'] tr[id ^='{1}']".format(table_id, tr_id))
            for i in range(0, len(total_rows)):
                actual_color_code=self.driver.find_element_by_css_selector("[id=" + table_id + "] tr[id ^= '" + tr_id + str(i) +"'] > td:nth-child(" + str(colnum+2) + ") > table td:nth-child(2)").value_of_css_property('background-color')
                reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_color_code)
                bg_color=reobj.group(1)
                if bg_color in expected_color_code:
                    occurence = occurence + 1 
                else:
                    break
            utillity.UtillityMethods.asequal(self, len(total_rows), occurence, msg)
        
        verify_visualization_black('ITableData0', 'I0r', 4, 'black', 'Step 03.1: Verify sales column visualize bar')
        
        def verify_visualization_green(table_id, tr_id, colnum, color_code, msg):
            expected_color_code=utillity.UtillityMethods.color_picker(self,color_code, 'rgba')
            occurence = 5
            total_rows=self.driver.find_elements_by_css_selector("[id='{0}'] tr[id ^='{1}']".format(table_id, tr_id))
            for i in range(5, len(total_rows)):
                actual_color_code=self.driver.find_element_by_css_selector("[id=" + table_id + "] tr[id ^= '" + tr_id + str(i) +"'] > td:nth-child(" + str(colnum+2) + ") > table table td").value_of_css_property('background-color')
                reobj=re.match('.*\((\d+,\s\d+,\s\d+).*', actual_color_code)
                bg_color=reobj.group(1)
                if bg_color in expected_color_code:
                    occurence = occurence + 1 
                else:
                    break
            utillity.UtillityMethods.asequal(self, len(total_rows), occurence, msg)
            
        verify_visualization_green('ITableData0', 'I0r', 4, 'green', 'Step 03.2: Verify sales column visualize bar')
            
        

if __name__ == '__main__':
    unittest.main() 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        