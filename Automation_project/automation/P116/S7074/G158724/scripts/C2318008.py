'''
Created on JUL 17, 2017
Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2318008
TestCase Name = Verify Horizontal Percent Bars in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon
from common.lib import utillity


class C2318008_TestClass(BaseTestCase):

    def test_C2318008(self):
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        result_obj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2318008"
        
        """    01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
        
        """    02: Add fields Product, Unit Sales, Dollar Sales.        """
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend g text[class='legend-labels!s0!']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        parent_css="#TableChart_1 g.legend g text[class='legend-labels!s1!']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
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
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 20)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 03a: Verify X-Axis Title")
        result_obj.verify_riser_legends("MAINTABLE_wbody0", ['Unit Sales', 'Dollar Sales'], "Step 3b: Verify riser legends")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 03d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'bar_blue', 'Step 03e(i): Verify first series bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g8!mbar!", 'pale_green', 'Step 03e(ii): Verify second series bar Color')
        expected_tooltip_list=['Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g6!mbar!', expected_tooltip_list, 'Step 3f(i): verify the default tooltip values for first series', mouse_duration=2.5)
        expected_tooltip_list=['Product:Capuccino', 'Dollar Sales:2381590', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g1!mbar!', expected_tooltip_list, 'Step 3f(ii): verify the default tooltip values for second series', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5)  
        
        """    04 : Select Format > Other, From Select a chart pop up choose 'Horizontal Percent Bars', Click OK    """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('bar', 'horizontal_percent_bars', 20, ok_btn_click=True)
        time.sleep(8)   
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 4a: Verify X-Axis Title")
        result_obj.verify_riser_legends("TableChart_1", ['Unit Sales', 'Dollar Sales'], "Step 4b: Verify riser legends")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4c: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 4d: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 4e(i): Verify first series first riser Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g1!mbar!', 'bar_green', 'Step 4e(ii): Verify second series second riser Color')
        
        """    05 : Click the Run button.       """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 20)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 05a: Verify X-Axis Title")
        result_obj.verify_riser_legends("MAINTABLE_wbody0", ['Unit Sales', 'Dollar Sales'], "Step 05b: Verify riser legends")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 05d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'bar_blue', 'Step 05e(i): Verify first series bar Color')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g8!mbar!", 'pale_green', 'Step 05e(ii): Verify second series bar Color')
        expected_tooltip_list=['Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g6!mbar!', expected_tooltip_list, 'Step 35(i): verify the default tooltip values for first series', mouse_duration=2.5)
        expected_tooltip_list=['Product:Capuccino', 'Dollar Sales:2381590', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g1!mbar!', expected_tooltip_list, 'Step 35(ii): verify the default tooltip values for second series', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 05g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID) 
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        