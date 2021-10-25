'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358891
'''
import unittest
import time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous, ia_styling
from common.lib import utillity
import keyboard as local_keyboard
from selenium.webdriver.support.color import Color

class C2358891_TestClass(BaseTestCase):

    def test_C2358891(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358891'
        expected_series_left_tab_list=['Fill', 'Border', 'Effect']        
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_styling_obj=ia_styling.IA_Style(driver)
        
        """    1. Launch IA to develop a Document.
        Select 'GGSales' as master file, and change output format as Active report
        Choose 'Chart' from 'Insert' tab, then add Product and DollarSales to get a graph    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=35, string_value='Document')
        ribbonobj.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 svg g text[class*='xaxisOrdinal-title']", "Product", 10)    
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 svg g text[class*='yaxis-title']", "Dollar Sales", 10)
        
        """    2. Now right click the chart in live preview and select More Style option    """
        oChart_component=driver.find_element_by_css_selector("#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        utillobj.default_click(oChart_component, click_option=1)
        oChart_component=driver.find_element_by_css_selector("#TableChart_1 rect[class^='riser!s0!g1!mbar']")
        utillobj.default_click(oChart_component, click_option=0)
        utillobj.default_click(oChart_component, click_option=1)
        utillobj.select_or_verify_bipop_menu('More Style Options...')
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    3. Format Series dialog box apperas. Fill tab option is selected by default.    """
        oNoFill=driver.find_element_by_css_selector("#seriesGradientSplitPane #fillPaneBtn[class*='checked']")
        utillobj.click_on_screen(oNoFill, "middle", click_type=0,pause=0.50) 
        oSeriesLeftTabs=driver.find_elements_by_css_selector("#seriesGradientSplitPane #frameLeftContainer>div")
        actual_series_left_tab_list=[el.text.strip() for el in oSeriesLeftTabs if bool(re.match('\S+', el.text.strip()))]
        utillobj.asequal(actual_series_left_tab_list, expected_series_left_tab_list, "Step 03a: Verify that Fill/Border/Effect tab option available.")
        
        """    4. Select no Fill radio button and click apply button. Execute the report    """
        oNoFill=driver.find_element_by_css_selector("#noFillRadioBtn>input")
        utillobj.click_on_screen(oNoFill, "middle", click_type=0,pause=0.50) 
        oFillColorBtn=driver.find_element_by_css_selector("#seriesFillColorBtn")
        utillobj.verify_element_visiblty(oFillColorBtn, visible=False, msg="Step 04a: Verify that Color icon option not available")
        oOkBtn=driver.find_element_by_css_selector("#seriesGradientOkBtn")
        utillobj.click_on_screen(oOkBtn, "middle", click_type=0,pause=0.50)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        time.sleep(2)
        miscobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 04b: Verify Chart toolbar")
        x_val_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        y_val_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, "Step 04b:")
        expected_tooltip=['Product:  Latte', 'Dollar Sales:  10943622', 'Filter Chart', 'Exclude from Chart']
        miscobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g6!mbar', expected_tooltip, "Step 04d: verify the chart tooltip")
        xaxis_value="Product"
        yaxis_value="Dollar Sales"
        resultobj.verify_xaxis_title("MAINTABLE_0", xaxis_value, "Step 04e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_0", yaxis_value, "Step 04e(ii): Verify Y-Axis Title")
        actual_color = driver.find_element_by_css_selector("#MAINTABLE_0 [class*='riser!s0!g1!mbar!']").get_attribute('fill')
        utillobj.asequal(actual_color, 'transparent', "Step 04f: Verify bar color transparent")
        #utillobj.verify_chart_color("MAINTABLE_0", "riser!s0!g0!mbar!", "transparent", "Step 04f: Verify bar color transparent", attribute='yes')
        miscobj.verify_chart_title("MAINTABLE_wbody0_ft","Dollar Sales by Product", "Step 04g: Verify chart title ")       
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04_', image_type='actual',x=0, y=20, w=-250, h=-120)
        time.sleep(1)
        
        """    5. Close the output window and again click on the chart bar select the More Style option    """
        resultobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        oChart_component=driver.find_element_by_css_selector("#TableChart_1 rect[class^='riser!s0!g1!mbar']")
        utillobj.default_click(oChart_component, click_option=0)
        utillobj.default_click(oChart_component, click_option=1)
        utillobj.select_or_verify_bipop_menu('More Style Options...')
        parent_css="div[id^='QbDialog'] [class*='active window'] [class*='caption']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    6. Select the Solid Fill and change the color option to Purple transparency set to 20% , Click apply button and execute the report.    """
        oColorFill=driver.find_element_by_css_selector("#colorFillRadioBtn>input")
        utillobj.click_on_screen(oColorFill, "middle", click_type=0,pause=0.50) 
        oAddColor=driver.find_element_by_css_selector("#seriesFillColorBtn")
        utillobj.click_on_screen(oAddColor, "middle", click_type=0,pause=0.50)
        ia_styling_obj.set_color('purple')
        oColorOKBtn=driver.find_element_by_css_selector("#BiColorPickerOkBtn")
        utillobj.click_on_screen(oColorOKBtn, "middle", click_type=0,pause=0.50) 
        oTransparnecy = self.driver.find_element_by_css_selector("#seriesTransparencySpinner input")
        utillobj.click_on_screen(oTransparnecy, 'left', click_type=0, x_offset=5)
        time.sleep(1)
        local_keyboard.press('ctrl')
        local_keyboard.press('a')
        local_keyboard.release('a')
        local_keyboard.release('ctrl')
        local_keyboard.send('del')
        local_keyboard.write('20', delay=0.5)
        time.sleep(1)
        local_keyboard.send('enter')
        time.sleep(1)
        oOkBtn=driver.find_element_by_css_selector("#seriesGradientOkBtn")
        utillobj.click_on_screen(oOkBtn, "middle", click_type=0,pause=0.50)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        time.sleep(2)
        miscobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 06a: Verify Chart toolbar")
        x_val_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        y_val_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, "Step 06b:")
        expected_tooltip=['Product:  Latte', 'Dollar Sales:  10943622', 'Filter Chart', 'Exclude from Chart']
        miscobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g6!mbar', expected_tooltip, "Step 06c: verify the chart tooltip")
        xaxis_value="Product"
        yaxis_value="Dollar Sales"
        resultobj.verify_xaxis_title("MAINTABLE_0", xaxis_value, "Step 06d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_0", yaxis_value, "Step 06d(ii): Verify Y-Axis Title")
        actual_color = Color.from_string(self.driver.find_element_by_css_selector("#MAINTABLE_0 [class*='riser!s0!g1!mbar!']").get_attribute('fill')).rgba
        utillobj.asequal(actual_color, 'rgba(128, 0, 128, 0.8)', "Step 04f: Verify bar color transparent")
        #utillobj.verify_chart_color("MAINTABLE_0", "riser!s0!g0!mbar!", "purple", "Step 06e: Verify bar color Purple", attribute='yes')
        miscobj.verify_chart_title("MAINTABLE_wbody0_ft","Dollar Sales by Product", "Step 06f : Verify chart title ")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step06_', image_type='actual',x=0, y=20, w=-250, h=-120)
        time.sleep(1)
        
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()