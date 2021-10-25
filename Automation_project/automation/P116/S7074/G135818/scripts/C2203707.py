'''
Created on Oct 25, 2016


@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203707
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest
import time


class C2203707_TestClass(BaseTestCase):

    def test_C2203707(self):
        
        """
            Step 01: Run 'customer's repro file based on CAR.fex' on IE8 (below 8.2 release) and verify the output. 
            There should be no error message on the screen.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("customer_repro_file_based_on_CAR.fex", "S7074", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01.1: Verify page summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203707_Ds01.xlsx', 'Step 01.2: Verify dataset')
        column_list=['COUNTRY']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.3: Verify columns listed on the report')
        miscelanousobj.verify_page_summary(1, '10of10records,Page1of1', "Step 01.4: Verify page summary")
        utillobj.verify_data_set('ITableData1', 'I1r', 'C2203707_Ds02.xlsx', 'Step 01.5: Verify dataset')
        column_list=['CAR']
        miscelanousobj.verify_column_heading("ITableData1", column_list, 'Step 01.6: Verify columns listed on the report')
        
        """
        Step 02: Run 'repro22233006.fex' on IE8 (below 8.2 release) and make sure output is without any error.
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("repro22233006.fex", "S7074", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 02.1: Verify page summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203707_Ds03.xlsx', 'Step 02.2: Verify dataset')
        column_list=['COUNTRY']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02.3: Verify columns listed on the report')
        
        """
        Step 03: Create Pie chart by selecting Chart > Pie > Country
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Chart','Pie','COUNTRY')
        time.sleep(3)
        miscelanousobj.verify_popup_title('wall1', 'COUNTRY by COUNTRY', 'Step 03.1: Verify Chart popup appears')
        miscelanousobj.verify_active_chart_tooltip('wall1', 'riser!s1!g0!mwedge', ['FRANCE','COUNTRY: 1','20.0% of 5'], 'Step 03.2: Verify chart tooltip')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()