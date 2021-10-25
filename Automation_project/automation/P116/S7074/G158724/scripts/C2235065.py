'''
Created on August 09, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235065
TestCase Name = Horizontal Dual-Axis Absolute Line Graph
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2235065_TestClass(BaseTestCase):

    def test_C2235065(self):
        
        """
        TESTCASE VARIABLES
        """
        TestCase_ID="C2235065"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01 : Create a Chart with ggsales.masSelect AHTML as the output format..
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', expire_time=10)
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType>div[class='bi-button-label']", 'ActiveReport', expire_time=5)
        
        """
            Step 01.1 : Expect to see the following generalized Preview Panel.
        """
        expected_xval_list=['Group 0','Group 1','Group 2','Group 3','Group 4']
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.1 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 25, 'Step 01.2 : Verify number of preview risers')
        result_obj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 01.3: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01.4 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 01.5 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "med_green", "Step 01.6 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow_2", "Step 01.7 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 01.8 : Verify preview bar color")
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_01', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 02 : From the Format Tab select Chart Types, then Other, then Horizontal Dual-Axis Absolute Line Graph and Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('line','horizontal_dual_axis_absolute_line', 10, ok_btn_click=True)
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 svg path[class*='line']", 5, expire_time=5)
        
        """
            Step 02.1 : Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis.
        """
        expected_xval_list=['Group 0','Group 1','Group 2','Group 3','Group 4']
        expected_y1val_list=['0', '10', '20', '30', '40', '50']
        expected_y2val_list=['0', '5', '10', '15', '20', '25','30','35','40','45']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y1val_list, 'Step 02.1 :')
        result_obj.verify_riser_chart_XY_labels('TableChart_1', [], expected_y2val_list, 'Step 02.1 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 02.2: Verify number of line in preview', custom_css=".chartPanel path[class^='riser']")
        result_obj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 02.3: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 02.4 : Verify preview bar color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "bar_green", "Step 02.5 : Verify preview bar color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mline!", "med_green", "Step 02.6 : Verify preview bar color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mline!", "pale_yellow_2", "Step 02.7 : Verify preview bar color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mline!", "brick_red", "Step 02.8 : Verify preview bar color",attribute_type='stroke')
        metadataobj.verify_query_pane_field('Axis','Vertical Axis',1,'Step 02.9 : ')
        metadataobj.verify_query_pane_field('Axis','Horizontal Axis 1',2,'Step 02.10 : ')
        metadataobj.verify_query_pane_field('Axis','Horizontal Axis 2',3,'Step 02.11 : ')
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_02', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 03 : Add field Category & Product under the Vertical axis, then
            Budget Dollars & Budget Units under the Horizontal axis 1 and
            Unit Sales under the Horizontal axis 2.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Category', expire_time=8)
        
        metadataobj.datatree_field_click('Product', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Category:Product', expire_time=8)
        
        metadataobj.datatree_field_click('Budget Dollars', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'BudgetDollars', expire_time=8)
        
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s1!']", 'BudgetUnits', expire_time=8)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree("Unit Sales", 1, "Horizontal Axis 2", 0, target_cord='middle')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='y2axis-title']", 'UnitSales', expire_time=8)
        
        """
            Step 03.1 : Expect to see the following Horizontal Dual Axis Absolute Line Graph Preview panel.
        """
        result_obj.verify_xaxis_title('TableChart_1','Category : Product','Step 03.1 : Verify X-Axis title')
        result_obj.verify_yaxis_title('TableChart_1','Unit Sales','Step 03.2 : Verify Y2-Axis title',custom_css=" text[class='y2axis-title']")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_y1val_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        expected_y2val_list=['0', '50K', '100K', '150K', '200K', '250K','300K','350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y1val_list, 'Step 03.3 :')
        result_obj.verify_riser_chart_XY_labels('TableChart_1', [], expected_y2val_list, 'Step 03.4 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 3, 'Step 03.5: Verify number of line in preview', custom_css=".chartPanel path[class^='riser']")
        result_obj.verify_riser_legends('TableChart_1',['Budget Dollars','Budget Units','Unit Sales'], 'Step 03.6: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 03.7 : Verify preview bar color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "bar_green", "Step 03.8 : Verify preview bar color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mline!", "med_green", "Step 03.9 : Verify preview bar color",attribute_type='stroke')
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 04: Click the Run button to generate the Horizontal Dual Axis Absolute Line Graph.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'BudgetDollars', expire_time=15)
        
        """
            Step 04.1 : Expect top see the following Horizontal Dual Axis Absolute Line Graph.
            Expect to see the three Measures in an Absolute Line Graph with separate Axis scales on the top and bottom of the graph.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft','Budget Dollars, Budget Units, Unit Sales BY Category, Product','Step 04.1 : Verify Chart title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Category : Product','Step 04.2 : Verify X-Axis title')
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales','Step 04.3 : Verify Y2-Axis title',custom_css=" text[class='y2axis-title']")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Grinder','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_y1val_list=['0', '3M', '6M', '9M', '12M']
        expected_y2val_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_y1val_list, 'Step 04.4 :')
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', [], expected_y2val_list, 'Step 04.4 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 04.6 : Verify number of line in preview', custom_css=".chartPanel path[class^='riser']")
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Budget Dollars','Budget Units','Unit Sales'], 'Step 04.7 : Verify chart legends ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "lochmara", "Step 04.8 : Verify bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 04.9 : Verify bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!mline!", "dark_green", "Step 04.10 : Verify bar color",attribute_type='stroke')
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 circle[class='marker!s2!g2!mmarker!']")
        utillobj.click_on_screen(parent_elem, 'middle', x_offset=-11, javascript_marker_enable=True, mouse_duration=2.5)
        #expected_tooltip_list=['Category:  Coffee', 'Product:  Latte', 'Unit Sales:  878063', 'Filter Chart', 'Exclude from Chart']
        #miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'marker!s1!g2!mmarker!', expected_tooltip_list, "Step 04.11 : Verify tooltip values.", default_move=True)
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.12 : Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.13 : Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.14 : Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        utillobj.switch_to_default_content(pause=1)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_04', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Save Report      
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(TestCase_ID)
        
if __name__=='__main__' :
    unittest.main()