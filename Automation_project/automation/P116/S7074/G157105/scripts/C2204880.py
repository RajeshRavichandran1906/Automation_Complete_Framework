'''
Created on JUL 11, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204880
TestCase Name = Verify user can add column on X-Axis
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity

class C2204880_TestClass(BaseTestCase):

    def test_C2204880(self):
        
        Test_Case_ID="C2204880"
        """
            TESTCASE VARIABLES
        """   
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
            Step 01:Execute attached fex "Chart_AHTML.fex" in IA.
        """
        utillobj.active_run_fex_api_login("Chart_AHTML.fex", "S7074", 'mrid', 'mrpass')
        parent_css="div [id='MAINTABLE_wmenu0']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 01.1 Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 01.2 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 01.3:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 01.4: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 01.5: Verify  bar color")
        expected_tooltip_list=['Unit Sales, Coffee/Latte: 878,063']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, "Step 01.6: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 01.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 01.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        """
            Step 02:Click Group By (X) option from the dropdown menu.
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Group By (X)',elem_index=0,custom_css='cpop',verify=True,expected_list=['Category', 'Product', '', 'Unit Sales'], msg="Step 02:")
        time.sleep(3)
        """
            Step 03:Click Unit Sales option: ( Group By (X) > Unit Sales)
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Group By (X)->Unit Sales',elem_index=0,custom_css='cpop')
        time.sleep(1)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.1 Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 03.2 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino/189217', 'Coffee/Espresso/308986', 'Coffee/Latte/878063', 'Food/Biscotti/421377', 'Food/Croissant/630054', 'Food/Scone/333414', 'Gifts/Coffee Grinder/186534', 'Gifts/Coffee Pot/190695', 'Gifts/Mug/360570', 'Gifts/Thermos/190081']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 03.3:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 03.4: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 03.5: Verify  bar color")
        expected_tooltip_list=['Unit Sales, Coffee/Latte/878063: 878,063']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, "Step 03.6: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product, Unit Sales', 'Step 03.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 03.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#orgdivouter0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step3', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()  