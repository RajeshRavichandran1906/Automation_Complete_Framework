"""-------------------------------------------------------------------------------------------
Created on September 09, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6459363
Test Case Title =  New Histogram
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods

class C6459363_TestClass(BaseTestCase):

    def test_C6459363(self):
        
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
        ok_button_css = "#qbSelectChartTypeDlgOkBtn"
        
        Step1 = """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2F&master=baseapp%2Fwf_retail&tool=chart
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail", mrid = "mrid", mrpass = "mrpass", folder_path = "P292_S11397%2FG435181")
        chart.wait_for_visible_text(chart_css, "Group 0")
        utils.wait_for_page_loads(chart.home_page_long_timesleep) #firefox its required
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Select Format tab > Select Other > Bar > Select "Vertical Histogram" chart > Click OK button.
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text(ok_button_css, "OK")
        chart.select_other_chart_type("bar", "vertical_histogram", 1, verify_selection=False)
        utils.synchronize_until_element_disappear(ok_button_css, chart.home_page_medium_timesleep)
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Expand Product > Product > Model > Attributes > Drag "Price,Dollars" to Measure bucket
            Prefix CNT is added in field.
            Bin field is created and canvas updated successfully.
        """
        chart.drag_field_from_data_tree_to_query_pane("Price,Dollars", 1, "Measure", 1)
        chart.wait_for_visible_text(querytree_css, "CNT.Price,Dollars")
        
        chart.verify_all_fields_in_query_pane(['Chart (wf_retail)', 'Matrix', 'Rows', 'Columns', 'Marker', 'Measure', 'CNT.Price,Dollars', 'PRICE_DOLLARS_BIN_1', 'Tooltip', 'Multi-graph', 'Animate'], "Step 03.01 : Prefix CNT is added in field.")
        chart.verify_x_axis_label_in_preview(['20.00', '50.00', '60.00', '70.00', '80.00', '90.00', '100.00', '110.00', '120.00', '140.00', '150.00', '160.00', '170.00', '180.00', '190.00', '210.00', '220.00', '230.00', '240.00', '260.00', '270.00', '280.00', '290.00', '310.00', '330.00', '340.00', '360.00', '370.00', '380.00', '390.00', '440.00', '470.00', '480.00', '490.00', '520.00', '540.00', '590.00', '640.00', '680.00', '690.00', '780.00', '790.00', '880.00', '890.00', '990.00', '1,180.00', '1,290.00', '1,390.00', '1,990.00', '2,240.00', '3,390.00', '3,490.00', '3,990.00'] , msg = "Step 03.02 : Bin field is created and canvas updated successfully.")
        chart.verify_x_axis_title_in_preview(['PRICE_DOLLARS_BIN_1'],  msg = "Step 03.03 : Bin field is created and canvas updated successfully.")
        chart.verify_y_axis_label_in_preview(['0', '3', '6', '9', '12', '15'], msg = "Step 03.04 : Bin field is created and canvas updated successfully.")
        chart.verify_y_axis_title_in_preview(['CNT Price Dollars'], msg = "Step 03.05 : Bin field is created and canvas updated successfully.")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 53, msg = "Step 03.06 : Bin field is created and canvas updated successfully.")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g5!mbar!", "bar_blue", msg = "Step 03.07 : Bin field is created and canvas updated successfully")
        utils.capture_screenshot("03.01", Step3, expected_image_verify = True)
        
        Step4 = """
            STEP 04 : Click Run button.
            Chart displayed in run time.
        """
        chart.select_item_in_top_toolbar("run")
        chart.switch_to_frame()
        chart.wait_for_visible_text("#jschart_HOLD_0", "CNT")
        
        chart.verify_x_axis_label_in_run_window(['20.00', '50.00', '60.00', '70.00', '80.00', '90.00', '100.00', '110.00', '120.00', '140.00', '150.00', '160.00', '170.00', '180.00', '190.00', '210.00', '220.00', '230.00', '240.00', '260.00', '270.00', '280.00', '290.00', '310.00', '330.00', '340.00', '360.00', '370.00', '380.00', '390.00', '440.00', '470.00', '480.00', '490.00', '520.00', '540.00', '590.00', '640.00', '680.00', '690.00', '780.00', '790.00', '880.00', '890.00', '990.00', '1,180.00', '1,290.00', '1,390.00', '1,990.00', '2,240.00', '3,390.00', '3,490.00', '3,990.00'] , msg = "Step 04.01 : Bin field is created and canvas updated successfully.")
        chart.verify_x_axis_title_in_run_window(['PRICE_DOLLARS_BIN_1'],  msg = "Step 04.02 : Bin field is created and canvas updated successfully.")
        chart.verify_y_axis_label_in_run_window(['0', '3', '6', '9', '12', '15'], msg = "Step 04.03 : Bin field is created and canvas updated successfully.")
        chart.verify_y_axis_title_in_run_window(['CNT Price Dollars'], msg = "Step 04.04 : Bin field is created and canvas updated successfully.")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 53, msg = "Step 04.05 : Bin field is created and canvas updated successfully.")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g5!mbar!", "bar_blue", msg = "Step 04.06 : Bin field is created and canvas updated successfully")
        utils.capture_screenshot("04.01", Step4, expected_image_verify = True)
        
        Step5 = """
            STEP .05 : Click Save icon in the toolbar > Enter title as "C6459363" > Click Save button.
        """
        chart.switch_to_default_content()
        
        chart.select_item_in_top_toolbar("save")
        chart.wait_for_visible_text(save_css, "Save")
        
        chart.save_file_in_save_dialog("C6459363")
        utils.synchronize_until_element_disappear(save_css, chart.home_page_short_timesleep)
        utils.capture_screenshot("05.01", Step5)
        
        Step6 = """
            STEP 06 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        utils.capture_screenshot("06.01", Step6)
        
        Step7 = """
            STEP 07 : Restore the C6459363.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2FC6459363.fex
            Chart restored successfully without errors.
        """
        chart.edit_fex_using_api_url(folder_name = "P292_S11397%2FG435181", fex_name = 'C6459363')
        chart.wait_for_visible_text("#pfjTableChart_1", "CNT")
        utils.wait_for_page_loads(chart.home_page_long_timesleep) #firefox its required
        
        chart.verify_x_axis_label_in_preview(['20.00', '50.00', '60.00', '70.00', '80.00', '90.00', '100.00', '110.00', '120.00', '140.00', '150.00', '160.00', '170.00', '180.00', '190.00', '210.00', '220.00', '230.00', '240.00', '260.00', '270.00', '280.00', '290.00', '310.00', '330.00', '340.00', '360.00', '370.00', '380.00', '390.00', '440.00', '470.00', '480.00', '490.00', '520.00', '540.00', '590.00', '640.00', '680.00', '690.00', '780.00', '790.00', '880.00', '890.00', '990.00', '1,180.00', '1,290.00', '1,390.00', '1,990.00', '2,240.00', '3,390.00', '3,490.00', '3,990.00'] , msg = "Step 07.01 : Bin field is created and canvas updated successfully.")
        chart.verify_x_axis_title_in_preview(['PRICE_DOLLARS_BIN_1'],  msg = "Step 07.02 : Bin field is created and canvas updated successfully.")
        chart.verify_y_axis_label_in_preview(['0', '3', '6', '9', '12', '15'], msg = "Step 07.03 : Bin field is created and canvas updated successfully.")
        chart.verify_y_axis_title_in_preview(['CNT Price Dollars'], msg = "Step 07.04 : Bin field is created and canvas updated successfully.")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 53, msg = "Step 07.05 : Bin field is created and canvas updated successfully.")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g5!mbar!", "bar_blue", msg = "Step 07.06 : Bin field is created and canvas updated successfully")
        utils.capture_screenshot("07.01", Step7, expected_image_verify = True)
        
        Step8 = """
            STEP 08 : Logout using API
            http://machine:port/alias/service/wf_security_logout.js
        """
        chart.api_logout()
        utils.capture_screenshot("08.01", Step8)
 
if __name__ == '__main__':
    unittest.main()