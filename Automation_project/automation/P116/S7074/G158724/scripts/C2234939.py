'''
Created on June 21, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234939
TestCase Name = Verify Vertical & Horizontal Absolute Line in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_ribbon, ia_resultarea
from common.lib import utillity


class C2234939_TestClass(BaseTestCase):

    def test_C2234939(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        Test_Case_ID="C2234939"
        
        
        """ Step 1: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        
        """ Step 2: Select Active Report as Output file format
        """
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 3: Click Format tab and click Other and Select Line chart
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(1)
               
        
        """ Step 4: From Line select a chart pop up choose 'Vertical Absolute Line'. Click OK
        """
        ia_ribbonobj.select_other_chart_type('line', 'vertical_absolute_line', 1, ok_btn_click=True)
        time.sleep(1)
        
        
        """ Step 5: Add fields as follows:
                    Region under Rows,
                    Unit Sales and Dollar Sales under Vertical Axis
                    Product ID under Horizontal Axis.
        """
        metadataobj.datatree_field_click('Region', 1, 1, 'Add To Query', 'Rows')
        parent_css="#TableChart_1 g.chartPanel text[class^='rowHeader-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='Region', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 4)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product ID', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='ProductID', with_regular_exprestion=True)
        result_obj.verify_xaxis_title("TableChart_1", 'Product ID', "Step 5.1: Verify X-Axis Title")
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Region', ['Midwest', 'Northeast', 'Southeast', 'West'], 'Step 5.2: ')
        expected_xval_list=['C141', 'C144']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 5.3: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 5.4 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mline!r1!c0', 'bar_blue1', 'Step 5.5: Verify Color', attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 8, 'Step 5.6: Verify Number of riser', custom_css="path[class^='riser']")
        
        
        """ Step 6: Click Run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product ID', "Step 6.1: Verify X-Axis Title")
        expected_xval_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 6.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 6.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mline!r1!c0', 'bar_blue', 'Step 6.4: Verify Color', attribute_type='stroke')
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g3!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        #expected_tooltip_list=['Region:Midwest', 'Product ID:F101', 'Unit Sales:116127', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 6.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 6.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 6.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 6.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        
        
        """ Step 7: Back in the Others/Line Charts, select Horizontal Absolute Line.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(1)
        ia_ribbonobj.select_other_chart_type('line', 'horizontal_absolute_line', 8, ok_btn_click=True)
        time.sleep(1)
        parent_css="#TableChart_1 g.scrollColAxis g text[class*='yaxis']"
        result_obj.wait_for_property(parent_css, 6)
        result_obj.verify_xaxis_title("TableChart_1", 'Product ID', "Step 7.1: Verify X-Axis Title")
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'RegionProduct ID', ['Midwest', 'Northeast', 'Southeast', 'West'], 'Step 7.2: Verify Row header and Row label')
        expected_xval_list=['C141', 'C141', 'C144', 'C141', 'C144', 'C141', 'C144']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 7.3: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 7.4 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mline!r1!c0', 'bar_blue1', 'Step 7.5: Verify Color', attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 8, 'Step 7.6: Verify Number of riser', custom_css="path[class^='riser']")
        
        
        """ Step 8: Click Run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product ID', "Step 8.1: Verify X-Axis Title")
        expected_xval_list=['C141', 'C142', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121', 'C141', 'C142', 'C144', 'F101', 'F102',
                             'F103', 'G100', 'G104', 'G110', 'G121', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110',
                             'G121', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 8.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 8, 'Step 8.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mline!r1!c0', 'bar_blue', 'Step 8.4: Verify Color', attribute_type='stroke')
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g0!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        #expected_tooltip_list=['Region:Midwest', 'Product ID:C141', 'Dollar Sales:1294947', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 8.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 8.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 8.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 8.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()