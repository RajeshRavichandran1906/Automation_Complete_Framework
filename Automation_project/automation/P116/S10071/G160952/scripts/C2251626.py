'''
Created on Jan 16, 2018

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10071&group_by=cases:section_id&group_id=160952&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2251626
TestCase Name = Verify compound report, co-ordinate filter is respected for fields with alias (141611)

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2251626_TestClass(BaseTestCase):

    def test_C2251626(self):
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
            Step 01 :Execute the attached repro - alias_names.fex
            Expect to see the following AHTML Document containing two reports both controlled by a Co-ordinated filter of Category.
            The default co-ordinated value is COFFEE.
        """
        utillobj.active_run_fex_api_login('alias_names.fex','S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class='arGrid']", 1, 65)
        
        miscelanousobj.verify_page_summary('0','3of10records,Page1of1', 'Step 01.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251626_Ds01.xlsx', 'Step 01.2:Verify the report is generated.')
        miscelanousobj.verify_page_summary('1','30of107records,Page1of1', 'Step 01.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251626_Ds01a.xlsx', 'Step 01.4:Verify the report is generated.')
        time.sleep(4)
        
        """
            Step 02 :Execute the attached repro - alias_names.fex
            Expect to see the following AHTML Document containing two reports both controlled by a Co-ordinated filter of Category.
            The default co-ordinated value is COFFEE.
        """
        
        dropdown_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar']")
        utillobj.click_on_screen(dropdown_css, 'middle')
        utillobj.click_on_screen(dropdown_css, 'middle', click_type=0)
        time.sleep(2)
        production_css = driver.find_element_by_css_selector("#IBILAYOUTDIV0[class*='arDashboardBar'] option[value='Food']")
        production_css.click()
        time.sleep(4)
        miscelanousobj.verify_page_summary('0','3of10records,Page1of1', 'Step 02.1: Verify the page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2251626_Ds02.xlsx', 'Step 02.2:Verify the report is generated.')
        miscelanousobj.verify_page_summary('1','33of107records,Page1of1', 'Step 02.3: Verify the page summary')
        utillobj.verify_data_set('ITableData1','I1r','C2251626_Ds02a.xlsx', 'Step 02.4:Verify the report is generated.')
        time.sleep(4)  
        
        
if __name__ == '__main__':
    unittest.main()