'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2317338
TestCase Name = Verify that Legend Border displayed in Red color.
'''

import unittest
import time, re
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon, ia_styling
from common.lib import utillity
from selenium.webdriver.support.color import Color


class C2317338_TestClass(BaseTestCase):

    def test_C2317338(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2317338'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        style_obj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Open IA and create a new chart using the GGSALES file.
        Select Active Report as the output type.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        
        """
        Add Category to the Horizontal axis.
        Add Unit Sales to the Vertical axs.
        Add Dollar Sales to the Vertical axs.
        """
        time.sleep(4)
        metadataobj.datatree_field_click("Category",2,1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        
        metadataobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        
        metadataobj.datatree_field_click("Dollar Sales", 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        xaxis_value="Category"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 01a Verify X-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0','1M','2M','3M','4M','5M','6M','7M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01b: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 01c: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01d: Verify bar color")
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_legend_list, 'Step 01e: Verify Legend Title')
        
        
        """
        Step 02: Using the Format tab, select Lables, then select Legend.
        Click Show Legend if not already selected.
        Step 03: Select More Legend Options.
        """
        ribbonobj.switch_ia_tab('Format')
        if driver.find_element_by_css_selector("#FormatChartLegend img").is_displayed()==False:
            elem=utillobj.validate_and_get_webdriver_object("#chartLabels_altButton img", "Legend Button")
            utillobj.default_click(elem)
        ribbonobj.select_ribbon_item('Format', 'legend')
        temp_css="table tr"
        bipopup_css="div[id^='BiPopup'][style*='inherit']"
        bipopups=driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(temp_css)
        time.sleep(2)
        actual_ticked_list=[el.text.strip() for el in menu_items if bool(re.match('.*checked$', el.find_element_by_css_selector("td:nth-child(1)").get_attribute("class")))]
        expected_ticked_list=['Show legend']
        print(actual_ticked_list)
        if expected_ticked_list == actual_ticked_list:
            print("Show Legend is selected in BiPopup.")
            utillobj.select_or_verify_bipop_menu('More Legend Options...',verify='true',expected_ticked_list=['Show legend'],expected_popup_list=['Show legend', 'Legend Position', 'More Legend Options...'],msg='Step 02.0: Verify Legend menu')
        else:
            print("Show Legend is not selected in BiPopup.")
            utillobj.select_or_verify_bipop_menu('Show legend',verify='true',expected_popup_list=['Show legend', 'Legend Position', 'More Legend Options...'],msg='Step 02.0: Verify Legend menu')
            ribbonobj.select_ribbon_item('Format', 'legend', opt='More Legend Options...')
        
        
        """
        Step 04: Click the Border Styles option, then check the Show Border box.
        Click color button, select red.
        Click OK to the color option.
        """
        borderStylesBtn=driver.find_element_by_css_selector("#leftPane div[id^='borderStylesBtn']")
        utillobj.default_left_click(object_locator=borderStylesBtn)
        parent_css="div#borderStylesPane"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(4)
        driver.find_element_by_css_selector("#rightPane #showBorderCheckBox input[id^='BiCheckBox']").click()
        time.sleep(4)
        color_btn=driver.find_element_by_css_selector("#borderStylesPane #borderSwatch img")
        utillobj.default_left_click(object_locator=color_btn)
        time.sleep(2)
        style_obj.set_color("red")
        time.sleep(4)
        
        """
        Step 05: Click OK. Click the Run button,
        """
        ok_btn=driver.find_element_by_css_selector("#legendOkBtn[class*='bi-button button'] div")
        utillobj.default_left_click(object_locator=ok_btn)
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        css="#MAINTABLE_wbody0 .chartPanel"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)

        xaxis_value="Category"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0','4M','8M','12M','16M','20M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05b: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 6, 'Step 05c: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", 'bar_blue', 'Step 05d: Verify Color')
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 05e: Verify Legend Title')
        raiser_css = "#MAINTABLE_wbody0 svg>g[class*='legend-clip'] path[class*='legend-background']"
        legend_color = Color.from_string(driver.find_element_by_css_selector(raiser_css).value_of_css_property("stroke")).rgba
        expected_color=utillobj.color_picker("red", 'rgba')
        utillobj.asequal(legend_color, expected_color, 'Step 05f: Verify Legend border color')
        time.sleep(5)
        expected_tooltip_list=['Category:Food', 'Unit Sales:1384845', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 05g: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category', 'Step 05h: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05i: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05j: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05k: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        
        """
        Step 06: Using the Format tab, select Labels, then select Legend.
        Click Show Legend if not already selected.
        Select More Legend Options.
        Click the Fill option, then Solid Fill and then yellow.
        """
        ribbonobj.select_ribbon_item('Format', 'legend')
        temp_css="table tr"
        bipopup_css="div[id^='BiPopup'][style*='inherit']"
        bipopups=driver.find_elements_by_css_selector(bipopup_css)
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(temp_css)
        time.sleep(2)
        actual_ticked_list=[el.text.strip() for el in menu_items if bool(re.match('.*checked$', el.find_element_by_css_selector("td:nth-child(1)").get_attribute("class")))]
        expected_ticked_list=['Show legend']
        print(actual_ticked_list)
        if expected_ticked_list == actual_ticked_list:
            print("Show Legend is selected in BiPopup.")
            utillobj.select_or_verify_bipop_menu('More Legend Options...',verify='true',expected_ticked_list=['Show legend'],expected_popup_list=['Show legend', 'Legend Position', 'More Legend Options...'],msg='Step 06.0: Verify Legend menu')
        else:
            print("Show Legend is not selected in BiPopup.")
            utillobj.select_or_verify_bipop_menu('Show legend',verify='true',expected_popup_list=['Show legend', 'Legend Position', 'More Legend Options...'],msg='Step 06.0: Verify Legend menu')
            ribbonobj.select_ribbon_item('Format', 'legend', opt='More Legend Options...')
        time.sleep(4)
        css="div[id^='BiComponent'][class*='bi-window active window']"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        time.sleep(2)
        fill_option=driver.find_element_by_css_selector("div[id^='legendFillBtn'][class*='bi-tool-bar-button tool-bar-button']")
        utillobj.default_left_click(object_locator=fill_option)
        time.sleep(2)
        
        css="#fillTypeColor input[type^='radio'][class*='bi-radio-button-input']"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        solid_fill=driver.find_element_by_css_selector("#fillTypeColor input[type^='radio'][class*='bi-radio-button-input']")
        utillobj.default_left_click(object_locator=solid_fill)
        time.sleep(2)
        
        color_btn=driver.find_element_by_css_selector("#fillSwatch img")
        utillobj.default_left_click(object_locator=color_btn)
        time.sleep(2)
        
        style_obj.set_color("yellow")
        time.sleep(4)
        
        ok_btn=driver.find_element_by_css_selector("#legendOkBtn[class*='bi-button button'] div")
        utillobj.default_left_click(object_locator=ok_btn)
        time.sleep(4)
        
        css="#TableChart_1 svg>g[class*='legend-clip'] path[class*='legend-background']"
        elem1=(By.CSS_SELECTOR, css)
        result_obj._validate_page(elem1)
        
        raiser_css = "#TableChart_1 svg>g[class*='legend-clip'] path[class*='legend-background']"
        legend_color = Color.from_string(driver.find_element_by_css_selector(raiser_css).value_of_css_property("fill")).rgba
        expected_color=utillobj.color_picker("yellow", 'rgba')
        utillobj.asequal(legend_color, expected_color, 'Step 06a: Verify Legend Background color')
        legend_border_color = Color.from_string(driver.find_element_by_css_selector(raiser_css).value_of_css_property("stroke")).rgba
        expected_color=utillobj.color_picker("red", 'rgba')
        utillobj.asequal(legend_border_color, expected_color, 'Step 06b: Verify Legend Border color')
        time.sleep(5)
        
        """
        Step 07: Click OK. Click the Run button,
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
        result_obj.wait_for_property(parent_css, 6)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        result_obj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        result_obj.wait_for_property(parent_css, 6)
        xaxis_value="Category"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        expected_xval_list=['Coffee','Food','Gifts']
        expected_yval_list=['0','4M','8M','12M','16M','20M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 07b: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 6, 'Step 07c: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", 'bar_blue', 'Step 07d: Verify Color')
        expected_legend_list=['Unit Sales','Dollar Sales']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 07e: Verify Legend Title')
        raiser_css = "#MAINTABLE_wbody0 svg>g[class*='legend-clip'] path[class*='legend-background']"
        legend_background_color = Color.from_string(driver.find_element_by_css_selector(raiser_css).value_of_css_property("fill")).rgba
        expected_background_color=utillobj.color_picker("yellow", 'rgba')
        utillobj.asequal(legend_background_color, expected_background_color, 'Step 07f(i): Verify Legend background color')
        legend_border_color = Color.from_string(driver.find_element_by_css_selector(raiser_css).value_of_css_property("stroke")).rgba
        expected_border_color=utillobj.color_picker("red", 'rgba')
        utillobj.asequal(legend_border_color, expected_border_color, 'Step 07f(ii): Verify Legend Border color')
        time.sleep(5)
        expected_tooltip_list=['Category:Food', 'Unit Sales:1384845', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', expected_tooltip_list, 'Step 07g: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category', 'Step 07h: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07i: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07j: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07k: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2317338_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()