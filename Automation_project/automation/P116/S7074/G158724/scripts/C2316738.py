'''
Created on JUN 27, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2316738
TestCase Name = Verify Step Line chart via Advance chart tool bar.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity

class C2316738_TestClass(BaseTestCase):

    def test_C2316738(self):
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        rollupobj =active_chart_rollup.Active_Chart_Rollup(driver)
        Test_Case_ID="C2316738"
        
        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        element_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        ribbonobj.change_output_format_type('active_report', location='Home')
        element_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        """
            Step 02:Add fields as follows: Category under Columns. Product under Horizontal axis. Unit Sales, Dollar Sales under Vertical axis.
        """
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        element_css="#TableChart_1 g.chartPanel g text[class='colHeader-label!']"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 20)
        
        metadataobj.datatree_field_click('Product', 2, 0)
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 20)
        
        metadataobj.datatree_field_click('Unit Sales',2, 0)
        element_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 20)
        
        metadataobj.datatree_field_click('Dollar Sales',2, 0)
        element_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 20)
        
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 02.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 02.3: Verify the total number of risers displayed on preview')
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 02.4: Verify row header and value")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 02.5: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.6:")
        """
            Step 03: Right click Horizontal Axis and check 'Suppress Empty Group'
        """ 
        metadataobj.querytree_field_click("Horizontal Axis",1, 'Suppress Empty Group')
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 03.3: Verify the total number of risers displayed on preview')
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.4: Verify row header and value")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 03.5: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6:")
        """
            Step 04:Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 04.4: Verify  bar color")
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.5: Verify Y-Axis Title")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 04.6: Verify row header and value")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 04.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!r0!c0!", expected_tooltip_list, "Step 04.11: Verify bar value")
        
        """
            Step 05:Select Advance Chart icon from the tool bar. Scroll down to the Line Charts.
            Step 06:Select Step line and click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        rollupobj.select_advance_chart('wall1', 'stepline')
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 06.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 06.2: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 06.3: Verify number of segment", custom_css=".chartPanel .scrollCharts g circle[class*='marker']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 06.4: Verify  bar color",attribute_type='stroke')
        legend=["Unit Sales", "Dollar Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.5: Verify Y-Axis Title")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 06.6: Verify row header and value")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Category, Product', 'Step 06.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'start')
#         parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g6!mmarker!r0!c0!']")
#         utillobj.click_on_screen(parent_obj,'start', javascript_marker_enable=True, mouse_duration=2.5)
#         expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s1!g6!mmarker!r0!c0!", expected_tooltip_list, "Step 06.11: Verify bar value", default_move=True)
        utillobj.switch_to_default_content(pause=3)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step6', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)

if __name__ == '__main__':
    unittest.main()          