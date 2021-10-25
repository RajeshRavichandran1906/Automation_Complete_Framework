'''
Created on April 13, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227197
Description = AHTML Total Calculation DEFINE w decimal values incorrect (ACT-188)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227197_TestClass(BaseTestCase):

    def test_C2227197(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        
        """Step 1: Create a new report fex in Text Editor, and copy into it the attachement, act-181.fex.
        """
        utillobj.active_run_fex_api_login("act-188.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(2)
        utillobj._validate_page((By.ID,'ITableData0'))
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        
        
        """ Step 2: Run the report.
                    In the MYFIELD column, each value ends in .000056. At the bottom, the total for MYFIELD ends in .001008.
        """
        time.sleep(7)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Verified the Page Summary')
        column_list=['CAR', 'COUNTRY', 'SALES', 'MYFIELD']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verified Column Heading')
#         utillobj.create_data_set('ITableData0','I0r','C2227197_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2227197_Ds01.xlsx','Step 01.3: Data set verified')
        
        
        """ Step 3: Close the report window.            """
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()