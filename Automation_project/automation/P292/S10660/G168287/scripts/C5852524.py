'''
Created on October 30, 2018

@author: Prabhakaran

TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852524
TestCase Name = Verify Mekko chart with 3 Measures (82xx)
'''

import unittest
from common.lib.global_variables import Global_variables
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart

class C5852524_TestClass(BaseTestCase):

    def test_C5852524(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5852524'
        
        """
        TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        chart_obj = Chart(self.driver)
        
        """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
         
        """
            STEP 02 : Click "Format" tab > "Other" icon > Click "HTML5" icon > select "Mekko" chart type.
            STEP 03 : Click "OK".
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Selectachart', 35) 
        ia_ribbobj.select_other_chart_type('html5', 'html5_Mekko', 2, ok_btn_click=True)
          
        """
            STEP 04 : Verify the default Mekko chart is displayed in "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 25, 20)
         
        expected_xval_list=['Group 4', 'Group 3', 'Group 2', 'Group 1', 'Group 0']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_stacktotal_labels=['175', '150', '125', '100', '75']
        legend=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 04.00 : Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 5, 5, 'Step 04.01 :  Verify the total number of risers displayed on preview')
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 04.02 : Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 04.03 : ")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 04.04 : Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!mbar", "bar_green", "Step 04.05 : Verify second bar color")
         
        """
            STEP 05 : Double click "LAST_NAME", "CURR_SAL", "SALARY", "GROSS". 
        """
        chart_obj.double_click_on_datetree_item('LAST_NAME', 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 15)
        chart_obj.collapse_data_field_section('Dimensions')
        chart_obj.double_click_on_datetree_item('CURR_SAL', 1)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, 15)
        chart_obj.double_click_on_datetree_item('SALARY', 1)
        parent_css= "#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 22, 15)
        chart_obj.double_click_on_datetree_item('GROSS', 1)
        
        """
            STEP 06 : Verify the Mekko chart is updated in "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 15)
         
        xaxis_value="LAST_NAME"
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        if Global_variables.browser_name == 'firefox':
            expected_xval_list = ['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GREE...']
        else:   
            expected_xval_list = ['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GRE...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 06.01 : Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 06.02 : Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 3, 11, 'Step 06.03 : Verify the total number of risers displayed on preview')
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 06.04 : Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 06.05 :")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar", "bar_blue", "Step 06.06 : Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar", "bar_green", "Step 06.07 : Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!mbar", "dark_green", "Step 06.08 : Verify third bar color")
         
        """
            STEP 07 : Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        utillobj.switch_to_frame(pause=2)
          
        """
            STEP 08 : Verify the Mekko chart is displayed correctly at run time.
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 25)
         
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        xaxis_value="LAST_NAME"
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        if Global_variables.browser_name == 'firefox':
            expected_xval_list = ['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GREE...']
        else:   
            expected_xval_list = ['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GRE...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 08.00 : Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 08.01 : Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 3, 11, 'Step 08.02 : Verify the total number of risers displayed on preview')
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 08.03 : Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 08.04 : ")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar", "bar_blue", "Step 08.05 : Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g2!mbar", "bar_green", "Step 08.06 : Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g2!mbar", "dark_green", "Step 08.07 : Verify third bar color")
         
        utillobj.switch_to_default_content(pause=2)
     
        """
            STEP 09 : Click Save in the toolbar > Save as "C5852524" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """
            STEP 10 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
     
        """
            STEP 11 : Run saved fex from bip using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C5852524.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10660_chart_2','mrid','mrpass')
         
        """
            STEP 12 : Verify the chart is run in a new window
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 65)
 
        xaxis_value="LAST_NAME"
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_xval_list=['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GREENS...']
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 12.00 : Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 12.01 : Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 3, 11, 'Step 12.02 : Verify the total number of risers displayed on preview')
        resultobj.verify_data_labels('jschart_HOLD_0', expected_stacktotal_labels, 'Step 12.03 : Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 12.04 : ")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar", "bar_blue", "Step 12.05 : Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g2!mbar", "bar_green", "Step 12.06 : Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g2!mbar", "dark_green", "Step 12.07 : Verify third bar color")
        
        """
            STEP 13 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            STEP 14 : Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC5852524.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
             
        """
            STEP 15 : Verify IA is launched preserving the Mekko chart in "Live Preview" and "query pane" bucket fields.
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 33, 65)
        
        legend=['CURR_SAL', 'SALARY', 'GROSS']
        xaxis_value="LAST_NAME"
        expected_stacktotal_labels=['102K', '95,238', '69,433', '61,875', '60,810', '56,330', '52,635', '49,280', '41,000', '38,500', '29,621']
        if Global_variables.browser_name == 'firefox':
            expected_xval_list = ['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GREE...']
        else:   
            expected_xval_list = ['CROSS', 'IRVING', 'SMITH', 'BANNING', 'JONES', 'MCKNIGHT', 'BLACKWOOD', 'ROMANS', 'STEVENS', 'MCCOY', 'GRE...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 15.00 : Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 15.01 : Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 3, 11, 'Step 15.02 : Verify the total number of risers displayed on preview')
        resultobj.verify_data_labels('TableChart_1', expected_stacktotal_labels, 'Step 15.03 : Verify stacktotal labels', custom_css="text[class*='stackTotalLabel']")
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 15.04 : ")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar", "bar_blue", "Step 15.05 : Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar", "bar_green", "Step 15.06 : Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!mbar", "dark_green", "Step 15.07 : Verify third bar color")
        
        """
            STEP 16 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
    
if __name__ == '__main__':
    unittest.main()