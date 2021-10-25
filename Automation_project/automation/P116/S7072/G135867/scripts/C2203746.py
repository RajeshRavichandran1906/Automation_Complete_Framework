'''
Created on Nov 03, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203746
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
import unittest,time,re

class C2203746_TestClass(BaseTestCase):

    def test_C2203746(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        """
        Step 01: Run attached repro - act-378.fex
        """
        utillobj.active_run_fex_api_login("act-378.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01.1: Verify Page Summary 5of5records")
        column_list=['COUNTRY','SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify 2columns listed for the report act-378.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-378.xlsx','Step 01.2: Verify data set of act-378')
        
        eles=self.driver.find_elements_by_css_selector("#THEAD_0_1_0_0 span")
        line=eles[0].get_attribute("style")        
        line1=eles[1].get_attribute("style")
        
        utillobj.asin("font-size:10pt;",re.sub('\s', '', line),"Step01.3: Verify Font Size is 10")
        utillobj.asin("font-size:11pt;",re.sub('\s', '', line1),"Step01.4: Verify Font Size is 11")
        
if __name__ == '__main__':
    unittest.main()