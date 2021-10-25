'''
Created on Dec 27, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228168
TestCase Name = Verify Line chart: Gradient Frame, Smooth Line, Data Labels, Format data Label (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2228168_TestClass(BaseTestCase):

    def test_C2228168(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228168'
        Test_Case_saveas_ID ="IA-VAL-CHART-005"
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Launch WF, New > Chart with GGSALES.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P292/S10032_chart_1', 'mrid', 'mrpass')
        time.sleep(5)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
         
        """
        Step 02: Click on "Format tab", expand chart types (if not expanded).
        Step 03: Select Line Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Line')
        time.sleep(3)
         
        """
        Step 04: Click "Features Grouping" icon to expand it.
        Step 05: Click "Frame & Background" icon.
        """
        ribbonobj.select_ribbon_item('Format', 'Frame_Background')
         
        """
        Step 06: Click on Gradient fill radio button.
        """
        parent_css="[id^='QbDialog'] [class*='active'] #frameSplitPane"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)
        utillobj.verify_object_visible(parent_css, True, "Step 06: Frame & Background window is displayed.")
        ia_ribbobj.set_format_frame_and_background('radiobutton', 'gradient_fill', 'uncheck')
         
        """
        Step 07: Click on color picker icon for the First color.
        Step 08: Select (255,0,255) > ok
        """
        time.sleep(3)
        ia_ribbobj.set_format_frame_and_background('styleimage_objects', 'first_color', 'check')
        time.sleep(3)
        ok_btn_css="div[id^='IAColorPicker'] div[class*='window-active'] #BiColorPickerOkBtn"
        resultobj.wait_for_property(ok_btn_css, 1, expire_time=30)
        ia_stylingobj.set_color('magenta')
         
        """
        Step 09: Click on color picker icon for the Second color.
        Step 10: Select (255,255,0), click "OK".
        """
        time.sleep(3)
        ia_ribbobj.set_format_frame_and_background('styleimage_objects', 'second_color', 'check')
        time.sleep(3)
        ok_btn_css="div[id^='IAColorPicker'] div[class*='window-active'] #BiColorPickerOkBtn"
        resultobj.wait_for_property(ok_btn_css, 1, expire_time=30)
        ia_stylingobj.set_color('yellow')
         
        """
        Step 11: Verify it displays the following colors for "Gradient style - Color Pattern".
        """
        time.sleep(3)
        color_pattern_css = "#abSwatchForFrame img[src*='c1=rgb(255%2C0%2C255)&c2=rgb(255%2C255%2C0)']"
        utillobj.verify_object_visible(color_pattern_css, True, "Step 11: Verify it displays the following colors for 'Gradient style - Color Pattern'.")
     
        """
        Step 12: Click "OK".
        """
        ok_btn = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] #frameOkBtn img")
        utillobj.click_on_screen(ok_btn, 'middle')
        utillobj.click_on_screen(ok_btn, 'middle', click_type=0)
         
        """
        Step 13: Double click "Product", "Unit Sales".
        """
        time.sleep(3)
        metaobj.datatree_field_click('Product', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
         
        metaobj.datatree_field_click('Unit Sales', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 text[class^='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
         
        """
        Step 14: Click on "Series" tab.
        Step 15: Click "Data Labels" icon from "Properties Grouping".
        """
        ribbonobj.select_ribbon_item('Series', 'Data_labels')
        time.sleep(5)
         
        """
        Step 16: Verify the following chart is displayed.
        """
        time.sleep(5)
        parent_css="#TableChart_1 text[class^='dataLabels']"
        resultobj.wait_for_property(parent_css, 2)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step16:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        expected_data_labels=['189K', '294K']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, 'Step 16.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 1, 'Step 16.d: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 16.ei: Verify line color", attribute_type='stroke')
        time.sleep(5)
        chartframe_gradient_fill = "url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_2550255_1_1_2552550_1_0_2550255_1)"
        chartframe_css = driver.find_element_by_css_selector("#TableChart_1 rect[class^='chartFrame']")
        actual_gradient_fill = chartframe_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, chartframe_gradient_fill, "Step 16.e: Verify gradient fill is applied to the chart frame & background.")
        
        """
        Step 17: Click "Data Labels" dropdown and select "More Data Labels" options.
        Step 18: Verify "Format Labels" window is displayed.
        """
        ribbonobj.select_ribbon_item('Series', 'Data_labels_menubtn', opt='More Data Label Options')
        time.sleep(5)
        parent_css="[id^='QbDialog'] [class*='active'] #dataLabelSplitPane"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)
        utillobj.verify_object_visible(parent_css, True, "Step 18: Verify the Format Labels window is displayed.")
        
        """
        Step 19: Click "Format Labels" dropdown > "Currency with no decimal" > "OK".
        """
        time.sleep(3)
        formatlabels_css = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='generalBLAformatDataLabelsComboBox'] div[class^='bi-button button']")
        utillobj.click_on_screen(formatlabels_css, 'middle')
        utillobj.click_on_screen(formatlabels_css, 'middle',  click_type=0)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Currency with no decimal', custom_css="div[id*='BiComboBoxItem']")
        time.sleep(3)
        ok_btn_css = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='dataLabelsOkBtn']")
        utillobj.click_on_screen(ok_btn_css, 'middle')
        utillobj.click_on_screen(ok_btn_css, 'middle',  click_type=0)
        
        """
        Step 20: Verify the following chart is displayed.
        """
        time.sleep(5)
        parent_css="#TableChart_1 text[class^='dataLabels']"
        resultobj.wait_for_property(parent_css, 2)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step20:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step20:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        expected_data_labels=['$189,217', '$293,544']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, 'Step 20.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 1, 'Step 20.d: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 20.ei: Verify line color", attribute_type='stroke')
        time.sleep(5)
        chartframe_gradient_fill = "url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_2550255_1_1_2552550_1_0_2550255_1)"
        chartframe_css = driver.find_element_by_css_selector("#TableChart_1 rect[class^='chartFrame']")
        actual_gradient_fill = chartframe_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, chartframe_gradient_fill, "Step 20.e: Verify gradient fill is applied to the chart frame & background.")
        
        """
        Step 21: Click "Smooth Line" icon on "Line Grouping".
        """
        ribbonobj.select_ribbon_item('Series', 'SmoothLine')
        time.sleep(5)
        
        """
        Step 22: Click "Run".
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        
        """
        Step 23: Verify the following chart is displayed in the "Run" window.
        """
        parent_css="#jschart_HOLD_0 text[class^='dataLabels']"
        resultobj.wait_for_property(parent_css, 10)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step23:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step23:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step23:a(iii):Verify XY labels")
        expected_data_labels=['$421,377', '$189,217', '$186,534', '$190,695', '$630,054', '$308,986', '$878,063', '$360,570', '$333,414', '$190,081']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, 'Step 23.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 1, 'Step 23.d: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mline!", "bar_blue", "Step 23.ei: Verify line color", attribute_type='stroke')
        time.sleep(5)
        chartframe_gradient_fill = "url(#jschart_HOLD_0__lineargradient_0_0_100p_0_0_2550255_1_1_2552550_1_0_2550255_1)"
        chartframe_css = driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class^='chartFrame']")
        actual_gradient_fill = chartframe_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, chartframe_gradient_fill, "Step 23.e: Verify gradient fill is applied to the chart frame & background.")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """    
        Step 24: Click "IA" > "Exit".
        Step 25: Click "Cancel".
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(15)
        parent_css="#saveAllDlg div[id*='loginForm'] div[id*='saveChangesLabel']"
        resultobj.wait_for_property(parent_css, 1)
        btn_css="div[id*='loginForm'] div[class^=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('Cancel')].click()
        time.sleep(8)
        
        """    
        Step 26: Click "IA" > "Exit".
        Step 27: Click "Yes".
        Step 28: Verify it displays the "Save As" window.
        Step 29: Enter Title = "IA-VAL-CHART-005".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_saveas_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 30: Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_saveas_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(10) 
        
        """
        Step 31: Verify the saved fex can be executed and output is the same chart.
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 text[class^='dataLabels']"
        resultobj.wait_for_property(parent_css, 10)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step31:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step31:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step31:a(iii):Verify XY labels")
        expected_data_labels=['$421,377', '$189,217', '$186,534', '$190,695', '$630,054', '$308,986', '$878,063', '$360,570', '$333,414', '$190,081']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, 'Step 31.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 1, 'Step 31.d: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mline!", "bar_blue", "Step 31.ei: Verify line color", attribute_type='stroke')
        time.sleep(5)
        chartframe_gradient_fill = "url(#jschart_HOLD_0__lineargradient_0_0_100p_0_0_2550255_1_1_2552550_1_0_2550255_1)"
        chartframe_css = driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class^='chartFrame']")
        actual_gradient_fill = chartframe_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, chartframe_gradient_fill, "Step 31.e: Verify gradient fill is applied to the chart frame & background.")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step31', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 32: Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_saveas_ID, 'idis', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 33: Verify that it launches IA tool and display the chart on "Live Preview".
        """
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(elem)
        time.sleep(5)
        parent_css="#TableChart_1 text[class^='dataLabels']"
        resultobj.wait_for_property(parent_css, 2)
        xaxis_value="Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 33:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 33:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 33:a(iii):Verify XY labels")
        expected_data_labels=['$189,217', '$293,544']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, 'Step 33.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 1, 'Step 33.d: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 33.ei: Verify line color", attribute_type='stroke')
        time.sleep(5)
        chartframe_gradient_fill = "url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_2550255_1_1_2552550_1_0_2550255_1)"
        chartframe_css = driver.find_element_by_css_selector("#TableChart_1 rect[class^='chartFrame']")
        actual_gradient_fill = chartframe_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, chartframe_gradient_fill, "Step 33.e: Verify gradient fill is applied to the chart frame & background.")
        
        """
        Step 34: Click "IA" > "Exit".
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()