'''
Created on Nov 17, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235061
TestCase Name = Horizontal Dual-Axis Clustered Bar Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon
from common.lib import utillity

class C2235061_TestClass(BaseTestCase):

    def test_C2235061(self):
        
        Test_Case_ID="C2235061"
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)     
   
        """
            Step 01 : Open IA.Create a Chart with ggsales.masSelect AHTML as the output format
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', expire_time=10)
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType>div[class='bi-button-label']", 'ActiveReport', expire_time=5)
        
        """
            Step 01.1 : Expect to see the following generalized Preview panel.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 01.1: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 01.2: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 01.3: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 01.4: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar", "med_green", "Step 01.5: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar", "pale_yellow_2", "Step 01.6: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar", "brick_red", "Step 01.7: Verify  bar color")
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.8: Verify Y-Axis legend")
        
        """
            Step 02 : From the Format Tab select Chart Types, then Other, then  Horizontal Dual-Axis Clustered Bars and Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'horizontal_dual_axis_clustered_bars', 16, ok_btn_click=True)      
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='y2axis-labels!m0!']", '0', expire_time=8)
        
        """
            Step 02.1 : Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis.
        """
        metadataobj.verify_query_pane_field('Axis', 'Vertical Axis', 1, "step 02.1:Verify Vertical Axis 1")
        metadataobj.verify_query_pane_field('Axis', 'Horizontal Axis 1', 2, "step 02.2:Verify Vertical Axis 2")
        metadataobj.verify_query_pane_field('Axis', 'Horizontal Axis 2', 3, "step 02.2:Verify Horizontal Axis")
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.1: Verify XY labels")
        expected_yval2_list=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 02.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 02.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 02.4: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 02.5: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar", "med_green", "Step 02.6: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar", "pale_yellow_2", "Step 02.7: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar", "brick_red", "Step 02.8: Verify  bar color")
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.9: Verify Y-Axis legend")
        
        """
            Step 03 : Add field Product under X axis, then Unit Sales & Budget Units under Vertical axis 1 and Dollar Sales & Budget Dollars under Vertical axis 2. Click the Run button.
        """
        metadataobj.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g text[class='xaxisOrdinal-title']", 'Product', expire_time=8)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='yaxis-title']", 'UnitSales', expire_time=8)
        
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s1!']", 'BudgetUnits', expire_time=8)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('Budget Dollars',1,'Horizontal Axis 2',0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='y2axis-title']", 'BudgetDollars', expire_time=8)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('Dollar Sales',1,'Horizontal Axis 2',0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s2!']", 'DollarSales', expire_time=8)
        
        """
            Step 03.1 : Expect to see the following Horizontal Dual Axis Clustered Bar Preview panel.
        """
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        expected_yval2_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 03.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 03.5: Verify  bar color")
        legend=["Unit Sales","Budget Units","Dollar Sales","Budget Dollars"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6: Verify Y-Axis legend")
        
        """
            Step 04 : Click the Run button to generate the Horizontal Dual Axis Clustered Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s2!']", 'DollarSales', expire_time=10)
        
        """
            Step 04.1 : Expect to see the following Horizontal Dual Axis Clustered Bar Chart.
            Expect to see two sets of Axis scales on the top and bottom of the graph.
        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '3M', '6M', '9M', '12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 04.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 04.5: Verify  bar color")
        legend=["Unit Sales","Budget Units","Dollar Sales","Budget Dollars"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.6: Verify Y-Axis legend")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Budget Units, Dollar Sales, Budget Dollars BY Product', 'Step 04.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        #expected_tooltip_list=['Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
        #resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar", expected_tooltip_list, "Step 04.11: Verify bar value")
        
        utillobj.switch_to_default_content(pause=3)
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Save Report      
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
          
if __name__ == '__main__':
    unittest.main()