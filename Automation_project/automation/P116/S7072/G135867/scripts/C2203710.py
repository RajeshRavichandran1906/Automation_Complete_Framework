'''
Created on Oct 21, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203710
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity
import unittest,time

class C2203710_TestClass(BaseTestCase):

    def test_C2203710(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj=visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Capture the actual path to stdr1003.fex from Properties and replace the value in drilldown.fex.
        Run drillDown.fex in IA
        """
        utillobj.active_run_fex_api_login("drilldown.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY','CAR','MODEL']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203710_Ds01.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Click any row in the Country column.
        """
        self.driver.find_element_by_css_selector('[id="I0r0.0C0"] div a').click()
        time.sleep(3)
        utillobj.asin('yahoo.com', driver.current_url, 'Step 02: Verify that the link takes you to Yahoo.com')
        
        """
        Step 03: Close the Yahoo window. Click the first Alfa Romeo value in the Car column.
        """
        self.driver.execute_script('window.history.go(-1)')        
        time.sleep(8)
        self.driver.find_element_by_css_selector('[id="I0r6.0C1"] div a').click()
        time.sleep(2)
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='ITALY', with_regular_exprestion=True)
        miscelanousobj.verify_page_summary(0, '3of3records,Page1of1', "Step 02.1: Verify Page Summary for Alfa Romeo only")
        column_list=['COUNTRY', 'CAR', 'BODYTYPE', 'MODEL', 'RETAIL_COST', 'DEALER_COST', 'SEATS', 'LENGTH']
        
        
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02.2: Verify all columns listed on the report Alfa Romeo only')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203710_Ds02.xlsx','Step 02.3: Verify data set for Alfa Romeo only')
        
        
        """
        Step 04: Close the Report window. Click any row in the Model column.
        """
        self.driver.execute_script('window.history.go(-1)')
        time.sleep(8)
        self.driver.find_element_by_css_selector('[id="I0r0.0C2"] div a').click()
        time.sleep(2)
        utillobj.asin('cnn.com', driver.current_url, 'Step 04: Verify that the link takes you to CNN.com')
        self.driver.execute_script('window.history.go(-1)')
        
if __name__ == "__main__":
    unittest.main()