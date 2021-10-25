'''
Created on Dec 21, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228165
TestCase Name = Verify HTML5 Gradient Series with Pie chart (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2228165_TestClass(BaseTestCase):

    def test_C2228165(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228165'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/ggsales
        """
        utillobj.infoassist_api_login('chart','ibisamp/ggsales','P292/S10032_chart_1', 'mrid', 'mrpass')
        
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """
        Step 02: Select "Format" > "Chart Types" > "Pie".
        """
        ribbonobj.select_ribbon_item('Format', 'Pie')
        time.sleep(3)
        
        """
        Step 03: Double Click "Unit Sales","Region".
        """
        
        metaobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 path[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        metaobj.datatree_field_click('Region', 2, 1)
        parent_css="#TableChart_1 path[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 15)
        
        """
        Step 04: Verify the following chart is displayed.
        """
        xaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step04:a(i) Verify X-Axis Title", custom_css="text[class*='pieLabel']")
        legend=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step04:c")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 4, 'Step 04a: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge", "bar_blue", "Step 04.d: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mwedge", "bar_green", "Step 04.e: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge", "dark_green", "Step 04.f: Verify third bar color")
        time.sleep(5)
        
        """
        Step 05: Select "Series" > "Data Labels".
        """
        ribbonobj.select_ribbon_item('Series', 'data_labels')
        
        """
        Step 06: Verify the following chart is displayed.
        """
        
        parent_css="#TableChart_1 text[class^='dataLabels']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 20)
        
        xaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step06:a(i) Verify X-Axis Title", custom_css="text[class*='pieLabel']")
        legend=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step06:c")
        expected_data_labels=['21%', '23%', '29%', '26%']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, 'Step 06.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 4, 'Step 06a: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge", "bar_blue", "Step 06.d: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mwedge", "bar_green", "Step 06.e: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge", "dark_green", "Step 06.f: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mwedge", "pale_yellow", "Step 06.g: Verify fourth bar color")
        time.sleep(5)
        
        """
        Step 07: Click "All Series" (dropdown) in "Select" group.
        Step 08: Select "Series 0 - Midwest".
        """
        ribbonobj.select_ribbon_item('Series', 'select_menubtn')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Series 0 - Midwest', custom_css="div[id*='BiComboBoxItem']")
        time.sleep(3)
        
        """
        Step 09: Click "Style" icon.
        """
        ribbonobj.select_ribbon_item('Series', 'style')
        time.sleep(2)
        
        """
        Step 10: Select "Gradient fill" radio button.
        Step 11: Click "OK".
        """
        parent_css="[id^='QbDialog'] [class*='active'] div[id*='seriesGradientSplitPane']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        utillobj.verify_object_visible(parent_css, True, "Step 10:Format series window is displayed.")
        
        gradientfill_radiobutton = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] div[id*='gradientFillRadioBtn'] input[type^='radio']")
        a=gradientfill_radiobutton.get_property("checked")
        print(a)
        if a != True:
            gradientfill_radiobutton.click()
        else:
            print("Step 10: Gradient fill radio button is checked by default.")
        time.sleep(3)
        ok_btn = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='seriesGradientOkBtn']")
        utillobj.click_on_screen(ok_btn, 'middle')
        utillobj.click_on_screen(ok_btn, 'middle', click_type=0)
        
        """
        Step 12: Verify the following chart is displayed.
        """
        time.sleep(5)
        parent_css="#TableChart_1 text[class^='dataLabels']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 15)
        
        xaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step12:a(i) Verify X-Axis Title", custom_css="text[class*='pieLabel']")
        legend=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step12:c")
        expected_data_labels=['21%', '23%', '29%', '26%']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, 'Step 12.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 4, 'Step 12a: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mwedge", "bar_green", "Step 12.e: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge", "dark_green", "Step 12.f: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mwedge", "pale_yellow", "Step 12.g: Verify fourth bar color")
        time.sleep(5)
        
        expected_gradient_fill = "url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_255255255_1_1_128128128_1)"
        pie_segment_css = driver.find_element_by_css_selector("#TableChart_1 path[class^='riser!s0!g0!mwedge']")
        actual_gradient_fill = pie_segment_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, expected_gradient_fill, "Step 12: Verify gradient fill is applied to the chart.")
        
        """
        Step 13: Click "Run".
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 14: Verify the following chart is displayed.
        """
        
        parent_css="#jschart_HOLD_0 text[class^='dataLabels']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step14:a(i) Verify X-Axis Title", custom_css="text[class*='pieLabel']")
        legend=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step14:c")
        expected_data_labels=['25%', '25%', '25%', '25%']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, 'Step 14.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 4, 'Step 14a: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mwedge", "bar_green", "Step 14.e: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge", "dark_green", "Step 14.f: Verify third bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mwedge", "pale_yellow", "Step 14.g: Verify fourth bar color")
        time.sleep(5)
        expected_gradient_fill = "url(#jschart_HOLD_0__lineargradient_0_0_100p_0_0_255255255_1_1_128128128_1)"
        pie_segment_css = driver.find_element_by_css_selector("#jschart_HOLD_0 path[class^='riser!s0!g0!mwedge']")
        actual_gradient_fill = pie_segment_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, expected_gradient_fill, "Step 14: Verify gradient fill is applied to the chart.")
        time.sleep(5)
       
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 15: Dismiss the "Run" window.
        Step 16: Click "IA" > "Save" > "C2228165" > "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
           
        """
        Step 17: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 18:Restore the fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228165.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
             
        """
        Step 19: Verify the following chart is displayed.
        """
        
        parent_css="#TableChart_1 text[class^='dataLabels']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 65)
        
        xaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step19:a(i) Verify X-Axis Title", custom_css="text[class*='pieLabel']")
        legend=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step19:c")
        expected_data_labels=['21%', '23%', '29%', '26%']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, 'Step 19.c: Verify stacktotal labels', custom_css="text[class^='dataLabels']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 4, 'Step 19: Verify number of gauge segment displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mwedge", "bar_green", "Step 19.e: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mwedge", "dark_green", "Step 19.f: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mwedge", "pale_yellow", "Step 19.g: Verify fourth bar color")
        time.sleep(5)
        
        expected_gradient_fill = "url(#pfjTableChart_1__lineargradient_0_0_100p_0_0_255255255_1_1_128128128_1)"
        pie_segment_css = driver.find_element_by_css_selector("#TableChart_1 path[class^='riser!s0!g0!mwedge']")
        actual_gradient_fill = pie_segment_css.get_attribute('fill')
        print(actual_gradient_fill)
        utillobj.asequal(actual_gradient_fill, expected_gradient_fill, "Step 19: Verify gradient fill is applied to the chart.")
        
        """
        Step 20: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()