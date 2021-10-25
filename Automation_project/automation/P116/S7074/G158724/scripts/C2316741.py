'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2316741
TestCase Name = Verify Stacked Area chart via Advance chart tool bar.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea, active_miscelaneous, active_chart_rollup
from common.lib import utillity

class C2316741_TestClass(BaseTestCase):
    def test_C2316741(self):
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        Test_Case_ID="C2316741"
        
        """    1. Right click on folder created in IA and select New > Chart and select GGSALES for the file and From Home tab Select Active Report as Output file format.    """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        
        """    2. Add fields as follows:
                    Category under Columns
                    Product under Horizontal axis
                    Unit Sales, Dollar Sales under Vertical axis.    """
        metadataobj.datatree_field_click('Category', 1, 1, 'Add To Query', 'Columns')
        parent_css="#TableChart_1 g.chartPanel g text[class='colHeader-label!']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        
        """    3. Right click Horizontal Axis and check 'Suppress Empty Group'    """
        result_obj.verify_xaxis_title("TableChart_1", "Product", "Step 03.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        result_obj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 03.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.4: Verify row header and value")
        time.sleep(2)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 03.5: Verify First bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!r0!c0!", "bar_green", "Step 03.6: Verify Second bar color")
        
        """    CheckPoint Parameters    """
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        expected_stacked_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        legend=["Unit Sales", "Dollar Sales"]
        column_values=['Coffee', 'Food', 'Gifts']
        oActiveChart_toolbar=['More Options','Advanced Chart','Original Chart']
        oAggr=['Aggregation']
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        
        """    4. Run the chart.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        time.sleep(2)
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.2: Verify XY labels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 04.4a: Verify First Series bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!r0!c2!", "pale_green", "Step 04.4b: Verify Second Series bar color")
        result_obj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.5: Verify Y-Axis Title")
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', column_values, "Step 04.6: Verify row header and value")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 04.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', oActiveChart_toolbar,"Step 04.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', oAggr,"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 04.11: Verify bar value")
        
        """    5. Select Advance Chart icon from the tool bar. Scroll down to the Area charts.    """
        """    6. Select Stacked Area Chart and click OK.    """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'stackedarea')
        time.sleep(3)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 06.1: Verify -xAxis Title")
        time.sleep(2)
        
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_stacked_yval_list, "Step 06.2: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 06.3: Verify number of Scatter", custom_css=".chartPanel .scrollCharts g circle[class*='marker']")
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!marea!r0!c0!", "bar_blue", "Step 06.4a: Verify First Series bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!marea!r0!c1!", "pale_green", "Step 06.4b: Verify Second Series bar color")
        result_obj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.5: Verify Y-Axis Title")
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', column_values, "Step 06.6: Verify row header and value")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 06.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', oActiveChart_toolbar,"Step 06.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', oAggr,"Step 06.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        '''parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s1!g6!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        time.sleep(2)
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s1!g6!mmarker!r0!c0!", expected_tooltip_list, "Step 06.11: Verify bar value", default_move=True)       
        time.sleep(2)'''
        utillobj.switch_to_default_content(pause=5)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step6', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
         
        
if __name__ == '__main__':
    unittest.main()

