'''
Created on Jul 26, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235070
TestCase Name = Scatter Diagram/Bubble Chart failure.Proj. 159305
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,active_chart_rollup,ia_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2235070_TestClass(BaseTestCase):

    def test_C2235070(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        1. Execute the attached repro - ahtml_chart.fex.
        This will create an initial Bar Chart. Expect to see the following chart.
        Expect to see the following Active Bar Chart.
        """
        utillobj.active_run_fex_api_login("ahtml-chart.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(5)
        xaxis_value="Category : Product ID"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 01:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 1.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 1.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 01.3: Verify bar color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 02: Verify Legend Title')
        time.sleep(5)
        expected_tooltip_list=['Dollar Sales, Coffee/C141: 3,906,243']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s1!g0!mbar!", expected_tooltip_list, 'Step 01.4: verify the bar tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 01.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        2. From the Bar Chart, select the Advanced Chart tab
        then Select Charts,
        then select Scatter Diagram.
        Click OK.
        Expect to see the following Scatter Diagram.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 5)
        time.sleep(2)
        rollupobj.select_advance_chart('charttoolt1', 'scatter(xy_plot)')
        expected_xval_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 1.1: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 0, 'Step 02(i): Verify Number of Scatter XY plots', custom_css="path[class^='riser']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, 'Step 02(ii): Verify Number of Scatter XY plots', custom_css="circle[class^='riser']")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 02.1: Verify Legend Title')
        time.sleep(3)
        expected_tooltip_list=['Unit Sales', 'X: Coffee/C141', 'Y: 309K']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g0!mmarker!", expected_tooltip_list, 'Step 02.2: verify the scatter tooltip values')
        time.sleep(3)
        expected_tooltip_list=['Dollar Sales', 'X: Coffee/C141', 'Y: 3.9M']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s1!g0!mmarker!", expected_tooltip_list, 'Step 02.3: verify the scatter tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 02.4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 02.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        3. From the Scatter Diagram, select the Advanced Chart tab, then Charts, then select Bubble Chart. Click OK.
        Expect to see the following Bubble Chart.
        The Bubble Chart variation only uses the first Measure field - Unit Sales.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 5)
        time.sleep(2)
        rollupobj.select_advance_chart('charttoolt1', 'bubble')
        time.sleep(4)
        expected_xval_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.1: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 03: Verify Number of Scatter XY plots', custom_css="circle[class^='riser']")
        expected_legend_list=['Unit Sales','Series 1']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 03: Verify Legend Title')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mmarker!", "bar_blue", "Step 03: Verify bar color")
        time.sleep(3)
        expected_tooltip_list=['Unit Sales', 'X: Coffee/C142', 'Y: 878K', 'Z: 10.9M']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g1!mmarker!", expected_tooltip_list, 'Step 03: verify the bar tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 03: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 03: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        4. Switch back to a Scatter Diagram again, using the Advance Chart tab again.
        Expect to see the following Scatter Diagram.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 5)
        time.sleep(2)
        rollupobj.select_advance_chart('charttoolt1', 'scatter(xy_plot)')
        expected_xval_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4.1: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 0, 'Step 04.2: Verify Number of Scatter XY plots', custom_css="path[class^='riser']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, 'Step 04.3: Verify Number of Scatter XY plots', custom_css="circle[class^='riser']")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 04.4: Verify Legend Title')
        time.sleep(3)
        expected_tooltip_list=['Unit Sales', 'X: Coffee/C141', 'Y: 309K']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g0!mmarker!", expected_tooltip_list, 'Step 04.5: verify the scatter tooltip values')
        time.sleep(3)
        expected_tooltip_list=['Dollar Sales', 'X: Coffee/C141', 'Y: 3.9M']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s1!g0!mmarker!", expected_tooltip_list, 'Step 04.6: verify the scatter tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 04.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 04.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,'C2235070_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()