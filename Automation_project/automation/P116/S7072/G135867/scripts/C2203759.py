'''
Created on Oct 7, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203759
TestCase Name = Verify selected column is hidden
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.support.color import Color

class C2203759_TestClass(BaseTestCase):

    def test_C2203759(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached fex.
        """
        utillobj.active_run_fex_api_login("147775.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Verify the Report summary')
        column_list=['COUNTRY','CAR','MODEL','RETAIL_COST','DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2203759_Ds01.xlsx',"Step 01.3: Verify entire Data set in Page 1") 

        """
        Step 02: Click on country dropdown and select Pivot->Country(Group by)->Car(Across)
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','COUNTRY','CAR')
        
        """
        Step 03: Verify the same AHTML report color background is applied to the pivot report.
        """
        css="td.arPivotColumnHeadingContainer table.arPivotColumnHeading"
        color=Color.from_string(self.driver.find_element_by_css_selector(css).value_of_css_property('background-color')).rgba
        expected_color=utillobj.color_picker('red', 'rgba')
        utillobj.asequal(color,expected_color,"Step 03: Verify pivot report background color is red")
        utillobj.verify_pivot_data_set('piv1', 'C2203759_Ds02.xlsx','Step 03.1: Verify pivot report')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()