'''
Created on Nov 22 , 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235062
TestCase Name = Horizontal Dual-Axis Stacked Bar Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2235062_TestClass(BaseTestCase):

    def test_C2235062(self):
        
        """
            TESTCASE VARIABLES
        """
        TestCase_ID="C2235062"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj=ia_ribbon.IA_Ribbon(self.driver)
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
            Step 02: From the Format Tab select Chart Types, then Other, then Horizontal Dual-Axis Clustered Bars and Click OK
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'horizontal_dual_axis_stacked_bars', 17, ok_btn_click=True)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='y2axis-labels!m0!']", '0', expire_time=8)
        
        """
            Step 02.1 : Expect to see the following Chart Preview, including areas Vertical axis, Horizontal axis 1 & Horizontal axis 2 areas.
        """
        expected_xval_list=['Group 0','Group 1','Group 2','Group 3','Group 4']
        expected_y1val_list=['0', '20', '40', '60', '80', '100','120']
        expected_y2val_list=['0', '10', '20', '30', '40', '50','60','70','80']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y1val_list, 'Step 02.1 :')
        result_obj.verify_riser_chart_XY_labels('TableChart_1', [], expected_y2val_list, 'Step 02.1 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        result_obj.verify_number_of_riser('TableChart_1', 1, 25, 'Step 02.2 : Verify number of preview risers')
        result_obj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 02.3: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02.4 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 02.5 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "med_green", "Step 02.6 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow_2", "Step 02.7 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 02.8 : Verify preview bar color")
        metadataobj.verify_query_pane_field('Axis','Vertical Axis',1,'Step 02.9 ')
        metadataobj.verify_query_pane_field('Axis','Horizontal Axis 1',2,'Step 02.10 ')
        metadataobj.verify_query_pane_field('Axis','Horizontal Axis 2',3,'Step 02.11 ')
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_02', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 03 : Add field Product under Vertical axis, then add Unit Sales & Budget Units under Horizontal axis 1 and
            Dollar Sales & Budget Dollars under Horizontal axis 2
        """
        metadataobj.datatree_field_click('Product', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Product', expire_time=8)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='yaxis-title']", 'UnitSales', expire_time=8)
        
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s1!']", 'BudgetUnits', expire_time=8)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('Budget Dollars',1,'Horizontal Axis 2',0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='y2axis-title']", 'BudgetDollars', expire_time=8)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('Dollar Sales',1,'Horizontal Axis 2',0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s2!']", 'DollarSales', expire_time=8)
        
        metadataobj.verify_query_pane_field('Horizontal Axis 1','Unit Sales',1,"Step 03.1: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis 1','Budget Units',2,"Step 03.2: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis 2','Dollar Sales',1,"Step 03.3: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis 2','Budget Dollars',2,"Step 03.4: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','Product',1,"Step 03.5: Verify query pane")
          
        """
            Step 03.1 : Expect to see the following Horizontal Dual Axis Stacked Bar Preview panel.
        """
        expected_xval_list=['Capuccino','Espresso']
        expected_y1val_list=['0', '100K', '200K', '300K', '400K', '500K','600K','700K']
        expected_y2val_list=['0', '1M', '2M', '3M', '4M', '5M','6M','7M','8M']
        result_obj.verify_xaxis_title('TableChart_1','Product','Step 03.0 : Verify X-Axis title')
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y1val_list, 'Step 03.6 :')
        result_obj.verify_riser_chart_XY_labels('TableChart_1', [], expected_y2val_list, 'Step 03.6 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        result_obj.verify_number_of_riser('TableChart_1', 1, 8, 'Step 03.7 : Verify number of preview risers')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Budget Units','Dollar Sales','Budget Dollars'], 'Step 03.8: Verify chart preview legends ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.9 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 03.10 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "med_green", "Step 03.11 : Verify preview bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow_2", "Step 03.12 : Verify preview bar color")
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step_03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 04 : Click the Run button to generate the Horizontal Dual Axis Stacked Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s2!']", 'DollarSales', expire_time=10)
        
        """
            Step 04.1 : Expect to see the following Horizontal Dual Axis Stacked Bar Chart.
            Expect to see two sets of Axis scales, one on the top and one on the bottom of the graph.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft','Unit Sales, Budget Units, Dollar Sales, Budget Dollars BY Product','Step 04.1 : Verify Chart title')
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_y1val_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        expected_y2val_list=['0', '4M', '8M', '12M', '16M', '20M','24M']
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Product','Step 04.2 : Verify X-Axis title')
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_y1val_list, 'Step 04.3 :')
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', [], expected_y2val_list, 'Step 04.3 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 40, 'Step 04.4 : Verify number of risers')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Budget Units','Dollar Sales','Budget Dollars'], 'Step 04.5 : Verify chart legends ')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "lochmara", "Step 04.6 : Verify bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!mbar!", "pale_green", "Step 04.7 : Verify bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g4!mbar!", "dark_green", "Step 04.8 : Verify bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g4!mbar!", "pale_yellow", "Step 04.9 : Verify bar color")
        #miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g4!mbar!',['Product:  Croissant', 'Unit Sales:  630054', 'Filter Chart', 'Exclude from Chart'],'Step 04.10 : Verify chart tooltip')
        #miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s1!g4!mbar!',['Product:  Croissant', 'Budget Units:  629989', 'Filter Chart', 'Exclude from Chart'],'Step 04.11 : Verify chart tooltip')
        
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