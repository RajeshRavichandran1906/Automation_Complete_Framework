'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234943
TestCase Name = Horizontal Dual-Axis Stacked Line Graph 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_ribbon, active_miscelaneous,ia_resultarea
from common.lib import utillity

class C2234943_TestClass(BaseTestCase):

    def test_C2234943(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        Test_Case_ID="C2234943"
         
        """    Step 1: Create a Chart with ggsales.mas
                    From Home tab Select Active Report as Output file format.    """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        element_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        ribbonobj.change_output_format_type('active_report')
        
        """    Step 2: From the Format Tab select Chart Types, then Other, then
                    Vertical Dual-Axis Absolute Lines and
                    Click OK.     """
        element_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(element_css, 'ActiveReport', 20)
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbonobj.select_other_chart_type('line', 'horizontal_dual_axis_stacked_line', 11, ok_btn_click=True)
           
        """ Step 3: Add field Category & Product under the X axis, then
                    Budget Dollars & Budget Units under the Y1 Measure and
                    Unit Sales under the Y2 Measure.
                    Three measures are used because additional Measures cannot be distinguished on the graph.    """ 
        metadataobj.datatree_field_click('Category', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 20)
        metadataobj.datatree_field_click('Product', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Category:Product', 20)
        metadataobj.datatree_field_click('Budget Dollars', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'BudgetDollars', 20)
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        element_css="#TableChart_1 g.legend g text[class='legend-labels!s0!']"
        utillobj.synchronize_with_visble_text(element_css, 'BudgetDollars', 20)
        element_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(element_css, 'BudgetUnits', 20)
        metadataobj.drag_drop_data_tree_items_to_query_tree("Unit Sales", 1, "Horizontal Axis 2", 0)
        element_css="#TableChart_1 g.legend g text[class='legend-labels!s2!']"
        utillobj.synchronize_with_visble_text(element_css, 'Unit Sales', 20)
        
        result_obj.verify_xaxis_title("TableChart_1", 'Category : Product', "Step 3a: Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3b: Verify XY Label')
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_y2val_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']        
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y2val_list, 'Step 3c: Verify Y2 Label', y_custom_css="text[class^='y2axis-labels']")
        expected_label_list=['Budget Dollars', 'Budget Units', 'Unit Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 3d: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mline!', 'bar_blue1', 'Step 3e(i): Verify Color', attribute_type='stroke')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mline!', 'bar_green', 'Step 3e(ii): Verify Color', attribute_type='stroke')
        utillobj.verify_chart_color('TableChart_1', 'riser!s2!g0!mline!', 'med_green', 'Step 3e(iii): Verify Color', attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 3, "Step 03.e: Verify number of line",custom_css=".chartPanel path[class*='riser']")
        
        """    Step 3: Click the Run button to generate the Vertical Dual Axis Absolute Line Graph.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category : Product', "Step 4a: Verify X-Axis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        expected_x2val_list=[]
        expected_y2val_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4b: Verify XY Label')
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_x2val_list, expected_y2val_list, 'Step 4c: Verify Y2 Label', y_custom_css="text[class^='y2axis-labels']")
        expected_label_list=['Budget Dollars', 'Budget Units', 'Unit Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 4d Verify Legends ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mline!', 'lochmara', 'Step 4e(i): Verify Color', attribute_type='stroke')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mline!', 'pale_green', 'Step 4e(ii): Verify Color', attribute_type='stroke')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mline!', 'dark_green', 'Step 4e(iii): Verify Color', attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, "Step 04.: Verify number of line",custom_css=".chartPanel path[class*='riser']")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Budget Dollars, Budget Units, Unit Sales BY Category, Product', 'Step 04g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()