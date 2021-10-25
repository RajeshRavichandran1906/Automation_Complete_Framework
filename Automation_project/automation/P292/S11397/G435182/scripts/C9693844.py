"""-------------------------------------------------------------------------------------------
Created on September 06, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9693844
Test Case Title =  Verify Chart with Auto Drill (82xx)
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods

class C9693844_TestClass(BaseTestCase):

    def test_C9693844(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        querytree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        save_css = "#IbfsOpenFileDialog7_btnOK"
        
        Step1 = """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2F&master=ibisamp%2Fcarolap&tool=chart
        """
        chart.invoke_chart_tool_using_api("ibisamp/carolap", mrid = "mrid", mrpass = "mrpass", folder_path = "P292_S11397%2FG435182")
        chart.wait_for_visible_text(chart_css, "Group 0")
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Double click "DEALER_COST".
        """
        chart.double_click_on_datetree_item("DEALER_COST", 1)
        chart.wait_for_visible_text(querytree_css, "DEALER_COST")
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Expand COUNTRY in Dimension > COUNTRY > double click "COUNTRY".
        """
        chart.double_click_on_datetree_item("COUNTRY", 3)
        chart.wait_for_visible_text(querytree_css, "COUNTRY")
        utils.capture_screenshot("03.01", Step3)
        
        Step4 = """
            STEP 04 : Select "Format" > Run with > Enable "Auto Drill" button.
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "auto_drill")
        utils.capture_screenshot("04.01", Step4)
        
        Step5 = """
            STEP 05 : Click Save in the toolbar > Enter title as "C9693844" > Click Save button.
        """
        chart.select_item_in_top_toolbar('save')
        chart.wait_for_visible_text(save_css, "Save")
        
        chart.save_file_in_save_dialog("C9693844")
        utils.synchronize_until_element_disappear(save_css, chart.home_page_medium_timesleep)
        utils.capture_screenshot("05.01", Step5)
        
        Step6 = """
            STEP 06 : Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart.api_logout()
        utils.capture_screenshot("06.01", Step6)
        
        Step7 = """
            STEP 07 : Run C9693844.fex using API code
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S11397%252FG435181%252F&BIP_item=C9693844.fex
        """
        chart.run_fex_using_api_url("P292_S11397/G435182", "C9693844", "mrid", "mrpass", run_chart_css = "body > iframe")
        chart.switch_to_frame(frame_css = "body > iframe")
        chart.wait_for_visible_text("#jschart_HOLD_0", "ENGLAND")
        utils.capture_screenshot("07.01", Step7)
        
        Step8 = """
            STEP 08 : Hover over "ITALY" riser
            Tooltip value is displayed.
        """
        chart.verify_x_axis_label_in_run_window(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], msg = "Step 08.01 : The following chart is displayed.")
        chart.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K'], msg = "Step 08.02 : The following chart is displayed.")
        chart.verify_x_axis_title_in_run_window(['COUNTRY'],  msg = "Step 08.03 : The following chart is displayed.")
        chart.verify_y_axis_title_in_run_window(['DEALER_COST'], msg = "Step 08.04 : The following chart is displayed.")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 5, msg = "Step 08.05 : The following chart is displayed." )
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar!", "bar_blue", msg = "Step 08.06 : The following chart is displayed.")
        
        tooltip_list = ['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Drill down to CAR']
        chart.verify_tooltip_in_run_window(riser_css = "riser!s0!g2!mbar!", expected_tooltip_list = tooltip_list , msg = "Step08.07 : Tooltip value is displayed.", move_to_tooltip = True)
        utils.capture_screenshot("08.01", Step8, expected_image_verify = True)
        
        Step9 = """
            STEP 09 : Select "Drill down to CAR",
            The following chart is displayed.
        """
        chart.select_autodrill_chart_tooltip_menu("riser!s0!g2!mbar!", "Drill down to CAR")
        chart.wait_for_visible_text("#jschart_HOLD_0", "ALFA ROMEO")
        
        chart.verify_x_axis_label_in_run_window(['ALFA ROMEO', 'MASERATI'],  msg = "Step 09.01 : The following chart is displayed.")
        chart.verify_y_axis_label_in_run_window(['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K'], msg = 'Step 09.02 : The following chart is displayed.')
        chart.verify_x_axis_title_in_run_window(['CAR'], msg = "Step 09.03 : The following chart is displayed.")
        chart.verify_y_axis_title_in_run_window(['DEALER_COST'],  msg = "Step 09.04 : The following chart is displayed.")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 2, msg = "Step 09.05 : The following chart is displayed.")
        chart.verify_chart_color("jschart_HOLD_0 ", "riser!s0!g1!mbar!", "bar_blue", msg = "Step 09.06 : The following chart is displayed.")
        chart.verify_chart_autodrill_breadcrumb_text(['Home->(COUNTRY)ITALY'], "09.07")
        utils.capture_screenshot("09.01", Step9, expected_image_verify = True)
        
        Step10 = """
            STEP 10 : Hover over "MASERATI" riser.
            Tooltip value displayed with following options.
        """
        tooltip_list = ['CAR:MASERATI', 'DEALER_COST:25,000', 'Reset', 'Go up to COUNTRY', 'Drill down to MODEL']
        chart.verify_tooltip_in_run_window(riser_css = "riser!s0!g1!mbar!", expected_tooltip_list = tooltip_list, msg = "Step 10 : Tooltip value displayed with following options.", move_to_tooltip = True)
        utils.capture_screenshot("10.01", Step10, expected_image_verify = True)
        
        Step11 = """
            STEP 11 : Select "Drill Down to MODEL".
        """
        chart.select_autodrill_chart_tooltip_menu("riser!s0!g1!mbar!", "Drill down to MODEL")
        chart.wait_for_visible_text("#jschart_HOLD_0", "DORA 2 DOOR")
        utils.capture_screenshot("11.01", Step11, expected_image_verify = True)
        
        Step12 = """
            STEP 12 : Hover over "DORA 2 DOOR" riser.
            Tooltip value displayed with following options.
        """
        tooltip_list = ['MODEL:DORA 2 DOOR', 'DEALER_COST:25,000', 'Reset', 'Go up to CAR']
        chart.verify_tooltip_in_run_window(riser_css = "riser!s0!g0!mbar!", expected_tooltip_list = tooltip_list, msg = "Step 12.01 : Tooltip value displayed with following options.", move_to_tooltip = True)
        utils.capture_screenshot("12.01", Step12, expected_image_verify = True)
        
        Step13 = """
            STEP 13 : Select "Restore Original".
            The following chart is displayed.
        """
        chart.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!", "Reset", wait_time = 5)
        chart.wait_for_visible_text("#jschart_HOLD_0", "ENGLAND")
        
        chart.verify_x_axis_label_in_run_window(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], msg = "Step 13.01 : The following chart is displayed.")
        chart.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K'], msg = "Step 13.02 : The following chart is displayed.")
        chart.verify_x_axis_title_in_run_window(['COUNTRY'],  msg = "Step 13.03 : The following chart is displayed.")
        chart.verify_y_axis_title_in_run_window(['DEALER_COST'], msg = "Step 13.04 : The following chart is displayed.")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 5, msg = "Step 13.05 : The following chart is displayed." )
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mbar!", "bar_blue", msg = "Step 13.06 : The following chart is displayed.")
        utils.capture_screenshot("13.01", Step13, expected_image_verify = True)
        
        Step14 = """
            STEP 14 : Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart.api_logout()
        utils.capture_screenshot("14.01", Step14)

if __name__ == '__main__':
    unittest.main()