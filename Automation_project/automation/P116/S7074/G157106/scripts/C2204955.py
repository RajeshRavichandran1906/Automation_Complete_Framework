'''
Created on Jul 19, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204955
TestCase Name = Verify user can delete columns by clicking X next to column name.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, ia_resultarea, active_chart_rollup, active_tools
from common.lib import utillity

class C2204955_TestClass(BaseTestCase):

    def test_C2204955(self):
        driver = self.driver
         
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        activeobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_toolsobj = active_tools.Active_Tools(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        
        """
        1. Execute attached fex "AR-CH-033.fex" in IA.
        """
        utillobj.active_run_fex_api_login("AR-CH-033.fex", "S7074", 'mrid', 'mrpass')
        
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
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales BY Category, Product', 'Step 01.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
        2. Click Chart/Rollup Tool option from the dropdown menu.
        Verify that Chart/Rollup Tool pop up opened.
        Verify that two tabs are displayed: Series and Charts.
        """
        
        activeobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Chart/Rollup Tool', elem_index=0, custom_css='cpop')
        
        css="#wall1 #charttoolt1 #tpanel_0_1_0"
        utillobj.synchronize_with_number_of_element(css, 1, 30)
        
        utillobj.verify_object_visible(css, True, 'Step 2.1: Verify that Chart/Rollup Tool pop up opened')
        series_tab="#charttoolt1 #ttpanel_0_1_0[class*='arToolTabSelected']"
        utillobj.verify_object_visible(series_tab, True, 'Step 2.2: Verify that Series tab is displayed: Series and Charts.')
        chart_tab="#charttoolt1 #ttpanel_1_1_0[class*='arToolTab']"
        utillobj.verify_object_visible(chart_tab, True, 'Step 2.3: Verify that Charts tab is displayed: Series and Charts.')
        
        """
        3. By Default user is on Series tab.
        Verify that Series tab shows Columns, Group By and Measures sub-sections.
        Verify that Group By shows - Category and Product.
        Verify Measures shows Unit Sales.
        """
        time.sleep(3)
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'Category', 'Product', 'Unit Sales'], 'Step 03.1: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Category', 'Product'], 'Step 03.2: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Sum:', 'Unit Sales'], 'Step 03.3: Expect to see the following Advanced Chart menu.')
        time.sleep(3)
        
        """
        4. Now delete Product from Group By.  
        Verify that Group By shows only Category and Measure shows only Unit Sales.
        Verify that Measure shows Product and Unit Sales
        Click OK to verify.
        """
        active_toolsobj.chart_rollup_tool_delete_column_items('charttoolt1', 2, 1)
        time.sleep(4)
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Category'], 'Step 04.1: Verify that Group By now shows only Category column')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Sum:', 'Unit Sales'], 'Step 04.2: Verify that Measure shows Unit Sales only.')
        time.sleep(2)
        active_toolsobj.chart_rollup_tool_close('charttoolt1', 'Ok')  
        
        """
        Expect to see a 3 Bar chart.
        """
        parent_css="#MAINTABLE_wbody0 g[class^='riser'] rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, 45)
        
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 4(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 4(ii) Verify Y Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.a: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 04.b: Verify number of risers', custom_css ="g[class^='riser'] rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "cerulean_blue", "Step 04.c: Verify bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales BY Category', 'Step 04.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 04.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,'C2204955_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()