'''
Created on Sep 16, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2060797
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.support.color import Color

class C2060797_TestClass(BaseTestCase):

    def test_C2060797(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        1. Execute the act-582.fex
        """
        utillobj.active_run_fex_api_login("act-582.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the act-582.fex')
        column_list=['CAR','DEALER_COST','RETAIL_COST','TOTAL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-582.xlsx',"Step 01.3: Verify data set act-582.fex")
        
        """Expect to see the following Active Report with only the Rowtotal column headings and data in Orange."""
        color=driver.find_element_by_css_selector("#TCOL_0_C_3 span").get_attribute('style')
        browser=utillobj.parseinitfile('browser')
        if browser=='Edge':
            utillobj.asequal("color:#FF7F00;",color,"Step 01.4: Verify Column Heading - TOTAL has orange color")
        else:
            utillobj.asequal("color: "+utillobj.color_picker('flush_orange')+";",color,"Step 01.4: Verify Column Heading - TOTAL has orange color")
        cuntobj = driver.find_elements_by_css_selector("#ITableData0 .arGridColumnHeading td[id='TCOL_0_C_3']")
        for i in range(len(cuntobj)):
            temp_obj=Color.from_string(cuntobj[i].value_of_css_property('color')).rgba
            if temp_obj == utillobj.color_picker('flush_orange', 'rgba'):
                stat = True
            else:
                stat = False
                break
        utillobj.asequal(stat, True, "Step 01.5: Verify table data column has orange color")
        time.sleep(3)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2060797_Ds01.xlsx',"Step 01.6: Verify Active Report with only the Rowtotal column headings and data in Orange - Known product failure.",'flush_orange')
        
            
if __name__ == '__main__':
    unittest.main()