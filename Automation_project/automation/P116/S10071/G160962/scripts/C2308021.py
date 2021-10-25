'''
Created on Jan 22, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2308021
TestCase Name = AHTML:Document:Applying style color to the chart is not reflected during run time (ACT-630)
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, active_miscelaneous, visualization_resultarea, ia_styling
from common.lib.basetestcase import BaseTestCase

class C2308021_TestClass(BaseTestCase):

    def test_C2308021(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2308021'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)

        """ 
        Step 01: Launch IA to develop a new Document.
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 60)
        
        """ 
        Step 02: Select 'GGSales' as master file, and change output format as Active report.
        Select Product and Unit Slaes fields to create one report
        """
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 2: Verify output format as Active report.")
        
        """ 
        Step 03: Choose 'Chart' from 'Insert' tab, then add fields eg: Product and Dollar Sales to get a chart.
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
        vis_metadata.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 25)
         
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 25)
        
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step03:a(i) Verify X-Axis Title")
        yaxis_value="Dollar Sales"
        vis_resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step03:a(ii) Verify y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step03:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c: Verify first bar color")
        time.sleep(5)
        
        """ 
        Step 04: Right click the chart in live preview and select More Style options
        """
        parent_elem=driver.find_element_by_css_selector("#TableChart_1 rect[class='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(parent_elem, 'middle')
        utillobj.click_on_screen(parent_elem, 'middle', click_type=0)
        time.sleep(1)
        utillobj.click_on_screen(parent_elem, 'bottom_middle', click_type=1, y_offset=-10)
        time.sleep(2)
        utillobj.default_click(parent_elem, click_option=1)
        time.sleep(3)
        popup_css = "div[id^='BiPopup'][style*='inherit']"
        utillobj.synchronize_with_number_of_element(popup_css, 1, 30)
        utillobj.select_or_verify_bipop_menu('More Style Options...')
        
        """ 
        Step 05: Select Solid Fill and change the color option eg: Red Color 
        """
        parent_css="[id^='QbDialog'] [class*='active'] div[id*='seriesGradientSplitPane']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
        utillobj.verify_object_visible(parent_css, True, "Step 05: Format series window is displayed.")
        
        solidfill_radiobutton = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] div[id*='colorFillRadioBtn'] input[type^='radio']")
        a=solidfill_radiobutton.get_property("checked")
        print(a)
        if a != True:
            solidfill_radiobutton.click()
        else:
            print("Step 05: Solid Fill radio button is checked by default.")
        time.sleep(3)
        
        color_css = driver.find_element_by_css_selector("#seriesGradientSplitPane #seriesFillColorBtn img")
        utillobj.click_on_screen(color_css, 'middle', click_type=0)
        
        time.sleep(3)
        ok_btn_css="div[id^='IAColorPicker'] div[class*='window-active'] #BiColorPickerOkBtn"
        utillobj.synchronize_with_number_of_element(ok_btn_css, 1, 25)
        ia_stylingobj.set_color('red')
        
        """ 
        Step 06: Click apply button and check the changes reflected in live preview and execute the report.
        """
        time.sleep(3)
        apply_btn = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='seriesGradientApplyBtn']")
        utillobj.click_on_screen(apply_btn, 'middle', click_type=0)
        time.sleep(3)
        apply_btn = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='seriesGradientOkBtn']")
        utillobj.click_on_screen(apply_btn, 'middle', click_type=0)
        
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 06:a(i) Verify X-Axis Title")
        yaxis_value="Dollar Sales"
        vis_resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 06:a(ii) Verify y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 06:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 06.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "red", "Step 06.c: Verify first bar color")
        time.sleep(5)
        
        """
        Step 07: Verify the changed color is reflected during run time
        """
        time.sleep(5)
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 25)
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step07:a(i) Verify X-Axis Title")
        yaxis_value="Dollar Sales"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step07:a(ii) Verify y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "red", "Step 07.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","Dollar Sales BY Product", "Step 07.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step07.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         expected_tooltip_list=['Product:Biscotti', 'Dollar Sales:5263317', 'Filter Chart', 'Exclude from Chart']
#         vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 07.i: verify the default tooltip values')
        
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        vis_ribbon.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()