'''
Created on Jul 20, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318013
TestCase Name = Verify Radar Line Chart in others tab under Format menu.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon, ia_ribbon, ia_resultarea
from common.lib import utillity

class C2318013_TestClass(BaseTestCase):

    def test_C2318013(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2318013'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01: Right click on folder created in IA.
            Select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-labels!g0!mgroupLabel!']"
        utillobj.synchronize_with_visble_text(parent_css, 'Group 0', 10)
        ribbonobj.change_output_format_type('active_report')
        
        """
            Step 02: Add fields Product, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click("Product",2,1)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Product', 8)
         
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        parent_css= "#TableChart_1 svg g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'UnitSales', 8)
         
        metadataobj.datatree_field_click("Dollar Sales", 2, 1)
        parent_css= "#TableChart_1 svg g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, 'DollarSales', 8)
        
        
        xaxis_value="Product"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_legend_list, 'Step 02: Verify Legend Title')
         
        """
            Step 03: Click the Run button. Expect to see the following Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        parent_css= "#MAINTABLE_wbody0 svg g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, 'DollarSales', 15)
        
        xaxis_value="Product"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0','2M','4M','6M','8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 3.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03.3: Verify bar color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 03.4: Verify Legend Title')
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 03.5: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Product', 'Step 03.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=1)
         
        """
            Step 04: Select Format > Other. From Select a chart pop up choose
            Radar Line Chart.
            Click OK.
            Expect to see the Clustered bar chart converted into the Preview pane for Radar Line Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('line', 'radar_line', 15, ok_btn_click=True)
        parent_css="#TableChart_1 svg g text[class='xaxis-labels!m0!']"
        utillobj.synchronize_with_visble_text(parent_css, 'Capuccino', 10)
        
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xval_list, expected_yval_list, 'Step 04: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1', 2, 'Step 04: Verify Number of riser', custom_css=".chartPanel>g>g>path")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 04: Verify bar1 color",attribute_type='stroke',custom_css=".chartPanel>g>g>path")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('pfjTableChart_1', expected_legend_list, 'Step 04: Verify Legend Title')
       
     
        """
        Step 05: Click the Run button.
        Expect to see the following Radar Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        parent_css= "#MAINTABLE_wbody0 svg g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, 'DollarSales', 15)
        
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0','2M','4M','6M','8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 04: Verify Number of riser', custom_css=".chartPanel>g>g>path")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "lochmara", "Step 04: Verify bar1 color",attribute_type='stroke',custom_css=".chartPanel>g>g>path")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 04: Verify Legend Title')
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .chartPanel>g text[class='yaxis-labels!m2!']")
        utillobj.click_on_screen(riser_css, 'middle',mouse_duration=2.5, y_offset=-2)
        expected_tooltip_list=['5.3M']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', None, expected_tooltip_list, 'Step 05.6: verify the default tooltip values', default_move=True)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Product', 'Step 05.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=1)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2318013_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()