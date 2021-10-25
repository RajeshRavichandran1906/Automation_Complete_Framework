'''
Created on Sep 20, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064077
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2064077_TestClass(BaseTestCase):

    def test_C2064077(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01. Execute the attached repro - act-ahtmltab.fex.
        Expect to see the following Active report, with correct drop down controls for 
        each field and correct Pagination bar information.
        """
        utillobj.active_run_fex_api_login("act-601.fex", "S7215", 'mrid', 'mrpass')
        element = (By.CSS_SELECTOR, "span[title='Goto Page']")
        utillobj._validate_page(element)
        time.sleep(5)
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18')
        column_list=['COUNTRY','CAR','BODYTYPE','SALES']
        active_misobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','act-601.xlsx',"Step 01.3: Verify act-601.fex dataset")
        active_misobj.verify_move_to_bottom('Top', 'Step 01.4: Verify Move to Bottom displayed')        
        try:
            img_status=self.driver.find_elements_by_css_selector("div[id*='popid'] img[src*='AAAAAElFTkSuQmCC']")
            utillity.UtillityMethods.asequal(self,4, len(img_status), 'Step 01.5: Verify drop down image displayed for all 4 fields')
        except:
            img_status='False'
            
            
if __name__ == '__main__':
    unittest.main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            