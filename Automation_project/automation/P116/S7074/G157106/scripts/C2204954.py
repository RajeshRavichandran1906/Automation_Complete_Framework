'''
Created on Jul 19, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204954
TestCase Name = Verify user can edit (drag-drop) columns.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, ia_resultarea, active_chart_rollup, active_tools
from common.lib import utillity

class C2204954_TestClass(BaseTestCase):

    def test_C2204954(self):
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
        
        Test_Case_ID = 'C2204954'
        
        """
        1. Execute attached fex "AR-CH-033.fex" in IA.
        """
        utillobj.active_run_fex_api_login("AR-CH-033.fex", "S7074", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 g[class^='riser'] rect[class^='riser']", 10, 65)
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 1(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 1(ii) Verify Y Axis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.a: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 01.b: Verify number of risers', custom_css ="g[class^='riser'] rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "cerulean_blue", "Step 01.c: Verify bar color")
        expected_tooltip_list=['Unit Sales, Coffee/Latte: 878,063']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 01.d: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales BY Category, Product', 'Step 01.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        2. Click Chart/Rollup Tool option from the dropdown menu.
        Verify that Chart/Rollup Tool pop up opened.
        Verify that two tabs are displayed: Series and Charts.
        """
        activeobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Chart/Rollup Tool', elem_index=0, custom_css='cpop')
        utillobj.synchronize_with_number_of_element("#wall1 #charttoolt1 #ttpanel_0_1_0", 1, 25)
        css="#wall1 #charttoolt1 #tpanel_0_1_0"
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
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'Category', 'Product', 'Unit Sales'], 'Step 03.1: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Category', 'Product'], 'Step 03.2: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Sum:', 'Unit Sales'], 'Step 03.3: Expect to see the following Advanced Chart menu.')
        time.sleep(3)
        
        """
        4. Now delete Product from Group By section and drag-drop Product under Measure. 
        Verify that Group By now shows only Category column
        Verify that Measure shows Product and Unit Sales
        """
        active_toolsobj.chart_rollup_tool_delete_column_items('charttoolt1', 2, 1)
        time.sleep(3)
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product', 1, 'Measure', 1)
        time.sleep(4)
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Category'], 'Step 04.1: Verify that Group By now shows only Category column.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Sum:', 'Unit Sales', 'Count:', 'Product'], 'Step 04.2: Verify that Measure shows Product and Unit Sales')
        time.sleep(2)
        
        """
        5. Click Ok.
        Verify that chart is updated with changes. Title changes to "Unit Sales, Product BY Category"
        """
        active_toolsobj.chart_rollup_tool_close('charttoolt1', 'Ok')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 g[class^='riser'] rect[class^='riser']", 6, 25)  
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 5(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 5(ii) Verify Y Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.a: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 6, 'Step 05.b: Verify number of risers', custom_css ="g[class^='riser'] rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "cerulean_blue", "Step 05.c: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales, Product BY Category', 'Step 05.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 05.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()