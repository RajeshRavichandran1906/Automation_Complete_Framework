'''
Created on Jul 25, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318012
TestCase Name = Verify Horizontal Absolute Line Chart in others tab under Format menu.
'''

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon, ia_ribbon, ia_resultarea
from common.lib import utillity


class C2318012_TestClass(BaseTestCase):

    def test_C2318012(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2318012'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Right click on folder created in IA.
        Select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
          
        """
        Step 02: Add fields Product, Unit Sales, Dollar Sales.
        """
        time.sleep(4)
        metadataobj.datatree_field_click("Product",2,1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
          
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
          
        metadataobj.datatree_field_click("Dollar Sales", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 4)
        xaxis_value="Product"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_legend_list, 'Step 02: Verify Legend Title')
          
        """
        Step 03: Click the Run button.
        Expect to see the following Bar Chart.
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        css="#MAINTABLE_wbody0 .chartPanel"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 20)
        xaxis_value="Product"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0','2M','4M','6M','8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 3.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03.3: Verify bar color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 03.4: Verify Legend Title')
        time.sleep(5)
        expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 03.5: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Product', 'Step 03.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(5)
          
        """
        Step 04: Select Format > Other.
        From Select a chart pop up choose
        Horizontal Absolute Line Chart.
        Click OK.
        Expect to see the Clustered bar chart converted into the Preview pane for Horizontal Absolute Line Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5)
        ia_ribbobj.select_other_chart_type('line', 'horizontal_absolute_line', 8, ok_btn_click=True)
        time.sleep(4)
        parent_css="#pfjTableChart_1 path[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        expected_title='Product'
        result_obj.verify_xaxis_title('pfjTableChart_1', expected_title, 'Step 04.1: Verify X-axis title')
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xval_list, expected_yval_list, 'Step 04.2: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1', 2, 'Step 04.3: Verify Number of lines', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 04.4: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s1!g0!mline!", "bar_green", "Step 04.5: Verify line2 color",attribute_type='stroke')
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('pfjTableChart_1', expected_legend_list, 'Step 04.6: Verify Legend Title')
        time.sleep(5) 
        
        """
        Step 05: Click the Run button.
        Expect to see the following Horizontal Absolute Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        css="#MAINTABLE_wbody0 .chartPanel"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody0 path[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        expected_title='Product'
        result_obj.verify_xaxis_title('MAINTABLE_wbody0', expected_title, 'Step 05.1: Verify X-axis title')
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0','2M','4M','6M','8M','10M','12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 05.4: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 05.5: Verify line2 color",attribute_type='stroke')
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 05.6: Verify Legend Title')
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s1!g9!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            time.sleep(3)
        else:
            time.sleep(1)
        expected_tooltip_list=['Product:  Thermos', 'Dollar Sales:  2385829', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mline!', expected_tooltip_list, 'Step 05.7: verify the default tooltip values', default_move=True)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Product', 'Step 05.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2318012_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()