'''
Created on June 9, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234971
TestCase Name = Verify Scatter chart with PRODUCT in color bucket
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_resultarea
from common.lib import utillity


class C2234971_TestClass(BaseTestCase):

    def test_C2234971(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        Test_Case_ID="C2234971"
        
        
        """ Step 1: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        
        
        """ step 2: On the Format tab, in the Output Types group, click Active report.
                    Select Chart Types as 'Scatter'
        """
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(9)
        ribbonobj.select_ribbon_item("Format", "Scatter")
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 17)
        
        
        """ Step 3: Select fields in the query pane as follows:
                    Unit Sales under Vertical Axis
                    Category under Horizontal Axis
                    Product under Color
        """
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Category', 1, 1, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 1, 1, 'Add To Query', 'Color')
        parent_css="#TableChart_1 g.legend text[class*='legend-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        time.sleep(2)
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title('TableChart_1', 'Unit Sales', 'Step 3.2: Verify y-Axis Title')
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.3: Verify XY Label')
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 3.4 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 3.5: Verify Color', custom_css=".chartPanel .groupPanel .markers g:nth-child(1)" ,attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 3.6: Verify Number of circle', custom_css="svg g circle[class^='riser']")
        
        
        """ Step 4: Click Run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category', "Step 4.1: Verify X-Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 4.3: Verify Number of circle', custom_css="svg g circle[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'bar_blue', 'Step 4.4: Verify Color', custom_css=".chartPanel .groupPanel .markers g:nth-child(1)" ,attribute_type='stroke')
        expected_tooltip_list=['Category:Food', 'Unit Sales:421377', 'Product:Biscotti', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mmarker', expected_tooltip_list, 'Step 4.5: verify the default tooltip values', mouse_duration=2, x_offset=-5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product, Category', 'Step 4.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()