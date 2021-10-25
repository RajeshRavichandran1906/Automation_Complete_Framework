'''
Created on Jan 30, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358893
TestCase Name = Insert Text, Image, Chart, Report, and Existing report in a compound report
'''

import unittest, time, keyboard
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, active_miscelaneous,\
    ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

class C2358893_TestClass(BaseTestCase):

    def test_C2358893(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2358893'
        fex_id = 'AR_AHTML_001'
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_styleobj = ia_styling.IA_Style(driver)
        
        """
        Step 01: Upload at_ahtml_001.fex in content folder.
        Step 02: Now create New> Document via IA tool.
        Select 'GGSales' as master file, and make sure format of the report is Active report.
        Select Category, Product, Unit Sales to get a report
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 25)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 02: Verify output format as Active report.")
        
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
            
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
        
        coln_list = ["Category", "Product", "Unit Sales"]
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 1.1: Verify report1 titles")
        
        """ 
        Step 03: Choose 'Chart' from 'Insert' tab
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
        
        """ 
        Step 04: Now add PRODUCT ID and Dollar Sales to get a graph
        """
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        parent_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 25)
         
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        parent_css="#TableChart_2 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 25)
        
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 34, 250,  target_drop_point='bottom_middle')
        time.sleep(5)
        
        xaxis_value="Product ID"
        vis_resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 2.2:a(i) Verify X-Axis Title")
        yaxis_value="Dollar Sales"
        vis_resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 2.2:a(ii) Verify y-Axis Title")
        expected_xval_list=['C141', 'C144']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step 2.2:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 2.2.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step 2.2.c: Verify first bar color")
        time.sleep(5)
        
        """ 
        Step 05: Select 'Existing Report' - 'AR-AHTML-001' from 'insert' tab and click open button.
        """
        vis_ribbon.select_ribbon_item('Insert', 'existing_report')
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK div", 'Open', 25)
        utillobj.ibfs_save_as(fex_id)
        utillobj.synchronize_with_number_of_element("#IncludeTable_1", 1, 15)
        
        ia_resultobj.drag_drop_document_component('#IncludeTable_1', '#TableChart_2', 250, 0)
        time.sleep(5)
        
        coln_list = ['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        vis_resultobj.verify_report_titles_on_preview(6, 6, "IncludeTable_1 ", coln_list, "Step 05.1: Verify report2 titles")
        
        """ 
        Step 06: Choose 'Text Box' from 'Insert' tab, and type "Chart, Report and Images are tested in this case". Adjust the text box accordingly. Make text Bold and change the color to red and click ok.
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        time.sleep(2)
        vis_ribbon.resizing_document_component('0.5', '4')
        time.sleep(3)
        ia_resultobj.enter_text_in_Textbox('Text_1', "Chart, Report and Images are tested in this case")
        
        parent_css = driver.find_element_by_css_selector("#Text_1")
        utillobj.click_on_screen(parent_css, coordinate_type='middle', click_type=0)
        time.sleep(1)
        keyboard.send('ctrl+a')
        time.sleep(1)
        font_bold_css = driver.find_element_by_css_selector("#palTxtOptions div[class*='bi-button-label'] img[src*='font_bold']")
        utillobj.click_on_screen(font_bold_css, coordinate_type='middle', click_type=0)
        time.sleep(1)
        font_color_css = driver.find_element_by_css_selector("#palTxtOptions div[class*='bi-button-label'] img[src*='font_color']")
        utillobj.click_on_screen(font_color_css, coordinate_type='middle', click_type=0)
        time.sleep(3)
        ok_btn_css="div[id^='BiColorPicker'] div[class*='window-active'] #BiColorPickerOkBtn"
        utillobj.synchronize_with_number_of_element(ok_btn_css, 1, 25)
        ia_styleobj.set_color('red')
        parent_css = driver.find_element_by_css_selector("#Text_1")
        utillobj.click_on_screen(parent_css, coordinate_type='middle', click_type=0)
        
        ia_resultobj.drag_drop_document_component('#Text_1', '#TableChart_1', 250, 0)
        time.sleep(5)
        
        frameid="[id*='BiRichEdit']"
        utillobj.switch_to_frame(pause=3, frame_css=frameid)
        expected_text_color=utillobj.color_picker('red', 'rgba')
        text_css = driver.find_element_by_css_selector("div[style*='text'] span[style*='color']")
        actual_text_color=Color.from_string(text_css.value_of_css_property("color")).rgba
        utillobj.asequal(actual_text_color, expected_text_color , "Step 06: Verification of text color in text box.")
        utillobj.switch_to_default_content(pause=1)
        
        """ 
        Step 07: Choose 'Image' from 'Insert' tab, and choose a image(ex-SMPLOGO1)
        Step 08: Click Ok.
        Step 09: Now arrange the chart, report, text and Image, So it wont collide each other.
        """
        vis_ribbon.select_ribbon_item('Insert', 'image')
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK div", 'Open', 1)
        utillobj.ibfs_save_as('smplogo1')
        utillobj.synchronize_with_number_of_element("#PageItemImage_1 img[src*='config']", 1, 15)
        ia_resultobj.drag_drop_document_component('#PageItemImage_1', '#Text_1', 80, 0)
        
        """ 
        Step 10: Now run the document.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=3)
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 25)
        utillobj.mouse_scroll('down', 1, option='uiautomation')
        time.sleep(3)
        
        miscelaneousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 10.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx', " Step 10.2: Verify report at run time.", desired_no_of_rows=5)
        
        miscelaneousobj.verify_page_summary(2, '107of107records,Page1of2', "Step 10.3: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData2', 'I2r', test_case_id + '_Ds02.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData2', 'I2r', test_case_id + '_Ds02.xlsx', " Step 10.4: Verify report at run time.", desired_no_of_rows=10)
        
        expected_text = 'Chart, Report and Images are tested in this case'
        elem_css = driver.find_elements_by_css_selector("[id*='LOBJText'] span")
        actual_text = elem_css[1].text.strip()
        utillobj.asequal(actual_text, expected_text,  "Step 10.5(i): Verify text in textbox")
        
        utillobj.verify_element_color_using_css_property("[id*='LOBJText'] span[style*='color']", 'red', "Step 10.5(ii): Verify text color in textbox", attribute = 'color')
        
        img_displayed=driver.find_element_by_css_selector("#orgdivouter0 #allLayoutObjects #EMBEDIMG0 img[src^='data']").is_displayed()
        utillobj.asequal(True, img_displayed, 'Step 10.6: Verify expected image appears on the document canvas')

        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 25)
        xaxis_value="Product ID"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        yaxis_value="Dollar Sales"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify y-Axis Title")
        expected_xval_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody1","Dollar Sales BY Product ID", "Step 10.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 10.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 10.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 10.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Product ID:C141', 'Dollar Sales:3906243', 'Filter Chart', 'Exclude from Chart']
        vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 10.i: verify the default tooltip values')
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,test_case_id+'_Actual_Step10')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=1)
        vis_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(test_case_id)
        time.sleep(3)
    

if __name__ == '__main__':
    unittest.main()        