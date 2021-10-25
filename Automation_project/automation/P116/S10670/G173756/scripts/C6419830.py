'''
Created on July 05, 2018

@author: Bhagavathi

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6419830
TestCase Name = Vertical Dual-Axis Stacked Bar Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon, metadata
from common.lib import utillity

class C6419830_TestClass(BaseTestCase):

    def test_C6419830(self):
        
        Test_Case_ID="C6419830"
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        meta_obj=metadata.MetaData(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)      
          
        """
            Step 01 : Open IA.Create a Chart with ggsales.masSelect AHTML as the output format
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', 65)
        
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType>div[class='bi-button-label']", 'ActiveReport',15)
        
        """
            Step 01.1 : Expect to see the general Chart Preview panel.
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
            Step 02 : From the Format Tab select Chart Types, then Other, then Vertical Dual-Axis Stacked Bars and Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'vertical_dual_axis_stacked_bars', 11, ok_btn_click=True)  
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='y2axis-labels!m0!']", '0', expire_time=8)
        
        """
            Step 02.1 : Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis.
        """    
        metadataobj.verify_query_pane_field('Axis', 'Vertical Axis 1', 1, "step 02.1:Verify Vertical Axis 1")
        metadataobj.verify_query_pane_field('Axis', 'Vertical Axis 2', 2, "step 02.2:Verify Vertical Axis 2")
        metadataobj.verify_query_pane_field('Axis', 'Horizontal Axis', 3, "step 02.2:Verify Horizontal Axis")
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '20', '40', '60', '80', '100', '120']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.1: Verify XY labels")
        expected_yval2_list=['0', '10', '20', '30', '40', '50', '60', '70', '80']
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
            Step 03 : Add field Product under X axis, then
            Unit Sales & Budget Units under Vertical axis 1 and
            Dollar Sales & Budget Dollars under Vertical axis 2.
            Click the Run button.
        """
        meta_obj.double_click_on_data_filed("Product")
        utillobj.synchronize_with_visble_text("#TableChart_1 g text[class='xaxisOrdinal-title']", 'Product', 10)
        
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='yaxis-title']", 'UnitSales', 10)
        
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s1!']", 'Budget Units', 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('Dollar Sales',1,'Vertical Axis 2',0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s2!']", 'DollarSales', 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('Budget Dollars',1,'Vertical Axis 2',1)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='y2axis-title']", 'BudgetDollars', 10)
        
        """
            Step 03.1 : Expect to see the following Vertical Dual Axis Clustered Bar Preview panel.
        """
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.1: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        expected_yval2_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 03.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 03.5: Verify  bar color")
        legend=["Unit Sales","Budget Units","Dollar Sales","Budget Dollars"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6: Verify Y-Axis legend")
        
        """
            Step 04 : Click the Run button to generate the Vertical Dual Axis Stacked Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s2!']", 'DollarSales', 15)
        
        """
            Step 04.1 : Expect to see the four Measures in a Stacked Bar Chart with separate Axis scales on left and right sides.
            Expect to see the following Vertical Dual Axis Stacked Bar Chart.
            Expect to see two sets of Axis scales on the left and right sides of the graph.
        """
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '4M', '8M', '12M', '16M', '20M', '24M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 04.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 04.5: Verify  bar color")
        legend=["Unit Sales","Budget Units","Dollar Sales","Budget Dollars"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.6: Verify Y-Axis legend")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Budget Units, Dollar Sales, Budget Dollars BY Product', 'Step 04.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        utillobj.switch_to_default_content(pause=3)
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        
if __name__ == '__main__':
    unittest.main()    
