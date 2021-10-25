'''
Created on Sep 9, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055500
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest
import time

class C2055500_TestClass(BaseTestCase):

    def test_C2055500(self):
        
        """
            Step 01: Execute 105103.fex form repro
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        utillobj.active_run_fex_api_login("105103.fex", "S7215", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#ITableData0 tr:nth-child(2) td"
        result_obj.wait_for_property(parent_css, 1, string_value='1', with_regular_exprestion=True)
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4317of4317records,Page1of76', "Step 01.1: Execute the 105103.fex")
        column_list=['Sequence#']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report 105103.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', '105103.xlsx','Step 01.3:  verify NO Print values are not displayed other than #sequence')
        
        """
        Step 02: Click on Forward page #2 and verify NO Print values are not displayed other than #sequence.
        """
        miscelanousobj.navigate_page('next_page')
        parent_css="#ITableData0 tr:nth-child(2) td"
        result_obj.wait_for_property(parent_css, 1, string_value='58', with_regular_exprestion=True)
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4317of4317records,Page2of76', "Step 02: Execute the 105103.fex")
        column_list=['Sequence#']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02.1: Verify all columns listed on the report 105103.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2055500_Ds01.xlsx','Step 02.2:  verify NO Print values are not displayed other than #sequence')
        
        """
        Step 03: Click on Forward page #3 and verify NO Print values are not displayed other than #sequence.
        """
        miscelanousobj.navigate_page('next_page')
        parent_css="#ITableData0 tr:nth-child(2) td"
        result_obj.wait_for_property(parent_css, 1, string_value='115', with_regular_exprestion=True)
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4317of4317records,Page3of76', "Step 03: Execute the 105103.fex")
        column_list=['Sequence#']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 03.1: Verify all columns listed on the report 105103.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2055500_Ds02.xlsx','Step 03.2:  verify NO Print values are not displayed other than #sequence')
        
        """
        Step 04: Click on Forward page #4 and verify NO Print values are not displayed other than #sequence.
        """
        miscelanousobj.navigate_page('next_page')
        parent_css="#ITableData0 tr:nth-child(2) td"
        result_obj.wait_for_property(parent_css, 1, string_value='172', with_regular_exprestion=True)
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4317of4317records,Page4of76', "Step 04: Execute the 105103.fex")
        column_list=['Sequence#']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 04.1: Verify all columns listed on the report 105103.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2055500_Ds03.xlsx','Step 04.2:  verify NO Print values are not displayed other than #sequence')
        
        
if __name__ == '__main__':
    unittest.main() 