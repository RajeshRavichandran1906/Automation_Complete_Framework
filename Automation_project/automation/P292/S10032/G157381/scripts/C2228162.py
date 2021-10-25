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
from common.lib import global_variables

class C2228162_TestClass(BaseTestCase):

    def test_C2228162(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228162'
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser = utillity.UtillityMethods.parseinitfile(self,'browser')
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        VisualizationResultareaLocators.__dict__['default_riser']
          
        """
        Step 02: Click "Format" tab.
        Step 03: Expand Chart Types group (if not already expanded).
        Step 04: Click "Other".
        Step 05: Select "Stacked Bar" and click "OK".
        """
        
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Selectachart', 30)
        
        ia_ribbobj.select_other_chart_type('bar', 'vertical_stacked_bars', 2, ok_btn_click=True)
        time.sleep(3)
         
        """
        Step 06: Double click on "LAST_NAME", "SALARY", "GROSS".
        """
        
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css,11,15)
         
        metaobj.datatree_field_click('SALARY', 2, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 15)
         
        metaobj.datatree_field_click('GROSS', 2, 1)
        time.sleep(4)
        
        """
        Step 07: Verify a "Stacked Bar" chart is displayed in Live Preview.
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 22, 30)
        
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
        parent_css="[id^='QbDialog'] [class*='active'] #dataLabelSplitPane"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
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
        utillobj.synchronize_with_number_of_element(parent_css, 11,25)
       
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
        '''updating datalabels checkpoint as per comments in CHART-3044'''        
        if global_variables.Global_variables.browser_name =="ie":
            expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '9,130', '7,040', '14,983', '9,000']
        else:
            expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
            
        resultobj.verify_data_labels('TableChart_1', expected_data_labels2, 'Step 15.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 15.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 15.g: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 15.h: Verify first bar color")
        
        """
        Step 16: Click "Run".
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 17: Verify the same chart in "Live Preview" is displayed at run time.
        """
        
        parent_css="#jschart_HOLD_0 text[class*='stackTotalLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 30)
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
        '''updating datalabels checkpoint as per comments in CHART-3044'''
        if global_variables.Global_variables.browser_name =="ie":
            expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '9,130', '7,040', '14,983', '9,000']
        else:
            expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
            
        
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels2, 'Step 17.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 17.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 17.g: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 17.h: Verify first bar color")
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 18: Click Save in the toolbar > Save as "C2228162" > Click Save
        Step 19: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        Step 20: Run saved fex from bip using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228162.fex
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
           
        """
        Step 21: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 22: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228162.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1', mrid='mrid', mrpass='mrpass')
        
        """
        Step 23: Verify IA is launched and preserves the chart in "Live Preview".
        """
        
        parent_css="#TableChart_1 text[class*='stackTotalLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 65)
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
        '''updating datalabels checkpoint as per comments in CHART-3044'''
        if global_variables.Global_variables.browser_name =="ie":
            expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '9,130', '7,040', '14,983', '9,000']
        else:
            expected_data_labels2=['2,475', '9,075', '22,014', '2,971', '17,094', '6,100', '1,540', '9,130', '7,040', '14,983', '9,000']
         
        resultobj.verify_data_labels('TableChart_1', expected_data_labels2, 'Step 26.e: Verify data labels2', custom_css="text[class*='dataLabels!s1']")
        expected_stacktotal_labels=['32,175', '30,855', '74,851', '20,621', '68,376', '42,330', '20,020', '40,230', '28,160', '46,733', '30,000']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 26.f: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 26.g: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 26.h: Verify first bar color")
        
        """
        Step 24: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
        
if __name__ == '__main__':
    unittest.main()        