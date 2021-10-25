'''
Created on Jul 3, 2017

@author: Magesh
'''

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204912_TestClass(BaseTestCase):

    def test_C2204912(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204912'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Open IA and create a new Chart using the GGSALES file.
        Select Active Report as the output type.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        
        """
        Add fields Category and State to the Horizontal axis
        Add field Unit Sales to the Vertical axis.
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
        metadataobj.datatree_field_click("State", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 11)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 11)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 11)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 11)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 6)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category : State"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Coffee : CA','Coffee : CT','Coffee : FL','Coffee : GA','Coffee : IL','Coffee : MA','Coffee : MO','Coffee : NY','Coffee : TN','Coffee : TX','Coffee : WA']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02: Verify bar color")
        
        """
        Step 02: Click the Run button.
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
        result_obj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 33)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 8)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category : State"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Coffee : CA','Coffee : CT','Coffee : FL','Coffee : GA','Coffee : IL','Coffee : MA','Coffee : MO','Coffee : NY','Coffee : TN','Coffee : TX','Coffee : WA']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 2: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 33, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 02: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['Category:Coffee', 'State:CA', 'Unit Sales:235583', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 02: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, State', 'Step 02: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        
        """
        Step 03: Right click on Bar in design area and select Sort > Limit > 5.
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        time.sleep(3)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Limit')
        utillobj.select_or_verify_bipop_menu('5')
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 5)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 9)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category : State"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Coffee : IL','Coffee : MO','Coffee : CT','Coffee : MA','Coffee : TX']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 5, 'Step 3: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03: Verify bar color")
        
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
        result_obj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 5)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category : State"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 04:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Gifts : NY','Gifts : TN','Gifts : MO','Gifts : CT','Gifts : MA']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 4: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 04: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['Category:Gifts', 'State:NY', 'Unit Sales:70194', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 04: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, State', 'Step 04: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        result_obj.select_panel_caption_btn(0, select_type='close', custom_css="div[id^='QbReportWindow']")
        
        """
        Step 05: Right click on Bar in design area and select Sort > Limit > 15. 
        """
        raiser_css="#TableChart_1 [class*='riser!s0!g0!mbar!']"
        obj_locator=driver.find_element_by_css_selector(raiser_css)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=0)
        time.sleep(3)
        utillobj.click_on_screen(obj_locator, 'middle', click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Limit')
        utillobj.select_or_verify_bipop_menu('15')
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 11)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 11)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 6)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category : State"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Coffee : IL','Coffee : MO','Coffee : CT','Coffee : MA','Coffee : TX','Coffee : NY','Coffee : FL','Coffee : TN','Coffee : WA','Coffee : GA','Coffee : CA']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 11, 'Step 05: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 05: Verify bar color")
        
        """
        Step 06: Click the Run button.
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
        result_obj.wait_for_property(parent_css, 15)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 15)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 5)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category : State"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 06:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Gifts : NY','Gifts : TN','Gifts : MO','Gifts : CT','Gifts : MA','Gifts : TX','Gifts : IL','Gifts : FL','Gifts : WA','Gifts : GA','Food : TX','Coffee : TN','Coffee : CT','Coffee : IL','Coffee : MA']
        expected_yval_list=['0', '30K', '60K', '90K', '120K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 15, 'Step 06: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 06: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['Category:Gifts', 'State:NY', 'Unit Sales:70194', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 06: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, State', 'Step 06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204912_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
if __name__ == '__main__':
    unittest.main()