'''
Created on Jul 14, 2017
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318035
TestCase Name = Verify Pareto Chart in others tab under Format menu.
'''
import unittest
import time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea, active_miscelaneous, ia_ribbon
from common.lib import utillity
from common.locators.ia_ribbon_locators import IaRibbonLocators
from selenium.webdriver.support.color import Color

class C2318035_TestClass(BaseTestCase):

    def test_C2318035(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2318035"
        
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
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 2b: Verify Y-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 2b: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2c: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 2d: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue', 'Step 2e(i): Verify any riser Color')  
         
        """    3. Click the Run button.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 03a: Verify X-Axis Title")
        #result_obj.verify_riser_legends("MAINTABLE_wbody0", ['Unit Sales', 'Dollar Sales'], "Step 3b: Verify riser legends")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 03b: Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 03d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'bar_blue', 'Step 03e: Verify first series bar Color')
        expected_tooltip_list=['Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g6!mbar!', expected_tooltip_list, 'Step 3f: verify the default tooltip values', mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product', 'Step 03g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5) 
        
        """    4. Select Format > Other. From Select a chart pop up choose Radar Area Chart . Click OK.    """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('special', 'pareto', 3, ok_btn_click=True)
        time.sleep(8)
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 4a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 4b: Verify Y-Axis Title")
        expected_xval_list=['Espresso','Capuccino']
        expected_yval_list=['0', '96.6K', '193.1K', '289.7K', '386.2K', '482.8K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4c(i): ')
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4c(ii): ', y_custom_css="text[class^='y2axis-labels']")
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue', 'Step 4d(i): Verify any riser Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mline!', 'bar_green', 'Step 4d(ii): Verify pareto line Color', attribute_type='stroke') 
        
        """    5. Click the Run button.    """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 svg g.groupPanel g rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product", "Step 05a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","Unit Sales", "Step 05b: Verify Y-Axis Title")
        expected_xval_list=['Latte', 'Croissant', 'Biscotti', 'Mug', 'Scone', 'Espresso', 'Coffee Pot', 'Thermos', 'Capuccino', 'Coffee Grinder']
        expected_yval_list=['0', '0.7M', '1.5M', '2.2M', '3M', '3.7M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05c(i): ')
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05c(ii): ', y_custom_css="text[class^='y2axis-labels']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'bar_blue', 'Step 05d: Verify first series bar Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product', 'Step 05e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 05f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=5) 
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)         
        
if __name__ == '__main__':
    unittest.main()