'''
Created on Dec 21, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228164
TestCase Name = Verify Mekko chart with 3 Measures (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase

class C2228164_TestClass(BaseTestCase):

    def test_C2228164(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228164'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """
        Step 02: Click "Format" tab > "Other" icon > Click "HTML5" icon > select "Mekko" chart type.
        Step 03: Click "OK".
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Selectachart', 35)
        
        ia_ribbobj.select_other_chart_type('html5', 'html5_Mekko', 2, ok_btn_click=True)
        time.sleep(3)
         
        """
        Step 04:Verify the default Mekko chart is displayed in "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 25, 20)
        
        expected_xval_list=['Group 4', 'Group 3', 'Group 2', 'Group 1', 'Group 0']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step07:a(i):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 5, 5, 'Step07.b: Verify the total number of risers displayed on preview')
        expected_stacktotal_labels=['175', '150', '125', '100', '75']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 07.c: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        legend=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step07:d")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 07.e: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!mbar", "bar_green", "Step 07.f: Verify second bar color")
        
        """
        Step 05:Double click "LAST_NAME", "CURR_SAL", "SALARY", "GROSS". 
        """
        
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 15)
        
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, 15)
         
        metaobj.datatree_field_click('SALARY', 2, 1)
        parent_css= "#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 22, 15)
        
        metaobj.datatree_field_click('GROSS', 2, 1)
        
        
        """
        Step 06: Verify the Mekko chart is updated in "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 15)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step09:a(i) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GRE...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step09:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 3, 11, 'Step09.b: Verify the total number of risers displayed on preview')
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 09.c: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step15:c")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar", "bar_blue", "Step 09.d: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar", "bar_green", "Step 09.e: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!mbar", "dark_green", "Step 09.f: Verify third bar color")
        
        """
        Step 07: Click "Run".
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
       
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 08:Verify the Mekko chart is displayed correctly at run time.
        """
        
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 25)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GRE...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step11:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 3, 11, 'Step11.b: Verify the total number of risers displayed on preview')
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 11.c: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step11:d")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar", "bar_blue", "Step 11.e: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g2!mbar", "bar_green", "Step 11.f: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g2!mbar", "dark_green", "Step 11.g: Verify third bar color")
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 09:Click Save in the toolbar > Save as "C2228164" > Click Save
        Step 10:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 11:Run saved fex from bip using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228164.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10032_chart_1','mrid','mrpass')
        
        """
        Step 12: Verify the chart is run in a new window
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 65)

        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step16:a(i) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GREENSP...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step16:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 3, 11, 'Step16.b: Verify the total number of risers displayed on preview')
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 16.c: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step16:d")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar", "bar_blue", "Step 16.e: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g2!mbar", "bar_green", "Step 16.f: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g2!mbar", "dark_green", "Step 16.g: Verify third bar color")
        time.sleep(5)
        
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 13:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 14:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228164.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
             
        """
        Step 15:Verify IA is launched preserving the Mekko chart in "Live Preview" and "query pane" bucket fields.
        """
        
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 65)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step19:a(i) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GRE...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step19:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 3, 11, 'Step19.b: Verify the total number of risers displayed on preview')
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 19.c: Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step19:d")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar", "bar_blue", "Step 19.e: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar", "bar_green", "Step 19.f: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!mbar", "dark_green", "Step 19.g: Verify third bar color")
        
        """
        Step 16:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()