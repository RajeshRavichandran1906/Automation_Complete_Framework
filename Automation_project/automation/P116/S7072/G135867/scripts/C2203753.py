'''
Created on Oct 6, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203753
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity


class C2203753_TestClass(BaseTestCase):

    def test_C2203753(self):
        """
            Step 01: Run the attached 140624.fex in run-adhoc page
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("140624.fex", "S7072", 'mrid', 'mrpass')

        """
        STep 02: Type "test" in the textbox and click ok in the report.
        """
        self.driver.find_element_by_css_selector('[type="password"]').send_keys('test')
        self.driver.find_element_by_css_selector('[class="arPromptButton"]').click()
        time.sleep(3)
        
        """
        Step 03: Report has to displayed with all records and its fields
        """
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 03.1: Verify page summary")
        column_list=['RETAIL_COST','DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203753_Ds01.xlsx','Step 03.3: Verify dataset')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()