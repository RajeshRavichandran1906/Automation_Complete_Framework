'''
Created on Dec 19, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228154
TestCase Name = Verify Gauge dialog (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color
from common.lib.global_variables import Global_variables

class C2228154_TestClass(BaseTestCase):

    def test_C2228154(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228154'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        VisualizationResultareaLocators.__dict__['default_riser']
        
        """
        Step 02: Verify "HTML5" is the selected "Output Types".
        """
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 75)
        
        homeformattype_css="#HomeFormatType img[src*='html5']"
        utillobj.verify_object_visible(homeformattype_css, True, "Step 02.1: Verify output format as Active Report")
        outputformattype_css="#sbpOutputFormatPanel #sbpOutputFormat img[src*='html5']"
        utillobj.verify_object_visible(outputformattype_css, True, "Step 02.2: Verify output format as Active Report")
        time.sleep(5)
         
        """
        Step 03: Select "Format" > "Chart Types" > "Other" > "Special" > "Gauge".
        Step 04: Click "OK".
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value='Selectachart', with_regular_exprestion=True)
        ia_ribbobj.select_other_chart_type('special', 'gauge', 1, ok_btn_click=True)
         
        """
        Step 05: Verify the following Gauge chart is displayed on "Live Preview".
        """
        elem="#pfjTableChart_1 path[class*='gaugeRange']"
        utillobj.synchronize_with_number_of_element(elem, 10, 35)
        
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 10, 'Step 05a: Verify number of gauge segment displayed', custom_css="path[class*='gaugeRange']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 2, 'Step 05b: Verify number of gauge needle displayed', custom_css="path[class*='riser']")
        expected_xval_list=['Group 0', 'Group 1']
        expected_yval_list=['35', '0']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05c: Verify gauge xy Labels', x_custom_css="text[class*='groupLabel']", y_custom_css="text[class*='totalLabel']")
        
        guage1=driver.find_elements_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(3)")
        actual_color = Color.from_string(guage1[0].value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('green', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 5d: Verify gauge1 color(with green color)")
        guage2=driver.find_elements_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(4)")
        actual_color = Color.from_string(guage2[1].value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('yellow', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 5e: Verify gauge2 color(with yellow color)")
        guage3=driver.find_elements_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(5)")
        actual_color = Color.from_string(guage3[0].value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('red', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 5f: Verify gauge3 color(with red color)")
         
        """
        Step 06: Double click "LAST_NAME", "SALARY".
        """
        
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALARY', 2, 1)
        parent_css="#TableChart_1 svg g text[class*='totalLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 35)
         
        """
        Step 07: Drag "LAST_NAME" into "Filter" pane.
        """

        metaobj.datatree_field_click('LAST_NAME',1, 1, 'Filter')
        time.sleep(4)
         
        """
        Step 08: Double click on <Value> > "Get Values" (dropdown) > "All".
        Step 09: Double click "JONES".
        Step 10: Verify "JONES" has been added to the "Multiple Values" box.
        Step 11: Click "OK" (2x).
        """
        ia_ribbobj.create_constant_filter_condition('All', ['JONES'], filter_dialog_close=True)
         
        """
        Step 12: Verify the following "Gauge" chart is displayed in "Live Preview".
        """
        
        elem="#pfjTableChart_1 path[class*='gaugeRange']"
        utillobj.synchronize_with_number_of_element(elem, 5, 35)
        
        metaobj.verify_filter_pane_field('LAST_NAME Equal to JONES', 1, 'Step 12')
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 5, 'Step 12a: Verify number of gauge segment displayed', custom_css="path[class*='gaugeRange']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 1, 'Step 12b: Verify number of gauge needle displayed', custom_css="path[class*='riser']")
        expected_xval_list=['JONES']
        expected_yval_list=['36230']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 12c: Verify gauge xy Labels', x_custom_css="text[class*='groupLabel']", y_custom_css="text[class*='totalLabel']")
        guage1=driver.find_element_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(3)")
        actual_color = Color.from_string(guage1.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('green', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 12d: Verify gauge1 color(with green color)")
        guage2=driver.find_element_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(4)")
        actual_color = Color.from_string(guage2.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('yellow', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 12e: Verify gauge2 color(with yellow color)")
        guage3=driver.find_element_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(5)")
        actual_color = Color.from_string(guage3.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('red', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 12f: Verify gauge3 color(with red color)")
        time.sleep(5)
         
        """
        Step 13: Expand "Features" group in "Format" tab.
        Step 14: Click "Gauges".
        """
        ribbonobj.select_ribbon_item('Format', 'Gauges')
        time.sleep(3)
         
        """
        Step 15: Verify the "Format Gauge" window is displayed.
        Step 16: Click "OK".
        """
        parent_css="[id^='QbDialog'] [class*='active'] [class*='window-caption'] [class*='bi-label']" #
        utillobj.synchronize_with_visble_text(parent_css, 'Format Gauge', 30)
        
        utillobj.verify_object_visible(parent_css, True, "Step 15a: Verify the Format Gauge window is displayed.")
        showtitle_checkbox = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='showTitleCheckBox'] input[type^='checkbox']").get_property("checked")
        #added a str(true) in asequal since IE accepts string and FF/CR gets boolean True
        utillobj.asequal(showtitle_checkbox, "true" if Global_variables.browser_name=='ie' else True, "Step 15b: Verify the Format Gauge window showtitle_checkbox is checked.")
        showvalue_checkbox = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='showValueCheckBox'] input[type^='checkbox']").get_property("checked")
        utillobj.asequal(showvalue_checkbox, "true" if Global_variables.browser_name=='ie' else True, "Step 15b: Verify the Format Gauge window showtitle_checkbox is checked.")
        time.sleep(3)
        ok_btn = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='gaugeOkBtn']")
        utillobj.click_on_screen(ok_btn, 'middle')
        utillobj.click_on_screen(ok_btn, 'middle', click_type=0)
         
        """
        Step17: Click "Run".
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 40)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 18: Verify the following chart is displayed at runtime.
        """
        elem="#jschart_HOLD_0 path[class*='gaugeRange']"
        utillobj.synchronize_with_number_of_element(elem, 5, 35)
        
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step 18a: Verify number of gauge segment displayed', custom_css="path[class*='gaugeRange']")
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 1, 'Step 18b: Verify number of gauge needle displayed', custom_css="path[class*='riser']")
        expected_xval_list=['JONES']
        expected_yval_list=['36230']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 18c: Verify gauge xy Labels', x_custom_css="text[class*='groupLabel']", y_custom_css="text[class*='totalLabel']")
        guage1=driver.find_element_by_css_selector("#jschart_HOLD_0 path[class*='gauge']:nth-child(3)")
        actual_color = Color.from_string(guage1.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('green', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 18d: Verify gauge1 color(with green color)")
        guage2=driver.find_element_by_css_selector("#jschart_HOLD_0 path[class*='gauge']:nth-child(4)")
        actual_color = Color.from_string(guage2.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('yellow', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 18e: Verify gauge2 color(with yellow color)")
        guage3=driver.find_element_by_css_selector("#jschart_HOLD_0 path[class*='gauge']:nth-child(5)")
        actual_color = Color.from_string(guage3.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('red', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 18f: Verify gauge3 color(with red color)")
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
         
        """
        Step 19:Click Save in the toolbar > Save as "C2228154" > Click Save
        Step 20: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
           
        """
        Step 21: Run from bip
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228154.fex
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step 22: Verify the correct chart is displayed in the chart run window.
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10032_chart_1','mrid','mrpass')
        
        """
        Step 23: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        elem="#jschart_HOLD_0 path[class*='gaugeRange']"
        utillobj.synchronize_with_number_of_element(elem, 5, 65)
        
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step 23a: Verify number of gauge segment displayed', custom_css="path[class*='gaugeRange']")
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 1, 'Step 23b: Verify number of gauge needle displayed', custom_css="path[class*='riser']")
        expected_xval_list=['JONES']
        expected_yval_list=['36230']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 23c: Verify gauge xy Labels', x_custom_css="text[class*='groupLabel']", y_custom_css="text[class*='totalLabel']")
        time.sleep(5)
        guage1=driver.find_element_by_css_selector("#jschart_HOLD_0 path[class*='gauge']:nth-child(3)")
        actual_color = Color.from_string(guage1.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('green', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 23d: Verify gauge1 color(with green color)")
        guage2=driver.find_element_by_css_selector("#jschart_HOLD_0 path[class*='gauge']:nth-child(4)")
        actual_color = Color.from_string(guage2.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('yellow', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 23e: Verify gauge2 color(with yellow color)")
        guage3=driver.find_element_by_css_selector("#jschart_HOLD_0 path[class*='gauge']:nth-child(5)")
        actual_color = Color.from_string(guage3.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('red', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 23f: Verify gauge3 color(with red color)")
        
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step23', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 24: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228154.fex
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step 25: Verify "IA" is launched and displays the correct chart in "Live Preview".
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        
        """
        Step 26: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        elem="#pfjTableChart_1 path[class*='gaugeRange']"
        utillobj.synchronize_with_number_of_element(elem, 5, 65)
        
        metaobj.verify_filter_pane_field('LAST_NAME Equal to JONES', 1, 'Step 26:')
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 5, 'Step 26a: Verify number of gauge segment displayed', custom_css="path[class*='gaugeRange']")
        iaresultobj.verify_number_of_chart_segment("TableChart_1", 1, 'Step 26b: Verify number of gauge needle displayed', custom_css="path[class*='riser']")
        expected_xval_list=['JONES']
        expected_yval_list=['36230']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 26c: Verify gauge xy Labels', x_custom_css="text[class*='groupLabel']", y_custom_css="text[class*='totalLabel']")
        time.sleep(5)
        guage1=driver.find_element_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(3)")
        actual_color = Color.from_string(guage1.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('green', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 26d: Verify gauge1 color(with green color)")
        guage2=driver.find_element_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(4)")
        actual_color = Color.from_string(guage2.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('yellow', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 26e: Verify gauge2 color(with yellow color)")
        guage3=driver.find_element_by_css_selector("#TableChart_1 path[class*='gauge']:nth-child(5)")
        actual_color = Color.from_string(guage3.value_of_css_property('fill')).rgba
        expected_color=utillobj.color_picker('red', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 26f: Verify gauge3 color(with red color)")
        
        
if __name__ == '__main__':
    unittest.main()        