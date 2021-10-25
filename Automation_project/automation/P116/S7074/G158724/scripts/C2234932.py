'''
Created on May 10, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234932
TestCase Name = Verify BAR, PIE, LINE, AREA & SCATTER charts are displayed correctly
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_chart_rollup, ia_resultarea, active_miscelaneous,visualization_metadata,visualization_ribbon
from common.lib import utillity


class C2234932_TestClass(BaseTestCase):

    def test_C2234932(self):
        """
            TESTCASE Functions Object
        """
        Test_Case_ID ="C2234932"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        chart_rollup_obj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj= visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
          
        """ Step 1: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
                    On the Format tab, in the Output Types group, click Active report.
            Step 2: Select data from the left pane (Dimensions and Measures)
                    Category under Columns
                    Product under Horizontal Axis, & Unit Sales under Vertical Axis
                    See corresponding data is displayed in the Live Preview pane.
            Step 3: Click the Run button.
                    Verify that bar chart is displayed on canvas with selected data.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        #result_obj.wait_for_property(parent_css, 1)  
        utillobj.synchronize_with_number_of_element(parent_css,1,38)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        #result_obj.wait_for_property(parent_css, 1)
        utillobj.synchronize_with_number_of_element(parent_css,1,30)
        time.sleep(3)
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        parent_css="#queryTreeWindow tr:nth-child(5) td img.icon"
        #result_obj.wait_for_property(parent_css, 1)
        utillobj.synchronize_with_number_of_element(parent_css, 1,25)
        parent_css="#TableChart_1 g text[class='colHeader-label!']"
        #result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'Category',15)
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 g text[class='xaxisOrdinal-title']"
        #result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)     
        utillobj.synchronize_with_visble_text(parent_css,'Product',15)
        metadataobj.datatree_field_click('Unit Sales',2, 0)
        parent_css="#TableChart_1 g text[class='yaxis-title']"
        #result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)      
        utillobj.synchronize_with_visble_text(parent_css,'UnitSales',15)
        time.sleep(5)        
        result_obj.verify_xaxis_title("TableChart_1", "Product", "Step 01.1: Verify -xAxis Title")
        result_obj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 01.2: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.3: Verify XY labels")
        result_obj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 01.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0", "bar_blue1", "Step 01.5: Verify  bar color")
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 01.6: Verify row header and value")
        """
            Step 03:Click Run.
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        #result_obj.wait_for_property(parent_css, 1)
        utillobj.synchronize_with_number_of_element(parent_css, 1,25)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollRowAxis text[class*='yaxis-title']"
        #result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'UnitSales',15)
        time.sleep(2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 3.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.3: ')
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], 'Step 3.4: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 3.5: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', 'bar_blue', 'Step 3.6: Verify Color')
        expected_tooltip_list=['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c1!', expected_tooltip_list, 'Step 3.7: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 3.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 3.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", expected_tooltip_list, "Step 03.12: Verify bar value")
        """ Step 4: From the icons at the top, change the Bar Chart to the first PIE chart.
                    Expect to see the Bar Chart converted to a PIE chart.
        """
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        parent_css="#wall1 [class='arWindowBarTitle']"
        #result_obj.wait_for_property(parent_css, 1, string_value='Chart/RollupTool', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'Chart/RollupTool',15)
        chart_rollup_obj.select_advance_chart('wall1', 'piebevel')
        time.sleep(5)
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], 'Step 4: ')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 30, 'Step 4.1: Expect to see the three PIE Chart Visible.')
        expected_label_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 4.2: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mwedge!r0!c1!', 'bar_blue', 'Step 4.3: Verify second pie color.')  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 4.4: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4.5: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4.6: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4.7: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales','Unit Sales', 'Unit Sales'],"'Step 4.8: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        expected_tooltip_list=['Product:Capuccino', 'Category:Coffee', 'Unit Sales:189217', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mwedge!r0!c0!", expected_tooltip_list, "Step 05: Verify bar value")
        time.sleep(5)
          
        """ Step 5: From the icons at the top, change the PIE chart to the first Line chart.
                    Expect to see the Bar Chart converted to a Line chart.
        """
          
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        parent_css="#wall1 [class='arWindowBarTitle']"
        #result_obj.wait_for_property(parent_css, 1, string_value='Chart/RollupTool', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'Chart/RollupTool',15)
        chart_rollup_obj.select_advance_chart('wall1', 'line')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollRowAxis text[class*='yaxis-title']"
        #result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'UnitSales',15)
        time.sleep(2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 5.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 5.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 5.3: ')
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], 'Step 5.4: ')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, 'Step 5.5: Expect to see the three PIE Chart Visible.')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 5.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 5.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 5.10: Verify second Line color",attribute_type='stroke')
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g5!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Category:Coffee', 'Product:Espresso', 'Unit Sales:308986', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s0!g5!mmarker!r0!c0!", expected_tooltip_list, "Step 05: Verify bar value", default_move=True)
        """ Step 6: From the icons at the top, change the Line chart to the first Area chart.
                    Expect to see the Line Chart converted to an Area chart.
        """
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        parent_css="#wall1 [class='arWindowBarTitle']"
        #result_obj.wait_for_property(parent_css, 1, string_value='Chart/RollupTool', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'Chart/RollupTool',15)
        chart_rollup_obj.select_advance_chart('wall1', 'area')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollRowAxis text[class*='yaxis-title']"
        #result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'UnitSales',15)
        time.sleep(2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 6.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 6.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 6.3: ')
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], 'Step 6.4: ')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, 'Step 6.5: Expect to see the three PIE Chart Visible.')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 6.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 6.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 6.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 6.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea!r0!c0!', 'bar_blue', 'Step 6.10: Verify area color.') 
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g6!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s0!g6!mmarker!r0!c0!", expected_tooltip_list, "Step 05: Verify bar value",default_move=True)
        time.sleep(3)
        """ Step 7: From the icons at the top, change the Area chart to a Scatter diagram.
                    Expect to see the Area Chart converted to a SCATTER diagram.
        """
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        parent_css="#wall1 [class='arWindowBarTitle']"
        #result_obj.wait_for_property(parent_css, 1, string_value='Chart/RollupTool', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'Chart/RollupTool',15)
        chart_rollup_obj.select_advance_chart('wall1', 'scatter(xy_plot)')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollRowAxis text[class*='yaxis-title']"
        #result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css,'UnitSales',15)
        time.sleep(2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 7.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 7.2: Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 7.3: ')
        result_obj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee', 'Food', 'Gifts'], 'Step 7.4: ')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 7.5: Expect to see the scatter Chart Visible.')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 7.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 7.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 7.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 7.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g1!mmarker!r0!c0!', 'bar_blue', 'Step 7.10: Verify second Line color.', custom_css=".chartPanel .groupPanel g[stroke]", attribute_type='stroke') 
        expected_tooltip_list=['Category:Coffee', 'Product:Espresso', 'Unit Sales:308986', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g1!mmarker!r0!c0!", expected_tooltip_list, "Step 05: Verify bar value",cord_type='middle',x_offset=-4,y_offset=-8)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step7', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()