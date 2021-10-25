'''
Created on Aug 1, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204885
TestCase Name = Verify user is able to use stacked option.
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,active_chart_rollup
from common.lib import utillity


class C2204885_TestClass(BaseTestCase):

    def test_C2204885(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollup_obj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01: Right click on folder created in IA.
        Select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        Expect to see the following Preview pane.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 text[class='legend-labels!s0!']"
        utillobj.synchronize_with_visble_text(parent_css, 'Series0', 65)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(2)
         
        """
        Step 02: Add Category & Product to the Horizontal axis.
        Add Unit Sales & Dollar Sales to the Vertical axis.
        Expect to see the Preview pane with Vertical and Horizontal axis fields.
        """
        metadataobj.datatree_field_click("Category",2,1)
        parent_css= "#TableChart_1 svg g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Category', 8)
        
        metadataobj.datatree_field_click("Product",2,1)
        parent_css= "#TableChart_1 svg g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Category:Product', 8)
         
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        parent_css= "#TableChart_1 svg g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'UnitSales', 8)
         
        metadataobj.datatree_field_click("Dollar Sales", 2, 1)
        parent_css= "#TableChart_1 svg g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, 'DollarSales', 8)
        
        """
        Expect to see the Preview pane with Vertical and Horizontal axis fields.
        """
        xaxis_value="Category : Product"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar1 color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 02: Verify bar2 color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_legend_list, 'Step 02: Verify Legend Title')
         
        """
        Step 03: Click the Run button.
        Expect to see the following Active Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        
        parent_css= "#MAINTABLE_wbody0 svg g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, 'DollarSales', 8)
        
        xaxis_value="Category : Product"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Grinder','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0','2M','4M','6M','8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 3.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03.3: Verify bar1 color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 03.3: Verify bar2 color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 03.4: Verify Legend Title')
        expected_tooltip_list=['Category:Coffee', 'Product:Capuccino', 'Dollar Sales:2381590', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 03.5: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 03.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        Step 04: From the first icon, click the Advanced Chart option.
        Expect to see the following Bar Chart menu.
        """
        rollup_obj.click_pivot_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1 [id^='chticon_1_0_bar1'] [id^='cp_0'] text[class*='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Bar', 6, 1)
        expected_datalabel=['Bar', 'Stacked Bar', 'Percent Bar', 'Column', 'StackedColumn', 'PercentColumn', 'Column Depth', 'Stacked Depth', 'Percent Depth', 'Pie', 'Pie withDepth', 'Donut(Cylinder)', 'Donut withDepth', 'Donut', 'Line', 'Curved', 'Straight', 'Curved +Markers', 'Straight +Markers', 'Step', 'Area', 'Stacked Area', 'Percent Area', 'Scatter(XYPlot)', 'Bubble', 'Funnel', 'Pyramid', 'Heatmap', 'Tag Cloud']
        result_obj.verify_data_labels('wall1', expected_datalabel, 'Step 4: Verify Bar Chart menu', custom_css="[id^='chticon_1_0'] [id^='cp_0'] text[class*='title']")
       
        """
        Step 05: Select the Stacked Column option.
        Click the OK button.
        Expect to see the Clustered Bar chart converted into a Stacked Bar Chart.
        """
        rollup_obj.select_advance_chart('wall1', 'stackedcolumn')
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 20, 10)
      
        xaxis_value="Category : Product"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Grinder','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0','3M','6M','9M','12M','15M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 05.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 05.3: Verify bar1 color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 05.3: Verify bar2 color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 05.4: Verify Legend Title')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 05.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=1)
        
        
if __name__ == '__main__':
    unittest.main()