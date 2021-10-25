'''
Created on Jul 17, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204888
TestCase Name = Verify Scatter displays x axis values as expected
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, ia_resultarea, active_chart_rollup
from common.lib import utillity

class C2204888_TestClass(BaseTestCase):

    def test_C2204888(self):
        
        driver = self.driver
         
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        activeobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        
        """
        1. Execute attached fex "Chart_AHTML.fex" in IA.
        """
        utillobj.active_run_fex_api_login("Chart_AHTML.fex", "S7074", 'mrid', 'mrpass')
        
        parent_css="#MAINTABLE_wbody0 g[class^='riser'] rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 65)
        
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 1(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 1(ii) Verify Y Axis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.a: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 01.b: Verify number of risers', custom_css ="g[class^='riser'] rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "cerulean_blue", "Step 01.c: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['Unit Sales, Coffee/Latte: 878,063']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 01.d: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales by Category, Product', 'Step 01.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
        2. Click Scatter chart icon from Active tool bar.
        """
        activeobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        parent_css="#MAINTABLE_wbody0 path[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 45)
        
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.1: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 02.2: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        expected_tooltip_list=['Unit Sales', 'X: Coffee/Latte', 'Y: 878K']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mmarker!', expected_tooltip_list, 'Step 02.3: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales by Category, Product', 'Step 02.4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 02.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,'C2204888_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()