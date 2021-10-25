'''
Created on Nov 20, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235066
TestCase Name = Horizontal Dual-Axis Stacked Line Graph
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_resultarea, ia_ribbon
from common.lib import utillity


class C2235066_TestClass(BaseTestCase):

    def test_C2235066(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2235066"
        
        """ 
            Step 1 : Create a Chart with ggsales.mas. Select AHTML as the output format.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', expire_time=10)
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType>div[class='bi-button-label']", 'ActiveReport', expire_time=5)
         
        """ 
            Step 2 : Expect to see the general Chart Preview panel.
        """
        expected_xval_list=['Group 0','Group 1','Group 2','Group 3','Group 4']
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2:')
        result_obj.verify_number_of_riser('TableChart_1', 1, 25, 'Step 2.1: Verify number of preview risers')
        result_obj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 2.2: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 2.3: Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 2.4: Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "med_green", "Step 2.5: Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow_2", "Step 2.6: Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 2.7: Verify preview bar color")
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele, Test_Case_ID + '_Actual_Step_02', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """ 
            Step 3 : From the Format Tab select Chart Types, then Other, then 
            Horizontal Dual-Axis Stacked Line Graph and Click OK.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbonobj.select_other_chart_type('line', 'horizontal_dual_axis_stacked_line', 11, ok_btn_click=True)
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 svg path[class*='line']", 5, expire_time=5)
        
        """ 
            Step 4 : Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis.
        """
        expected_xval_list=['Group 0','Group 1','Group 2','Group 3','Group 4']
        expected_yval_list1=['0', '20', '40', '60', '80', '100', '120']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list1, 'Step 4:')
        expected_yval_list2=['0', '10', '20', '30', '40', '50']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list2, 'Step 4.1:', y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 4.2: Verify number of line in preview', custom_css=".chartPanel path[class^='riser']")
        result_obj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 4.3: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 4.4: Verify preview bar color", attribute_type='stroke')
             
        """ 
            Step 5 : Add field Category & Product under the Vertical axis, then
            Budget Dollars & Budget Units under the Horizontal axis 1 and
            Unit Sales under the Horizontal axis 2.
            Three measures are used because additional Measures cannot be distinguished on the graph.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Category', expire_time=8)
        
        metadataobj.datatree_field_click('Product', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Category:Product', expire_time=8)
        
        metadataobj.datatree_field_click('Budget Dollars', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'BudgetDollars', expire_time=8)
        
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s1!']", 'BudgetUnits', expire_time=8)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree("Unit Sales", 1, "Horizontal Axis 2", 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='y2axis-title']", 'UnitSales', expire_time=8)
       
        """ 
            Step 6: Expect to see the following Horizontal Dual Axis Stacked Line Graph Preview panel.
        """
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list1, 'Step 6:')
        expected_yval_list2=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list2, 'Step 6.1:', y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 3, 'Step 6.2: Verify number of line in preview', custom_css=".chartPanel path[class^='riser']")
        result_obj.verify_riser_legends('TableChart_1',['Budget Dollars', 'Budget Units', 'Unit Sales'], 'Step 6.3: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 6.4: Verify preview bar color", attribute_type='stroke')
        
        """ 
            Step 6 : Click the Run button to generate the Horizontal Dual Axis Stacked Line Graph.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2) 
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'BudgetDollars', expire_time=15)
        
        """
            Step 6.1 : Expect top see the following Horizontal Dual Axis Stacked Line Graph.
            Expect to see the three Measures in an Stacked Line Graph with separate Axis scales on the top and bottom of the graph. 
        """
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 'Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos']
        expected_yval_list1=['0', '3M', '6M', '9M', '12M', '15M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list1, 'Step 7:')
        expected_yval_list2=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list2, 'Step 7.1:', y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 7.2: Verify number of line in preview', custom_css=".chartPanel path[class^='riser']")
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Budget Dollars', 'Budget Units', 'Unit Sales'], 'Step 7.3: Verify chart preview legends ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "lochmara", "Step 7.4: Verify preview bar color", attribute_type='stroke')
        #expected_tooltip_list=['Category:  Coffee', 'Product:  Latte', 'Unit Sales:  878063', 'Filter Chart', 'Exclude from Chart']
        #ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s2!g2!mmarker!', expected_tooltip_list, 'Step 04.5 : Verify tooltip')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Budget Dollars, Budget Units, Unit Sales BY Category, Product', 'Step 7.6: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 7.7: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 7.8: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 7.9: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        xaxis_value="Category : Product"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 7.10: Verify X-Axis Title")
        y2axis_value="Unit Sales"
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", y2axis_value, "Step 7.11: Verify Y2-Axis Title",custom_css="svg g text[class*='y2axis-title']")

        utillobj.switch_to_default_content(pause=2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele, Test_Case_ID + '_Actual_Step_06', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()