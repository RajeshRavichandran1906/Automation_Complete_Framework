'''
Created on May 1, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234933
TestCase Name = Verify Origianl chart icon shows original chart on a chart window
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_chart_rollup, active_miscelaneous, ia_resultarea


class C2234933_TestClass(BaseTestCase):

    def test_C2234933(self):
        
        """
            TESTCASE Functions Object
        """

        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        chart_rollup_obj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
             
        """ Step 1: Execute the attached C2205032.fex in IA.
                    Verify that bar chart is displayed on canvas with selected data.
        """
        utillobj.active_run_fex_api_login('C2205032.fex', 'S7074', 'mrid', 'mrpass')
        time.sleep(2)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollRowAxis text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(2)
#         result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 1.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 1.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 1.3: ')
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category : Product', ['Coffee', 'Food', 'Gifts'], 'Step 1.4: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 1.5: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', 'bar_blue', 'Step 1.6: Verify Color')
        expected_tooltip_list=['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', expected_tooltip_list, 'Step 1.7: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 1.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 1.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 1.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 1.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        
        """ Step 2: From the Advanced Chart icon, select PIE(Bevel)(1st icon).
                    Verify that "Unit Sales by Category, Product" Pie chart is displayed on canvas with selected data.
        """
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        parent_css="#wall1 [class='arWindowBarTitle']"
        result_obj.wait_for_property(parent_css, 1, string_value='Chart/RollupTool', with_regular_exprestion=True)
        chart_rollup_obj.select_advance_chart('wall1', 'piebevel')
        time.sleep(3)
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category : Product', ['Coffee', 'Food', 'Gifts'], 'Step 2: ')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 30, 'Step 2.1: Expect to see the three PIE Chart Visible.')
        expected_label_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 2.2: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mwedge', 'bar_blue', 'Step 2.3: Verify color.')  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 2.4: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 2.5: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2.6: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 2.7: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales','Unit Sales', 'Unit Sales'],"'Step 2.8: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
            
         
        """ Step 3: Click Original Chart(3rd icon).
                    Verify that chart restores to the original display.
        """
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 2)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollRowAxis text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(2)
#         result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 3.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.3: ')
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category : Product', ['Coffee', 'Food', 'Gifts'], 'Step 3.4: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 3.5: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', 'bar_blue', 'Step 3.6: Verify Color')
        expected_tooltip_list=['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', expected_tooltip_list, 'Step 3.7: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 3.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 3.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        
if __name__ == '__main__':
    unittest.main()