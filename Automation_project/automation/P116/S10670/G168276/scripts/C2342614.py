'''
Created on Jun 21, 2018

@author: BM13368
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2342614&group_by=cases:section_id&group_order=asc&group_id=168276
TestCase Name = AHTML: Vertical Dual-Axis Absolute & Stacked Line Graphs
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2342614_TestClass(BaseTestCase):

    def test_C2342614(self):
        
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)
        
        time_out=15
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25 

        """
            Step 01 : Sign in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Execute the following URL:
            http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FS10670
            Change the Output type to Active Report.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25 
        
        """
            Step 03 : From the Format Tab select Chart Types, then Other, then 
            Vertical Dual-Axis Absolute Lines and
            Click OK.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5)
        
        ia_ribbobj.select_other_chart_type('line', 'vertical_dual_axis_absolute_line', 4, ok_btn_click=True)
        time.sleep(5)
        
        """
            Expect to see the following Chart Preview, including areas Vertical Axis 1 Measure & Vertical Axis 2 Measure.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.1: Verify XY labels")
        expected_yval2_list=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 02.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 02.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 02.4: Verify  bar color",attribute_type='stroke')
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.9: Verify Y-Axis legend")
        
        """
            Step 04 : Add field Category & Product under the Horizontal axis, then
            Budget Dollars & Budget Units under the Vertical Axis 1 Measure and
            Unit Sales under the Vertical Axis 2 Measure.
            Three measures are used because additional Measures cannot be distinguished on the graph.
        """
        metadataobj.datatree_field_click('Category', 2, 0)
        parent_css="#TableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Category', expire_time=time_out)
        
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Category : Product', expire_time=time_out)
        
        metadataobj.datatree_field_click('Budget Dollars', 2, 0)
        parent_css="#TableChart_1 [class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Budget Dollars', expire_time=time_out)
        
        metadataobj.datatree_field_click('Budget Units', 2, 0)
        parent_css="#TableChart_1 [class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Budget Units', expire_time=time_out)
      
        metadataobj.drag_drop_data_tree_items_to_query_tree('Unit Sales', 1, 'Vertical Axis 2',0)
        parent_css="#TableChart_1 [class='y2axis-title']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Unit Sales', expire_time=time_out)
        
        """
            Expect to see the following Vertical Dual Axis Absolute Line Graph Preview panel.
        """
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval1_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.1: Verify XY labels")
        expected_yval2_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 02.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 3, 'Step 02.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 02.4: Verify  bar color",attribute_type='stroke')
        legend=['Budget Dollars', 'Budget Units', 'Unit Sales']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.9: Verify Y-Axis legend")
        
        """
            Step 05 : Click the Run button to generate the Vertical Dual Axis Absolute Line Graph.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class='xaxisOrdinal-title']", "Category : Product", 15)
        
        """
            Expect top see the following Vertical Dual Axis Absolute Line Graph.
            Expect to see the three Measures in an Absolute Line Graph with separate Axis scales on left and right sides.
        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category : Product", "Step 05.1: Verify -xAxis Title")
        resobj.verify_yaxis_title('MAINTABLE_wbody0', "Unit Sales", "Step 05.2 Verify -y2Axis Title",custom_css="text[class='y2axis-title']")       
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone']
        expected_yval1_list=['0', '3M', '6M', '9M', '12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.3: Verify XY labels")
        expected_yval2_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 05.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 05.7: Verify  bar color",attribute_type='stroke')
        legend=['Budget Dollars', 'Budget Units', 'Unit Sales']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.8: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Budget Dollars, Budget Units, Unit Sales by Category, Product', 'Step 05.9: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 06 : Close Line graph and again from Format tab select Chart Types, then Other, then select Vertical Dual-Axis Stacked Line Chart and Click Ok
        """
        utillobj.switch_to_default_content(pause=1)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5)
        
        ia_ribbobj.select_other_chart_type('line', 'vertical_dual_axis_stacked_line', 5, ok_btn_click=True)
        time.sleep(5)
        
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval1_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.1: Verify XY labels")
        expected_yval2_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 06.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 3, 'Step 06.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 06.4: Verify  bar color",attribute_type='stroke')
        
        """
            Step 07 :Click Run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class='xaxisOrdinal-title']", "Category : Product", 15)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category : Product", "Step 07.1: Verify -xAxis Title")
        resobj.verify_yaxis_title('MAINTABLE_wbody0', "Unit Sales", "Step 07.2 Verify -y2Axis Title",custom_css="text[class='y2axis-title']")       
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone']
        expected_yval1_list=['0', '3M', '6M', '9M', '12M', '15M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.3: Verify XY labels")
        expected_yval2_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.4: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 07.5: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 07.6: Verify  bar color",attribute_type='stroke')
        legend=['Budget Dollars', 'Budget Units', 'Unit Sales']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Budget Dollars, Budget Units, Unit Sales by Category, Product', 'Step 07.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)


if __name__ == "__main__":
    unittest.main()