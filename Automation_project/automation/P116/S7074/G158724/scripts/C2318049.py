'''
Created on Jul 17, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318049
TestCase Name = Verify Treemap Chart in others tab under Format menu.
'''

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon, ia_ribbon, ia_resultarea
from common.lib import utillity


class C2318049_TestClass(BaseTestCase):

    def test_C2318049(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2318049'
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
        time.sleep(6)
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        
        """
        Step 02: Add fields Category, Product, Unit Sales.
        """
        time.sleep(4)
        metadataobj.datatree_field_click("Category",2,1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        
        metadataobj.datatree_field_click("Product", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 8)
        xaxis_value="Category : Product"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso']
        expected_yval_list=['0','50K','100K','150K','200K','250K','300K','350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar color")
        
        """
        Step 03: Click the Run button.
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        css="#MAINTABLE_wbody0 .chartPanel"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 10)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 10)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 6)
        xaxis_value="Category : Product"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee : Capuccino','Coffee : Espresso','Coffee : Latte','Food : Biscotti','Food : Croissant','Food : Scone','Gifts : Coffee Grinder','Gifts : Coffee Pot','Gifts : Mug','Gifts : Thermos']
        expected_yval_list=['0','200K','400K','600K','800K','1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.1: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 3.2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 03.3: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 03.5: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 03.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(5)
        
        """
        Step 04: Select Format > Other >HTML5
        and choose Treemap Chart.
        Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5)
        ia_ribbobj.select_other_chart_type('html5', 'tree_map', 5, ok_btn_click=True)
        time.sleep(4)
        parent_css="#pfjTableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css="#pfjTableChart_1 svg g text[class*='dataLabels']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css= "#pfjTableChart_1 svg g rect[class*='group-header']"
        result_obj.wait_for_property(parent_css, 1)
        expected_datalabel=['Coffee','Espresso', 'Capuccino']
        result_obj.verify_data_labels("pfjTableChart_1", expected_datalabel, 'Step 04: Verify riser datalabels', custom_css="> svg > g > g > g > text")
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1', 2, 'Step 04: Verify Number of riser', custom_css="rect[class^='riser']")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!sCoffee-_-Espresso!g0!mnode", "bar_blue1", "Step 04: Verify 1st bar color")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!sCoffee-_-Capuccino!g0!mnode", "bar_blue1", "Step 04: Verify 2nd bar color")
        time.sleep(5)
        
        """
        Step 05: Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        css="#MAINTABLE_wbody0 .chartPanel"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 10)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='dataLabels']"
        result_obj.wait_for_property(parent_css, 10)
        parent_css= "#MAINTABLE_wbody0 svg g rect[class*='group-header']"
        result_obj.wait_for_property(parent_css, 3)
        expected_datalabel=['Food', 'Coffee', 'Gifts', 'Croissant', 'Biscotti', 'Scone', 'Latte', 'Espresso', 'Capuccino', 'Mug', 'Coffee Pot', 'Thermos', 'Coffee Grinder']
        result_obj.verify_data_labels("MAINTABLE_wbody0_f", expected_datalabel, 'Step 05: Verify riser datalabels', custom_css="> svg > g > g > g > text")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 05: Verify Number of riser', custom_css="rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!sFood-_-Croissant!g0!mnode", "bar_blue", "Step 05: Verify 1st bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!sCoffee-_-Latte!g0!mnode", "pale_green", "Step 05: Verify 2nd bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!sGifts-_-Mug!g0!mnode", "dark_green", "Step 05: Verify 3rd bar color")
        time.sleep(5)
        expected_tooltip_list=['Category:Food', 'Product:Croissant', 'Unit Sales:630054', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!sFood-_-Croissant!g0!mnode', expected_tooltip_list, 'Step 05: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2318049_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()