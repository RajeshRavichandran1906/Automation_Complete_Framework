'''
Created on Sep 6, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053783
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_chart_rollup
from common.lib import utillity
import unittest

class C2053783_TestClass(BaseTestCase):

    def test_C2053783(self):
        

        """
            Step 01: Execute the AR-RP-001A.fex
        """
        Test_Case_ID ="C2053783"
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        utillobj.active_run_fex_api_login("AR-RP-001A.fex", "S7074", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("table[id='ITableData0'] .arGridColumnHeading table>tbody", "Category", 35)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Execute the AR-RP-001A.fex")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report AR-RP-001A.fex')
        
        """
        Step 02: Select State > Chart > Line > Category
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Chart','Line','Category')
        utillobj.synchronize_with_number_of_element("#wall1 #wtop1", 1, 25)
        miscelanousobj.verify_popup_appears('wall1', 'State by Category', 'Step 02.1: Verify that State By Category pop up window for the Line chart is displayed')
        rollupobj.verify_arChartMenu('wall1', 'Step 02.2: Verify that chart toolbar is present with all the options')
        miscelanousobj.verify_active_chart_tooltip('wall1', 'marker!s0!g0!mmarker', ['State: 30','X: Coffee'],  'Step 02.3: Verify chart tooltip')
        utillobj.verify_chart_color('wall1', 'marker!s0!g0!mmarker','white',"Step 02.4: Verify Chart piebevel Color ")
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"_pic01", image_type='actual_images')
        
if __name__ == '__main__':
    unittest.main()
