'''
Created on Dec 20, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228162
TestCase Name = Verify Data Labels for Stacked Bar chart (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2228162_TestClass(BaseTestCase):

    def test_C2228162(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228162'
        Test_Case_saveas_ID ="IA-VAL-CHART-017"
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Click "Format" tab.
        Step 03: Expand Chart Types group (if not already expanded).
        Step 04: Click "Other".
        Step 05: Select "Stacked Bar" and click "OK".
        """
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value='Selectachart', with_regular_exprestion=True)
        ia_ribbobj.select_other_chart_type('bar', 'vertical_stacked_bars', 2, ok_btn_click=True)
        time.sleep(3)
         
        """
        Step 06: Double click on "LAST_NAME", "SALARY", "GROSS".
        """
        time.sleep(3)
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 11)
         
        metaobj.datatree_field_click('SALARY', 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
         
        metaobj.datatree_field_click('GROSS', 2, 1)
        time.sleep(4)
        
        """
        Step 07: Verify a "Stacked Bar" chart is displayed in Live Preview.
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 22)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step07:a(i) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step07:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 11, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step07.d: Verify first bar color")
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step07:e Verify Y-Axis Title")
        time.sleep(5)
        
        """
        Step 08: Click "Series" tab.
        Step 09: Click "Data Labels" dropdown > "More Data Label Options".
        """
        ribbonobj.select_ribbon_item('Series', 'Data_labels_menubtn', opt='More Data Label Options')
        time.sleep(5)
        parent_css="[id^='QbDialog'] [class*='active'] #dataLabelSplitPane"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)
        utillobj.verify_object_visible(parent_css, True, "Step 09: Verify the Format Labels window is displayed.")
        
        """
        Step 10: Check "Show Data Labels" check box.
        """
        ia_ribbobj.set_format_labels_general('checkbox', 'show_data_label', 'uncheck')
        time.sleep(5)
            
        """
        Step 11: Click "Above" (dropdown) next to "Position".
        Step 12: Select "Center".
        """
        position_dropdown = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='stackedPositionLabelComboBox'] div[class^='bi-button button']")
        utillobj.click_on_screen(position_dropdown, 'middle')
        utillobj.click_on_screen(position_dropdown, 'middle',  click_type=0)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Center', custom_css="div[id*='BiComboBoxItem']")
        time.sleep(3)
        
        """
        Step 13: Uncheck "Show Cumulative Sums" and check "Show Stack Total".
        Step 14: Click "OK" in "Format Labels" window.
        """
        showcumulativesum_checkbox = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='stackedShowCumulativeSumsCheckBox'] input[type^='checkbox']")
        b=showcumulativesum_checkbox.get_property("checked")
        print(b)
        if b == True:
            showcumulativesum_checkbox.click()
        else:
            print("Step 13: Show Cumulative Sums check box is unchecked by default.")
            showcumulativesum_checkbox.click()
        time.sleep(3)
        ia_ribbobj.set_format_labels_general('checkbox', 'show_stacked_total', 'uncheck', ok_btn=True)
        time.sleep(3)
        
        """
        Step 15: Verify the chart in "Live Preview" displays data labels.
        """
        parent_css="#TableChart_1 text[class*='stackTotalLabel']"
        resultobj.wait_for_property(parent_css, 11)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step15:a(i) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step15:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 11, 'Step15.b: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step15:c")
        expected_data_labels1=['29,700', '21,780', '52,837', '17,650', '51,282', '36,230', '18,480', '31,100', '21,120', '31,750', '21,000']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels1, 'Step 15.d: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels2, 'Step 15.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 15.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 15.g: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 15.h: Verify first bar color")
        time.sleep(5)
        
        """
        Step 16: Click "Run".
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 17: Verify the same chart in "Live Preview" is displayed at run time.
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 text[class*='stackTotalLabel']"
        resultobj.wait_for_property(parent_css, 11)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step17:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 11, 'Step17.b: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step17:c Verify Y-Axis Title")
        expected_data_labels1=['29,700', '21,780', '52,837', '17,650', '51,282', '36,230', '18,480', '31,100', '21,120', '31,750', '21,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels1, 'Step 17.d: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels2, 'Step 17.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 17.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 17.g: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 17.h: Verify first bar color")
        time.sleep(5)
        bar=['LAST_NAME:BANNING', 'SALARY:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 17.i: Verify bar value")
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 18: Click "IA" > "Save".
        Step 19: Enter Title = "IA-VAL-CHART-017".
        Step 20: Click "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_saveas_ID)
        time.sleep(10)
           
        """
        Step 21: Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 22: Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_saveas_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(10) 
        
        """
        Step 23: Verify the chart is run in a new window.
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 text[class*='stackTotalLabel']"
        resultobj.wait_for_property(parent_css, 11)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 23:a(i) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 23:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 11, 'Step 23.b: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 23.c: Verify Y-Axis Title")
        expected_data_labels1=['29,700', '21,780', '52,837', '17,650', '51,282', '36,230', '18,480', '31,100', '21,120', '31,750', '21,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels1, 'Step 23.d: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels2, 'Step 23.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 23.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 23.g: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 23.h: Verify first bar color")
        time.sleep(5)
        bar=['LAST_NAME:BANNING', 'SALARY:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 23.i: Verify bar value")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step23', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 24: Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 25: Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_saveas_ID, 'idis', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 26: Verify IA is launched and preserves the chart in "Live Preview".
        """
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(elem)
        parent_css="#TableChart_1 text[class*='stackTotalLabel']"
        resultobj.wait_for_property(parent_css, 11)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 26:a(i) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 26:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 11, 'Step 26.b: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 26:c Verify Y-Axis Title")
        expected_data_labels1=['29,700', '21,780', '52,837', '17,650', '51,282', '36,230', '18,480', '31,100', '21,120', '31,750', '21,000']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels1, 'Step 26.d: Verify data labels1', custom_css="text[class*='dataLabels!s0']")
        expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels2, 'Step 26.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 26.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 26.g: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 26.h: Verify first bar color")
        
        """
        Step 27: Click "IA" > "Exit".
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()        