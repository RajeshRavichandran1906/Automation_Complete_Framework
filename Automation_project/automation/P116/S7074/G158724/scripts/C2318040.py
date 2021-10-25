'''
Created on Jul 13, 2017
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318040
TestCase Name = Verify Vertical Box Plot in others tab under Format menu..
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea, active_miscelaneous, ia_ribbon
from common.lib import utillity

class C2318040_TestClass(BaseTestCase):

    def test_C2318040(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        Test_Case_ID="C2318040"
        
        """    1. Right click on folder created in IA. Sselect New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.    """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
         
        """    2. Add fields Product, Unit Sales.    """
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 2a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 2b: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2c: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 2d: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 2e: Verify Color') 
         
        """    3. Click the Run button.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 03a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 03b: Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 03d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'bar_blue', 'Step 03e: Verify bar Color')
        expected_tooltip_list=['Product:Espresso', 'Unit Sales:308986', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g5!mbar!', expected_tooltip_list, 'Step 3f: verify the default tooltip values', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5) 
        
        """    4. Select Format > Other. From Select a chart pop up choose Vertical Box Plot.
                    Add Sequence# to Upper Quartile.
                    Add Dollar Sales to Median.
                    Add Budget Units to Lower Quartile.
                    Add Budget Dollars to Lower Limit.
                    Click OK. """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('special', 'vertical_boxplot', 4, ok_btn_click=True)
        time.sleep(8) 
        metadataobj.drag_drop_data_tree_items_to_query_tree("Sequence#", 1, "Upper quartile", 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        result_obj.wait_for_property(parent_css, 1, string_value='Sequence#', with_regular_exprestion=True)
        time.sleep(2)
        metadataobj.drag_drop_data_tree_items_to_query_tree("Dollar Sales", 1, "Median", 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        metadataobj.drag_drop_data_tree_items_to_query_tree("Budget Units", 1, "Lower quartile", 0)
        parent_css="#queryTreeWindow table tr:nth-child(11) td"
        result_obj.wait_for_property(parent_css, 1, string_value='BudgetUnits', with_regular_exprestion=True)
        metadataobj.drag_drop_data_tree_items_to_query_tree("Budget Dollars", 1, "Lower limit", 0)
        parent_css="#queryTreeWindow table tr:nth-child(13) td"
        result_obj.wait_for_property(parent_css, 1, string_value='BudgetDollars', with_regular_exprestion=True)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4a: ')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 4b: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 4c: Verify Color') 
        
        """    5. Click the Run button.    """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 5a(1): Expect to see 10 bars')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 5a(2): Expect to see 10 line over the bars', custom_css=".chartPanel line[class^='boxplotConnectorLine!s0']")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 5b: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', 'lochmara', 'Step 5c: Verify any one bar color.')  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Sequence#, Dollar Sales, Budget Units, Budget Dollars BY Product', 'Step 5d: Verify Vertical Box Plot Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 5e: Verify Vertical Box Plot Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5f: Verify Vertical Box Plot Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5g: Verify Vertical Box Plot Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['(Series 0 630054, 1481273, 7749902, 629989, 7824715)']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g4!mbar', expected_tooltip_list, 'Step 5h: verify the default tooltip values')
        utillobj.switch_to_default_content(pause=5)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)        
        
if __name__ == '__main__':
    unittest.main()