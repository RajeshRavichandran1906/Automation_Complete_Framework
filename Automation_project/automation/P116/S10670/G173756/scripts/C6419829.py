'''
Created on Jul 4, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/6419829&group_by=cases:section_id&group_order=asc&group_id=173756
TestCase Name : Vertical Dual-Axis Clustered Bar Chart
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon
from common.lib import utillity

class C6419829_TestClass(BaseTestCase):

    def test_C6419829(self):
        
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        preview_chart_css="TableChart_1"
        default_vertical_axis_labels="#TableChart_1 g.chartPanel text[class*='y2axis-labels!']"
        
        """
            Step 01 :Open IA.
            Create a Chart with ggsales.mas
            Select AHTML as the output format.
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#TableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        """
            Expect to see the general Chart Preview panel.
        """
        expected_yval_list=[]
        expected_xval_list=[]
        resobj.verify_riser_chart_XY_labels(preview_chart_css, expected_xval_list, expected_yval_list, 'Step 01:01: X and Y axis labels')
        utillobj.verify_chart_color(preview_chart_css, "riser!s0!g0!mbar!", "lochmara", "Step 01:02: Verify first bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s1!g0!mbar!", "pale_green", "Step 01:03: Verify second bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s2!g0!mbar!", "dark_green", "Step 01:04: Verify third bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s3!g0!mbar!", "pale_yellow_2", "Step 01:05: Verify four bar color")
        utillobj.verify_chart_color(preview_chart_css, "riser!s4!g0!mbar!", "brick_red", "Step 01:06: Verify five bar color")
        expected_label_list=['Series0','Series1','Series2','Series3','Series4']
        resobj.verify_riser_legends(preview_chart_css, expected_label_list, 'Step 01:07: Verify pie chart Legends')
        resobj.verify_number_of_riser(preview_chart_css, 1, 25, 'Step 01:08 Verify the total number of risers displayed on live preview Chart')

        """
            Step 02 :From the Format Tab select Chart Types, then Other, then 
            Vertical Dual-Axis Clustered Bars and
            Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'vertical_dual_axis_clustered_bars', 10, ok_btn_click=True)
        
        """
            Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis
        """
        utillobj.synchronize_with_number_of_element(default_vertical_axis_labels, 10, 35)
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        expected_xval_list=['Group0','Group1','Group2','Group3','Group4']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "lochmara", "Step 02:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 02:03: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "dark_green", "Step 02:04: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow_2", "Step 02:05: Verify four bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 02:06: Verify five bar color")
        resobj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 02.07 : Verify chart legends')
        resobj.verify_number_of_riser('TableChart_1', 1, 25, 'Step 02.08: Verify Number chart segment')
        expected_data_labels=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        resobj.verify_data_labels('TableChart_1', expected_data_labels, "Step 02:09 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        
        """
            Step 03 :Add field Product under X axis, then
            Unit Sales & Budget Units under Vertical Axis 1 and
            Dollar Sales & Budget Dollars under Vertical Axis 2
            Click the Run button.
        """
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Product', 15)
            
        metadataobj.datatree_field_click('Unit Sales',2, 0)
        parent_css="#TableChart_1 g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'UnitSales', 15)
             
        metadataobj.datatree_field_click('Budget Units',2, 0)
        parent_css="#TableChart_1 g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, 'BudgetUnits', 15)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('Dollar Sales', 1, 'Vertical Axis 2', 0)
        parent_css=".y2axis-title"
        utillobj.synchronize_with_visble_text(parent_css, 'Dollar Sales', 15)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('Budget Dollars', 1, 'Vertical Axis 2', 1)
        parent_css="[class='legend-labels!s3!']"
        utillobj.synchronize_with_visble_text(parent_css, 'Budget Dollars', 15)
        
        """
            Expect to see the following Vertical Dual Axis Clustered Bar Preview panel.
        """
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        expected_yval2_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 03.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 03.5: Verify  bar color")
        legend=["Unit Sales","Budget Units","Dollar Sales","Budget Dollars"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6: Verify Y-Axis legend")
        
        """
            Step 04 :Click the Run button to create the AHTML Bar chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "Product", 15)
        
        """
            Expect top see the following Vertical Dual Axis Clustered Bar Chart.
            Expect to see the four Measures in a Clustered Bar Chart with separate Axis scales on left and right sides.
        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '3M', '6M', '9M', '12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 04.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 04.5: Verify  bar color")
        legend=["Unit Sales","Budget Units","Dollar Sales","Budget Dollars"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.6: Verify Y-Axis legend")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Budget Units, Dollar Sales, Budget Dollars by Product', 'Step 04.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()