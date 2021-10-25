'''
Created on Jun 30, 2017

@author: Magesh
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204910_TestClass(BaseTestCase):

    def test_C2204910(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204910'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Right click on folder created in IA and select New > Chart using the GGSALES file.
        On the Format tab, in the Output Types group, click Active Report/Active PDF.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        
        """
        Step 02: Add fields Product and Dollar Sales.
        """
        time.sleep(4)
        metadataobj.datatree_field_click("Product",2,1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        
        metadataobj.datatree_field_click("Dollar Sales", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 2)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 9)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Product"
        yaxis_value="Dollar Sales"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar color")
        
        """
        Step 03: Right click on Bar in design area, and select Sort > Sort > Ascending, Then Run the report
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        time.sleep(3)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Ascending')
        time.sleep(4)
        
        """
        Step 04: Click the Run button.
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
        result_obj.wait_for_property(parent_css, 10)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 10)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Product"
        yaxis_value="Dollar Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 04:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Coffee Grinder','Capuccino','Thermos','Coffee Pot','Espresso','Scone','Mug','Biscotti','Croissant','Latte']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 4: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", 'bar_blue', 'Step 04: Verify Color')
        time.sleep(5)
        expected_tooltip_list=['Product:Coffee Grinder', 'Dollar Sales:2337567', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 4: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204910_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        
if __name__ == '__main__':
    unittest.main()