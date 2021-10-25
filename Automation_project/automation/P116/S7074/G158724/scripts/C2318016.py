'''
Created on Jul 14, 2017
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318016
TestCase Name = Verify Radar Area Chart in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_ribbon
from common.lib import utillity
from selenium.webdriver.support.color import Color

class C2318016_TestClass(BaseTestCase):

    def test_C2318016(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2318016"
        
        """    1. Right click on folder created in IA. Sselect New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.    """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        element_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(element_css, 11, 20)
        
        ribbonobj.change_output_format_type('active_report')
        element_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(element_css, 'ActiveReport', 20)
         
        """    2. Add fields Product, Unit Sales, Dollar Sales.    """
        metadataobj.datatree_field_click('Product', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 20)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 20)
        
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        element_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 20)
        
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 2a: Verify X-Axis Title")
        result_obj.verify_riser_legends("TableChart_1", ['Unit Sales', 'Dollar Sales'], "Step 2b: Verify riser legends")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2c: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 2d: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 2e(i): Verify first series first riser Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g1!mbar!', 'bar_green', 'Step 2e(ii): Verify second series second riser Color')  
         
        """    3. Click the Run button.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        
        element_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 20, 20)
        
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 03a: Verify X-Axis Title")
        result_obj.verify_riser_legends("MAINTABLE_wbody0", ['Unit Sales', 'Dollar Sales'], "Step 3b: Verify riser legends")
        #result_obj.verify_yaxis_title("MAINTABLE_wbody0","Dollar Sales", "Step 03b: Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 03d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'bar_blue', 'Step 03e(i): Verify first series bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g8!mbar!", 'pale_green', 'Step 03e(ii): Verify second series bar Color')
#         expected_tooltip_list=['Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
#         result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g6!mbar!', expected_tooltip_list, 'Step 3f(i): verify the default tooltip values for first series', mouse_duration=2.5)
#         expected_tooltip_list=['Product:Capuccino', 'Dollar Sales:2381590', 'Filter Chart', 'Exclude from Chart']
#         result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g1!mbar!', expected_tooltip_list, 'Step 3f(ii): verify the default tooltip values for second series', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=5) 
        
        """    4. Select Format > Other. From Select a chart pop up choose Radar Area Chart . Click OK.    """
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbonobj.select_other_chart_type('area', 'area_radar', 11, ok_btn_click=True)
        result_obj.verify_riser_legends("TableChart_1", ['Unit Sales', 'Dollar Sales'], "Step 4a: Verify riser legends")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4b: ')
        
        """    5. Click the Run button.    """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        
        result_obj.verify_riser_legends("MAINTABLE_wbody0", ['Unit Sales', 'Dollar Sales'], "Step 5a: Verify riser legends")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 5b: ')
        path_css="#MAINTABLE_0 svg > g.chartPanel > g.groupPanel > g:nth-child(3) > path"
        actual_color = Color.from_string(driver.find_element_by_css_selector(path_css).value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('pale_green', 'rgba')
        utillobj.asequal(actual_color, expected_color, "Step 5c: Verify color in radar")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 5d: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 5e: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5f: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5g: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=5)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)         
        
if __name__ == '__main__':
    unittest.main()